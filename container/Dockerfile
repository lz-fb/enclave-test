
FROM amazonlinux

RUN yum install python3 -y

COPY gateway .
COPY service .
COPY test .

CMD ["python3", "test/test_nsm.py"]
