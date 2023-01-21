from pathlib import Path

import uvicorn
from settings import settings

if __name__ == '__main__':
    images_folder = Path("images")
    if not images_folder.exists():
        images_folder.mkdir()
    uvicorn.run(
        "app:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
        workers=4
    )
