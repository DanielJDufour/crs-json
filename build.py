from csv import DictReader
import json
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile, ZIP_DEFLATED
from urllib.request import urlopen

url = "https://s3.amazonaws.com/crs.csv/crs.csv.zip"
req = urlopen(url)
binary_data = BytesIO(req.read())

with ZipFile(binary_data) as z:
  with z.open("crs.csv") as f:
    print("f:", f)
    textWrapper = TextIOWrapper(f)
    dictReader = DictReader(textWrapper, delimiter="\t")
    data = list(dictReader)

str = json.dumps(data, indent=2)

with open("crs.json", "w") as f:
  # write intermediate file for testing and visualization purposes
  f.write(str)

# write zip file
with ZipFile("crs.json.zip", "w", ZIP_DEFLATED) as z:
  z.writestr("crs.json", str)
