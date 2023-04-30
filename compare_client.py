import grpc
import compare_pb2 as pb2
import compare_pb2_grpc as pb2_grpc


class CompareClient(object):
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

    def call_service(self, image, guid):
        """
        Client function to call the rpc for Compare
        """
        compare_rq = pb2.CompareRQ()
        compare_rq.image = image
        compare_rq.GUID = str(guid)
        print(f'{compare_rq}')
        return self.stub.Compare(compare_rq)
