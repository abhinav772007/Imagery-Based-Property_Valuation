import os
import time
import requests
import pandas as pd
from tqdm import tqdm
from PIL import Image
from io import BytesIO



DATA_PATH = "data/train.csv"
IMAGE_DIR = "data/arcgis_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

SIZE = 256
BUFFER = 0.0008
SLEEP_TIME = 0.25         
MAX_RETRIES = 5
BASE_URL = (
    "https://services.arcgisonline.com/ArcGIS/rest/services/"
    "World_Imagery/MapServer/export"
)
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})
def fetch_arcgis_image(lat, lon, idx):
    save_path = os.path.join(IMAGE_DIR, f"{idx}.jpg")

    if os.path.exists(save_path):
        return "skipped"
    xmin=lon-BUFFER
    ymin=lat-BUFFER
    xmax=lon+BUFFER
    ymax=lat+BUFFER
    params = {
        "bbox": f"{xmin},{ymin},{xmax},{ymax}",
        "bboxSR": 4326,
        "imageSR": 4326,
        "size": f"{SIZE},{SIZE}",
        "format": "png32",
        "f": "image"
    }
    for attempt in range(MAX_RETRIES):
        try:
            r=session.get(BASE_URL,params=params,timeout=20)
            r.raise_for_status()

            img=Image.open(BytesIO(r.content)).convert("RGB")
            img.save(
                save_path,
                format="JPEG",
                quality=85,
                subsampling=0
            )

            time.sleep(SLEEP_TIME)
            return "success"

        except Exception as e:
            time.sleep(2*(attempt + 1))

    print(f"failed {idx}")
    return "failed"



def main():
    df = pd.read_csv(DATA_PATH)

    success=skipped=failed=0

    for idx,row in tqdm(df.iterrows(),total=len(df)):
        status=fetch_arcgis_image(row["lat"], row["long"],idx)
        if status=="success":
            success+=1
        elif status=="skipped":
            skipped+=1
        else:
            failed+=1
    print(f"Downloaded : {success}")
    print(f"Skipped    : {skipped}")
    print(f"Failed     : {failed}")

if __name__ == "__main__":
    main()
