# Copyright (c) Meta, Inc. and its affiliates.

import base64
from typing import Any

import cbor2
from Crypto.PublicKey import RSA

from OpenSSL import crypto


def decode_att_doc(doc: bytes):
    # decodes CBOR2 document into human-readable format

    # https://github.com/richardfan1126/nitro-enclave-python-demo/blob/master/attestation_verifier/secretstore/attestation_verifier.py
    data = cbor2.loads(doc)

    # Header
    header = cbor2.loads(data[0])  # Example {"1": -35}
    uhdr = data[1]  # Example {}

    # PCRS
    att = cbor2.loads(data[2])
    # print(att.keys())

    pcrs = att["pcrs"]
    for i in pcrs:
        pcrs[i] = base64.b64encode(pcrs[i]).decode()

    # X509 Certificate
    cert = crypto.load_certificate(crypto.FILETYPE_ASN1, att["certificate"])
    # att['certificate'] = cert
    att["certificate"] = _cert_info(cert)

    # Certificate chain
    att["cabundle"] = [
        _cert_info(crypto.load_certificate(crypto.FILETYPE_ASN1, x))
        for x in att["cabundle"]
    ]

    # Public key
    public_key = RSA.import_key(att["public_key"])
    att["public_key"] = public_key

    return (header, uhdr, att)


def _cert_info(cert: crypto.X509) -> Any:
    # Returns dict of relevant fields
    cert_info = {
        "issuer": cert.get_issuer(),
        "notAfter": cert.get_notAfter(),
        "notBefore": cert.get_notBefore(),
        "pubkey": cert.get_pubkey(),
        "serialNum": cert.get_serial_number(),
        "sigAlg": cert.get_signature_algorithm(),
        "subject": cert.get_subject(),
        "version": cert.get_version(),
    }
    return cert_info
