# Copyright (c) Meta, Inc. and its affiliates.

from rsa_key import RSAKeyPair


class KeyManagementService:
    """Key management service for enclave process"""

    keyPair: RSAKeyPair

    def __init__(self):
        pass

    def generate_key_pair(self) -> None:
        """Generates a key pair of 2048 bits"""
        self.keyPair = RSAKeyPair(2048)

    def get_public_key(self) -> bytes:
        """Returns public key as DER format"""
        return self.keyPair.get_public_key()

    def get_private_key(self) -> bytes:
        """Returns private key as DER format"""
        return self.keyPair.get_private_key()
