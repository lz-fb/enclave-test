# Copyright (c) Meta, Inc. and its affiliates.

from service import key_management, onedocker_runner


def test_onedocker_init():
    """Tests whether Onedocker service can initialize using a KMS"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    assert runner

    # output for testing in local Docker image
    print("Onedocker runner service created")


if __name__ == "__main__":
    test_onedocker_init()

    # To connect to the enclave console, need to keep the process running
    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
