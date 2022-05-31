
FROM amazonlinux

RUN yum install python3 -y
RUN python3 -m pip install pycryptodome

COPY entity .
COPY gateway .
COPY service .
COPY test .

CMD ["run_tests.sh"]
