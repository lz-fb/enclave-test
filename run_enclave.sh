#!/bin/bash

# Exit on any failure
set -e

# Remove unneeded docker images
docker image prune

# Build docker image from Dockerfile
docker build -f container/Dockerfile -t enclave .
echo -e "\e[1;32m [ SUCCESS ] Built docker image \e[0m"

# Convert image to EIF
nitro-cli build-enclave --docker-uri enclave --output-file enclave.eif
echo -e "\e[1;32m [ SUCCESS ] Converted image to EIF \e[0m"

# Can only have one enclave
nitro-cli terminate-enclave --all

nitro-cli run-enclave --eif-path enclave.eif --memory 12288 --cpu-count 2 --debug-mode
echo -e "\e[1;32m [ SUCCESS ] Started enclave process \e[0m"

ENCLAVE_ID=$(nitro-cli describe-enclaves | jq -r .[0].EnclaveID)

echo -e "\e[1;36m [ INFO ] Connecting to enclave console \e[0m"
nitro-cli console --enclave-id "$ENCLAVE_ID"
