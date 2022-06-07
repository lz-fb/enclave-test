# Copyright (c) Meta, Inc. and its affiliates.

from enclave.test.test_kms import test_kms_create_rsa
from enclave.test.test_nsm import test_nsm_library_init
from enclave.test.test_odrunner import test_onedocker_init


def run_tests():
    test_kms_create_rsa()
    test_nsm_library_init()
    test_onedocker_init()


if __name__ == "__main__":
    run_tests()

    # To connect to the enclave console, need to keep the process running
    import time

    while True:
        time.sleep(1)
        print(".", end="", flush=True)
