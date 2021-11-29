#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

OUT_DIR="./cosmos_proto"

mkdir -p "$OUT_DIR"

echo "Processing proto files ..."

COSMOS_SDK_DIR="../cosmos-sdk/proto"
COSMOS_SDK_THIRD_PARTY_DIR="../cosmos-sdk/third_party/proto"
TERRA_DIR="../terra/proto"
OSMOSIS_DIR="../osmosis/proto"

protoc \
  --proto_path=${COSMOS_SDK_DIR} \
  --proto_path=${COSMOS_SDK_THIRD_PARTY_DIR} \
  --proto_path=${TERRA_DIR} \
  --proto_path=${OSMOSIS_DIR} \
  --python_betterproto_out="${OUT_DIR}" \
  $(find ${COSMOS_SDK_DIR} ${TERRA_DIR} ${OSMOSIS_DIR} -path -prune -o -name '*.proto' -print0 | xargs -0)
