#!/bin/bash -e

python3 -m grpc_tools.protoc -I../../pb --python_out=. --grpc_python_out=. ../../pb/ms.proto
