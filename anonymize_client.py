import grpc
import anonymize_pb2 as pb2
import anonymize_pb2_grpc as pb2_grpc


class AnonymizeClient(object):
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
        self.stub = pb2_grpc.AnonymizerStub(self.channel)

    def call_service(self, image, guid):
        """
        Client function to call the rpc for Compare
        """
        anonymize_rq = pb2.AnonymizeRQ()
        anonymize_rq.image = image
        anonymize_rq.GUID = guid
        print(f'{anonymize_rq}')
        return self.stub.Anonymize(anonymize_rq)
