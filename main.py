from urllib.parse import urlencode
from pycurl import Curl
import re
from datetime import datetime
import time
from sys import stdout
import json
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

def header_function(header_line):
    try:
        header_line = header_line.decode('iso-8859-1')
        if ':' not in header_line:
            return
        name, value = header_line.split(':', 1)
        name = name.strip().lower()
        value = value.strip()
        headers[name] = value
    except:
        print("something wrong")


def login():
    try:
        print('sedang login...')
        global headers
        headers = {}
        login = Curl()
        login.setopt(login.URL, "http://elearning.man1balam.sch.id/login/do_login")
        data = json.load(open('data_user.json', 'r'))
        pf = urlencode(data)
        login.setopt(login.POSTFIELDS, pf)
        login.setopt(login.WRITEDATA, buffer)
        login.setopt(login.COOKIEJAR, 'cookies.txt')
        login.setopt(login.HEADERFUNCTION, header_function)
        login.setopt(login.POST, True)
        login.perform()
        login.close()
        if 'content-type' in headers:
            content_type =  headers['content-type'].lower()
            match = re.search('application/json', content_type)
            if match:
                raise Exception("password atau username salah")
        body = buffer.getvalue()
        print('Berhasil login sebagai: ' + body.decode('UTF-8'))
    except Exception as error:
        print(error)
def absen(nama, url):
    try:
        print('Mengisi absensi ' + nama + '...')
        absen = Curl()
        absen.setopt(absen.URL, 'http://elearning.man1balam.sch.id/studentkelas/absensi/' + url)
        absen.setopt(absen.COOKIEFILE, 'cookies.txt')
        absen.setopt(absen.WRITEDATA, buffer)
        absen.perform()
        absen.close()
        body = buffer.getvalue()
        match = re.search('Session Anda sudah habis', body.decode('iso-8859-1'))
        if match:
            raise Exception('Session sudah habis')
        print('berhasil')
    except Exception as error:
        print(error)

if __name__ == '__main__':
    buffer = BytesIO()
    login()
    print('Mengambil data jadwal...')
    jadwal = json.load(open('jadwal.json', 'r'))
    print('Mencocokkan hari...')
    for list_jadwal in jadwal[datetime.now().strftime('%a')]:
        for nama, url in list_jadwal.items():
            absen(nama, url)