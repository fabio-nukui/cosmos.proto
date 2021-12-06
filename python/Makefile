.PHONY: all update-deps install proto-pull proto-gen format

################################################################################################
## VARIABLES
################################################################################################

COSMOS_SDK_VERSION ?= v0.44.5
TERRA_VERSION ?= v0.5.12
OSMOSIS_VERSION ?= v4.2.0

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
