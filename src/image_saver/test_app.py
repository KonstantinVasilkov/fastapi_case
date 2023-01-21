import pathlib
import uuid
from pathlib import Path

from fastapi.testclient import TestClient

from src.image_saver.app import app

client = TestClient(app)


def test_create_image():
    boundary = uuid.uuid4().hex
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    file_name = 'test_image.jpg'
    path_to_image = Path.cwd().joinpath(f'tests/{file_name}')
    with open(path_to_image, "rb") as image_file:
        response = client.post(
            "/images",
            files={"file": (file_name, image_file, "image/jpeg")},
            headers=headers
        )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] is not None
    file_path = f"images/{response.json()['id']}.jpg"
    assert pathlib.Path(file_path).exists()


def test_create_image_invalid_ext():
    boundary = uuid.uuid4().hex
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    file_name = 'test_image.txt'
    path_to_image = Path.cwd().joinpath(f'tests/{file_name}')
    with open(path_to_image, "rb") as image_file:
        response = client.post(
            "/images",
            files={"file": (file_name, image_file, "image/jpeg")},
            headers=headers
        )
    assert response.status_code == 415
    json_response = response.json()
    assert "detail" in json_response
    assert json_response["detail"] == "Only jpeg, jpg, png files are allowed!"
