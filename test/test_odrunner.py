# Copyright (c) Meta, Inc. and its affiliates.

from enclave.service import key_management, onedocker_runner


def test_onedocker_init():
    """Tests whether Onedocker service can initialize using a KMS"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    assert runner

    # output for testing in local Docker image
    print("Onedocker runner service created")


def test_onedocker_get_att(print_attestation: bool = True):
    """Tests whether Onedocker service can generate attestation document"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    att = runner.get_attestation_document()
    assert att

    # output for testing in local Docker image
    print("Attestation document generated")

    if print_attestation:
        print("==== Attestation document starts below ====")
        print(att)
        print("==== End of attestation document ====")


if __name__ == "__main__":
    test_onedocker_init()
    test_onedocker_get_att()

    # To connect to the enclave console, need to keep the process running
    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
