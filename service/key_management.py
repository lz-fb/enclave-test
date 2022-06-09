# Copyright (c) Meta, Inc. and its affiliates.

from enum import Enum

from Crypto.PublicKey import RSA
from enclave.entity.key_pair_details import KeyPairDetails


class KeyAlgorithm(Enum):
    # For now we only support RSA since it is one of the most common algorithms, will add more key algorithms in the future
    RSA = "RSA"


class KeyManagementService:
    """Key management service for enclave process"""

    keyPair: KeyPairDetails

    def __init__(self, key_alg: KeyAlgorithm = KeyAlgorithm.RSA, key_size: int = 4096):
        """Upon initialization generates a key pair. Currently only supports RSA."""
        self.keyPair = self._generate_key_pair(key_alg, key_size)

    def _generate_key_pair(
        self, key_alg: KeyAlgorithm, key_size: int, key_format: str = "DER"
    ) -> KeyPairDetails:
        if key_alg == KeyAlgorithm.RSA:
            private_key = RSA.generate(key_size)
            public_key = private_key.publickey()
            return KeyPairDetails(
                private_key.export_key(key_format),
                public_key.export_key(key_format),
            )
        else:
            raise NotImplementedError

    def get_public_key(self) -> bytes:
        """Returns public key as DER format"""
        return self.keyPair.public_key

    def get_private_key(self) -> bytes:
        """Returns private key as DER format"""
        return self.keyPair.private_key
