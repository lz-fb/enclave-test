# Copyright (c) Meta, Inc. and its affiliates.

from . import libnsm


class NitroGateway:
    """Wraps NSM library"""

    def __init__(self):
        self._lib = libnsm.nsm_lib_init()

    def get_attestation_document(self) -> bytes:
        pass
