# Copyright (c) Meta, Inc. and its affiliates.

import gateway.nsm as nsm


def test_nsm_library_init():
    """Tests whether NSM library can initialize"""
    gateway = nsm.NitroGateway()
    # assert is not needed but prevents 'unused variable'
    assert gateway
