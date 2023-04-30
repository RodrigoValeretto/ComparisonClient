# ComparisonClient
A python comparison client used to test comparison service, another repository from this github profile.

## Running local
To run this client locally on your computer it is necessary to download the LFW image dataset encountered in
http://vis-www.cs.umass.edu/lfw/

It is also important to install and configure GRPC tools for python, the documentation can be found in https://grpc.io/docs/languages/python/quickstart/

To generate the GRPC files correctly use the command
```shell
python3 -m grpc_tools.protoc --proto_path=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/*.proto
```

To run the project, being in the root folder of it, run
```shell
python3 client.py
```
