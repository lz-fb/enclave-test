# Copyright (c) Meta, Inc. and its affiliates.

import pprint

from enclave.gateway import att_doc
from enclave.service import key_management, onedocker_runner


def test_onedocker_init():
    """Tests whether Onedocker service can initialize using a KMS"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    assert runner

    # output for testing in local Docker image
    print("Onedocker runner service created")


def test_onedocker_get_att():
    """Tests whether Onedocker service can generate attestation document"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    att = runner.get_attestation_document()
    assert att

    # output for testing in local Docker image
    print("Attestation document generated")


def test_onedocker_print_att():
    """Tests decoding attestation document"""
    kms = key_management.KeyManagementService(key_size=2048)
    runner = onedocker_runner.OneDockerRunnerService(kms)
    att = runner.get_attestation_document()
    assert att

    print("==== Attestation document starts below ====")
    pprint.pprint(att_doc.decode_att_doc(att))
    print("==== End of attestation document ====")


if __name__ == "__main__":
    test_onedocker_init()
    test_onedocker_get_att()
    test_onedocker_print_att()

    # To connect to the enclave console, need to keep the process running
    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
