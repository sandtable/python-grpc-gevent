from gevent import monkey
monkey.patch_all()

import grpc
import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()

from concurrent import futures
import random
import time
import sys

import service_pb2
import service_pb2_grpc


class ServerServicer(service_pb2_grpc.ServerServicer):
    def Foo(self, request, context):
        print('Accept new request')
        
        time.sleep(5)
        
        print('Done with request')
        return service_pb2.Empty()


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServerServicer_to_server(ServerServicer(), server)

    server.add_insecure_port('[::]:50001')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
