#!/bin/bash

# Build docker image from Dockerfile
docker build -f container/Dockerfile -t enclave .

# Convert image to EIF
nitro-cli build-enclave --docker-uri enclave --output-file enclave.eif

# Can only have one enclave
nitro-cli terminate-enclave --all

nitro-cli run-enclave --eif-path enclave.eif --memory 12288 --cpu-count 2 --debug-mode

ENCLAVE_ID=$(nitro-cli describe-enclaves | jq -r .[0].EnclaveID)
nitro-cli console --enclave-id "$ENCLAVE_ID"
