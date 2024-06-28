from hate.logger import logging
from hate.exception import CustomException
import sys
import gdown


url = "https://drive.google.com/file/d/1BS1689dM2Hqu9f58pbreDsy0yZylp2Tg/view?usp=drive_link"

file_id = url.split("/")[-2]

print(file_id)

prefix = "https://drive.google.com/uc?/export=download&id="
gdown.download(prefix + file_id, "download/data.zip")