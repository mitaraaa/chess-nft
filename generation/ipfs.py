import json
import os

from dotenv import load_dotenv
from web3storage import Client

load_dotenv()


api_token = os.getenv("WEB3STORAGE_TOKEN")

client = Client(api_token)

metadata_cids = []

for index in range(150):
    response = client.upload_file(f"out/images/{index}.png")
    cid = response["cid"]

    print(f"Uploaded {index}.png to {cid}")

    with open(f"out/metadata/{index}.json", "r") as metadata_file:
        metadata: dict = json.loads(metadata_file.read())

        metadata["image"] = f"ipfs://{cid}"

        with open(f"out/metadata/{index}.json", "w") as metadata_file:
            json.dump(metadata, metadata_file)

        response = client.upload_file(f"out/metadata/{index}.json")
        cid = response["cid"]

        metadata_cids.append(cid)

        print(f"Uploaded {index}.json to {cid}")


with open("out/cids.json", "w") as cids_file:
    json.dump(metadata_cids, cids_file)
