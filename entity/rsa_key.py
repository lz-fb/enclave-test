# Copyright (c) Meta, Inc. and its affiliates.

from Crypto.PublicKey import RSA


class RSAKeyPair:
    """Entity wrapper for RSA keypair"""

    _private_key: RSA.RsaKey
    _public_key: RSA.RsaKey

    def __init__(self, nbits: int):
        """Generates an RSA keypair of length nbits"""
        self._private_key = RSA.generate(nbits)
        self._public_key = self._rsa_key.publickey()

    def get_public_key(self) -> bytes:
        """Export public key as DER format"""
        return self._public_key.export_key("DER")

    def get_private_key(self) -> bytes:
        """Export private key as DER format"""
        return self._private_key.export_key("DER")
