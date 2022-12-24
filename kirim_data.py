import requests
import time

urlpost = "http://www.anggilubis1234.000webhost.com/tambah_data.php/datakomputer/deteksi"
#urlget = "http://192.168.1.3/belajar/index.php/raspi/getinsert"
#urlgambar = "http://192.168.1.3/belajar/index.php/raspi/simpangambar"


tespost = "Helo POST" 
tesget = "Helo GET"

#img = "gambar.jpg"
#files = {"image":open(img, "rb")}


while True:
    try:
        #kirim = requests.get(urlget, params={"data":tesget})
        kirim = requests.post(urlpost, data={"deteksi":tespost})
        #kirim = requests.post(urlgambar, data={"gambar":"save"}, files=files)

        print(kirim.text)
    except:
        print("error")
        
    time.sleep(1)
