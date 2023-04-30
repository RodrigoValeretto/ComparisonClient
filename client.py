
# Code to generate GPRC classes
# python3 -m grpc_tools.protoc --proto_path=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/compare.proto

from uuid import uuid4
import grpc
import compare_pb2 as pb2
import compare_pb2_grpc as pb2_grpc

image_path = "./lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 5099

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.ComparerStub(self.channel)

    def get_compare(self, image, guid):
        """
        Client function to call the rpc for Compare
        """
        compare_rq = pb2.CompareRQ()
        compare_rq.image = image
        compare_rq.GUID = str(guid)
        print(f'{compare_rq}')
        return self.stub.Compare(compare_rq)


def open_image(path):
    with open(path, "rb") as image:
        f = image.read()
        b = bytes(f)
        return b


if __name__ == '__main__':
    client = UnaryClient()

    image_bytes = open_image(image_path)
    guid = uuid4()

    compare_rs = client.get_compare(image_bytes, guid)
    print(f'{compare_rs}')
