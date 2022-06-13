
docker build -f container/Dockerfile -t enclave .

nitro-cli build-enclave --docker-uri enclave --output-file enclave.eif
nitro-cli run-enclave --eif-path enclave.eif --memory 4096 --cpu-count 2 --debug-mode

ENCLAVE_ID=$(nitro-cli describe-enclaves | jq -r .[0].EnclaveID)
nitro-cli console --enclave-id $ENCLAVE_ID
