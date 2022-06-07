# Copyright (c) Meta, Inc. and its affiliates.

from enclave.service.key_management import KeyManagementService


def test_kms_create_rsa():
    """Tests whether KMS can create an RSA keypair"""
    kms = KeyManagementService(key_size=2048)
    assert kms

    # output for testing in local Docker image
    print("KMS and keypair created")


if __name__ == "__main__":
    test_kms_create_rsa()

    # To connect to the enclave console, need to keep the process running
    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
