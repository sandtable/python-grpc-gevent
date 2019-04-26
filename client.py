import grpc

import service_pb2
import service_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:50001')
    stub = service_pb2_grpc.ServerStub(channel)

    print('Send request')
    stub.Foo(service_pb2.Empty())
    print('Request successful')

if __name__ == '__main__':
    main()
