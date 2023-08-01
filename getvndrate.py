#pip install PyPDF2
#pip install requests

import requests
import datetime
from PyPDF2 import PdfReader
import os

def download_pdf(url, file_name, headers):
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)

headers = {
    "User-Agent": "Chrome/51.0.2704.103",
    }
    # Define URL of a PDF
url = "https://www.bk.mufg.jp/report/vietnamrate/hochiminhcity_rate.pdf"

   # Define PDF file name
x = datetime.datetime.now()
timenow = str(x).replace(' ','').replace(':','').replace('-','').replace('.','')
file_name = url.split("/")[-1].split('.')[0] + timenow + ".pdf"

    # Download PDF
download_pdf(url, file_name, headers)

# creating a pdf reader object
reader = PdfReader(file_name)

page = reader.pages[0]
text = page.extract_text()
content_array = text.split('\n')

for line in content_array:
    if line == "- Mua  VND":
        rate_index = content_array.index(line) + 2
        print(content_array[0].split('        ')[-1].split('-')[-1])
        print("USD to VND = " + content_array[rate_index].split(' ')[0])

os.remove(file_name)