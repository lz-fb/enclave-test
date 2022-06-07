# Copyright (c) Meta, Inc. and its affiliates.

FROM amazonlinux

RUN yum install python3 -y
RUN python3 -m pip install pycryptodome

COPY . .

CMD ["python3", "run_integration_tests.py"]
