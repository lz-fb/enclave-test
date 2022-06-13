# Copyright (c) Meta, Inc. and its affiliates.

import cbor2

from enclave.gateway import libnsm


class NitroGateway:
    """Wraps NSM library"""

    def __init__(self):
        self._lib = libnsm.nsm_lib_init()

    def get_attestation_document(self, public_key: bytes) -> bytes:
        """public_key must be in DER format
        returns decoded document"""
        document = libnsm.nsm_get_attestation_doc(
            self._lib, public_key, len(public_key)
        ) # document is bytes in CBOR2 format

        return self._decode_cbor2(document)

    def _decode_cbor2(self, doc: bytes) -> dict:
        # decodes CBOR2 document into generic JSON object
        # https://github.com/richardfan1126/nitro-enclave-python-demo/blob/master/attestation_verifier/secretstore/attestation_verifier.py
        data = cbor2.loads(doc)

        # PCR
        doc_obj = cbor2.loads(data[2])
        return doc_obj
        #pcrs = doc_obj['pcrs']

        # Header
        #header = cbor2.loads(data[0])
