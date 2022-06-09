# Copyright (c) Meta, Inc. and its affiliates.

import unittest
from unittest.mock import MagicMock

from enclave.gateway.nsm import NitroGateway
from enclave.service.onedocker_runner import OneDockerRunnerService


class TestODRunner(unittest.TestCase):
    TEST_PLAINTEXT = b"Hello!"
    TEST_CIPHERTEXT = b"Test"
    TEST_ATT_DOC = b"Attestation"

    def setUp(self):
        self.kms = MagicMock()
        self.odrunner = OneDockerRunnerService(self.kms)

    def test_init(self):
        self.odrunner = OneDockerRunnerService(self.kms)

        self.assertIsInstance(self.odrunner.nsm, NitroGateway)

    def test_get_attestation(self):
        # Arrange
        mock_nsm = MagicMock()
        mock_nsm.get_attestation_document.return_value = self.TEST_ATT_DOC
        self.odrunner.nsm = mock_nsm

        # Act
        att = self.odrunner.get_attestation_document()

        # Assert
        self.assertEqual(att, self.TEST_ATT_DOC)
        self.odrunner.nsm.get_attestation_document.assert_called()

    def test_decrypt_data(self):
        # Arrange
        mock_cipher_lib = MagicMock()
        mock_cipher_obj = MagicMock()

        mock_cipher_lib.new.return_value = mock_cipher_obj
        mock_cipher_obj.decrypt.return_value = self.TEST_PLAINTEXT

        # Act
        data = self.odrunner.decrypt_data(self.TEST_CIPHERTEXT, mock_cipher_lib)

        # Assert
        self.assertEqual(data, self.TEST_PLAINTEXT)

        mock_cipher_obj.decrypt.assert_called_with(self.TEST_CIPHERTEXT)


if __name__ == "__main__":
    unittest.main()
