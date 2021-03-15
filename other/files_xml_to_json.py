import ftplib
from zipfile import ZipFile
import xmltodict, json


filename = 'pubmed21n0001.gz'

# ftp = ftplib.FTP("ftp.ncbi.nlm.nih.gov")
# ftp.login("anonymous", "")
# ftp.cwd("/pubmed/baseline/")

# file_list = []
# ftp.retrlines('LIST', lambda x: file_list.append(x.split()))
# print(file_list)

# ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# ftp.quit()

import gzip

with gzip.open(filename, 'rb') as f:
    file_content = f.read()

obj = xmltodict.parse(file_content)

f = open("test.json", "a")
f.write(json.dumps(obj))
f.close()