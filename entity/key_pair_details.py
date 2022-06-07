# Copyright (c) Meta, Inc. and its affiliates.

from dataclasses import dataclass


@dataclass
class KeyPairDetails:
    private_key: bytes
    public_key: bytes
