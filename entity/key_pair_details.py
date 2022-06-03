# Copyright (c) Meta, Inc. and its affiliates.

from dataclasses import dataclass


@dataclass
class KeyPairDetails:
    private_key_pem: bytes
    public_key_pem: bytes
