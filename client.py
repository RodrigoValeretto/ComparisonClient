# Code to generate GPRC classes
# python3 -m grpc_tools.protoc --proto_path=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/compare.proto

import sys
from uuid import uuid4
from compare_client import CompareClient
from anonymize_client import AnonymizeClient
import asyncio

image_path = "./lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"
guid = None


def open_image(path):
    with open(path, "rb") as image:
        f = image.read()
        b = bytes(f)
        return b


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This client takes one argument: integer 1 or 2")
        print("1 - Call anonymization service")
        print("2 - Call comparison service")
        sys.exit()

    match sys.argv[1]:
        case "1":
            client = AnonymizeClient()
        case "2":
            client = CompareClient()

    try:
        image_bytes = open_image(image_path)
        if guid == None:
            guid = str(uuid4())
    except e:
        print("Error opening image")

    res = client.call_service(image_bytes, guid)
    print(f"{res}")
