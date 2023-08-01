# pythonPDF

This is specific script for extract the VND rate exchange from USD following MUFG public data.
The script runs as flow:
 - download pdf
 - save pdf as unique file name
 - read pdf into array
 - find keywords "Mua VND"
 - get the rate
 - remove the pdf file

How to use it?

$ pip install venv
$ python -m venv pypdf-venv


$ cd pythonPDF/pypdf-venv
$ . bin/activate

$ pip install -r requirements.txt
$ python ../getvndrate.py
