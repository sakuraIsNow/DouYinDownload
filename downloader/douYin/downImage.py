import os
import filetype
import requests
from PIL import Image
from pathlib import Path

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch",
    # 'Connection': 'close',
}

def download_image(image_url, dst_dir, file_name, timeout=20):
    Path(dst_dir).mkdir(parents=True, exist_ok=True)
    response = None
    file_path = os.path.join(dst_dir, file_name)
    try_times = 0
    while True:
        try:
            try_times += 1
            response = requests.get(
                image_url, headers=headers, timeout=timeout)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            response.close()
            file_type = filetype.guess(file_path).extension

            if file_type in ["jpg", "jpeg", "png", "bmp", "webp"]:
                new_file_name = "{}.{}".format(file_name, 'png')
                new_file_path = os.path.join(dst_dir, new_file_name)
                img = Image.open(file_path)
                img.save(new_file_path)
                os.remove(file_path)
                print("## OK:  {}  {}".format(new_file_name, image_url))
            else:
                os.remove(file_path)
                print("## Err: TYPE({})  {}".format(file_type, image_url))
            break
        except Exception as e:
            if try_times < 3:
                continue
            if response:
                response.close()
            print("## Fail:  {}  {}".format(image_url, e.args))
            break




