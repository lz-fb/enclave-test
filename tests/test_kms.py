# Copyright (c) Meta, Inc. and its affiliates.

import unittest
from unittest.mock import MagicMock

from enclave.entity.key_pair_details import KeyPairDetails
from enclave.service.key_management import KeyAlgorithm, KeyManagementService


class TestKMS(unittest.TestCase):
    TEST_KEY_ALGORITHM = KeyAlgorithm.RSA
    TEST_KEY_SIZE = 2048
    TEST_PUBLICKEY = b"hello"
    TEST_PRIVATEKEY = b"goodbye"
    TEST_KEYPAIR = KeyPairDetails(TEST_PRIVATEKEY, TEST_PUBLICKEY)

    def test_init(self):
        # Arrange
        KeyManagementService._generate_key_pair = MagicMock(
            return_value=self.TEST_KEYPAIR
        )

        # Act
        kms = KeyManagementService(
            key_alg=self.TEST_KEY_ALGORITHM, key_size=self.TEST_KEY_SIZE
        )

        # Assert
        self.assertEqual(kms.get_public_key(), self.TEST_PUBLICKEY)
        kms._generate_key_pair.assert_called_with(
            self.TEST_KEY_ALGORITHM, self.TEST_KEY_SIZE
        )

    def test_generate_key_pair(self):
        # Arrange
        kms = KeyManagementService(
            key_alg=self.TEST_KEY_ALGORITHM, key_size=self.TEST_KEY_SIZE
        )

        # Act
        key_pair = kms._generate_key_pair(KeyAlgorithm.RSA, key_size=self.TEST_KEY_SIZE)

        # Assert
        self.assertIsInstance(key_pair, KeyPairDetails)

    def test_get_public_key(self):
        kms = KeyManagementService(
            key_alg=self.TEST_KEY_ALGORITHM, key_size=self.TEST_KEY_SIZE
        )
        self.assertIsInstance(kms.get_public_key(), bytes)

    def test_get_private_key(self):
        kms = KeyManagementService(
            key_alg=self.TEST_KEY_ALGORITHM, key_size=self.TEST_KEY_SIZE
        )
        self.assertIsInstance(kms.get_private_key(), bytes)


if __name__ == "__main__":
    unittest.main()
