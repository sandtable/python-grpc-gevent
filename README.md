# Using gevent with gRPC in Python

This repository provides a simple example of using gevent server-side for gRPC using Python.

Python 3.6

gRPC 1.14.0

## Install dependencies

```
pip install -r requirements.txt
```

## Generate gRPC stubs

```
make stubs
```

## Run server

```
make server
```

## Run client

```
make client
```