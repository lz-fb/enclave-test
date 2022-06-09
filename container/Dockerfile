# Copyright (c) Meta, Inc. and its affiliates.

FROM amazonlinux

RUN yum install python3 -y
RUN python3 -m pip install pycryptodome

COPY . ./enclave/

CMD ["python3", "-m", "enclave.run_integration_tests"]
