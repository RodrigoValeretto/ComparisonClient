# Code to generate GPRC classes
# python3 -m grpc_tools.protoc --proto_path=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/compare.proto

import sys
from uuid import uuid4
from compare_client import CompareClient
from anonymize_client import AnonymizeClient
import numpy as np
import asyncio
from PIL import Image

image_path_1 = "./lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"
image_path_2 = "./lfw/Alexander_Downer/Alexander_Downer_0001.jpg"
image_path_3 = "./lfw/Alexander_Downer/Alexander_Downer_0002.jpg"
image_path_4 = "./lfw/Alexander_Downer/Alexander_Downer_0003.jpg"
image_path_5 = "./lfw/Alexander_Downer/Alexander_Downer_0004.jpg"

image_path = image_path_2

guid = "8d1c0c1d-1634-4f81-9d70-696ba5e726ab"


def open_image(path):
    with open(path, "rb") as image:
        f = image.read()
        return f


def open_image2(path):
    image = Image.open(path)
    return image.tobytes()


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
    except Exception as e:
        print("Error creating request:", e)
        exit()

    res = client.call_service(image_bytes, guid)
    print(res)
