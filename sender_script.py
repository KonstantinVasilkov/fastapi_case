import argparse
import asyncio
import csv
import uuid
from pathlib import Path
from typing import Any

import aiohttp


async def post_image_to_api(
        session: aiohttp.ClientSession,
        file_path: Path
) -> tuple[Path, Any]:
    boundary = uuid.uuid4().hex
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }

    with open(file_path, "rb") as image_file:
        data = aiohttp.FormData()
        data.add_field("file", image_file, filename=file_path.name)
        async with session.post("http://localhost:8000/images", data=data) as resp:
            json_response = await resp.json()
            return file_path, json_response["id"]


async def main(folder_path: str):
    folder_path = Path(folder_path)
    if not folder_path.exists():
        print(f"Folder {folder_path} does not exist.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = []
        for file_path in folder_path.glob("*.*"):
            extension = file_path.suffix
            if file_path.is_file() and extension in {'.jpeg', '.jpg', '.png'}:
                tasks.append(post_image_to_api(session, file_path))

        results = await asyncio.gather(*tasks)

    with open("results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder_path",
        help="Path to the folder containing the images"
    )
    args = parser.parse_args()
    asyncio.run(main(args.folder_path))
