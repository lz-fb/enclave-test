# Copyright (c) Meta, Inc. and its affiliates.

import nsm


def test_nsm_library_init():
    """Tests whether NSM library can initialize"""
    gateway = nsm.NitroGateway()
    # assert is not needed but prevents 'unused variable'
    assert gateway
    print("Nitro gateway created") # output for testing in local Docker image

if __name__ == "__main__":
    test_nsm_library_init()
