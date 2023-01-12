import sys

from hello_world import app

import grpc

app.build()
import grippy_pb2
import grippy_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grippy_pb2_grpc.GrippyStub(channel)
        response = stub.greet(grippy_pb2.greetRequest(times=3, name='World!'))
    print(response.return_val)
