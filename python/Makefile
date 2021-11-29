.PHONY: all update-deps install proto-pull proto-gen format

################################################################################################
## VARIABLES
################################################################################################

COSMOS_SDK_VERSION ?= v0.44.3
TERRA_VERSION ?= 746a15f1bd83d62cd284e4af9471dc58701b3e33
OSMOSIS_VERSION ?= main

################################################################################################
## GENERAL COMMANDS
################################################################################################

all: install proto-pull proto-gen build

update-deps:
	@echo "Updating dependencies"
	poetry update

install:
	@echo "Installing dependencies"
	poetry install --no-root

proto-pull:
	@echo "Pull external .proto files"
	git submodule update --init --recursive
	(cd ../cosmos-sdk && git fetch && git checkout ${COSMOS_SDK_VERSION})
	(cd ../terra && git fetch && git checkout ${TERRA_VERSION})
	(cd ../osmosis && git fetch && git checkout ${OSMOSIS_VERSION})

proto-gen:
	@echo "Generating Protobuf files"
	./scripts/proto-gen.sh

build:
	@echo "Building distribution artifacts"
	poetry install
	poetry build
