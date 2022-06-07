# Copyright (c) Meta, Inc. and its affiliates.

from enclave.gateway import libnsm


class NitroGateway:
    """Wraps NSM library"""

    def __init__(self):
        self._lib = libnsm.nsm_lib_init()

    def get_attestation_document(self, public_key: bytes) -> bytes:
        """public_key must be in DER format"""
        document = libnsm.nsm_get_attestation_doc(
            self._lib, public_key, len(public_key)
        )
        return document
