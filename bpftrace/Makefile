DOCKER_REPO := rsysio/bpftrace
DOCKER_TAG ?= latest
DOWNLOAD_URL := https://github.com/iovisor/bpftrace/releases/download/v0.14.0/bpftrace

build:
	docker build -t ${DOCKER_REPO}:${DOCKER_TAG} .

run:
	docker run
