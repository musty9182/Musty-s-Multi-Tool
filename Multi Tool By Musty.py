import requests
import os
import colorama
import json
import time
import sys

basarisiz = r"""
 ██████╗ ██╗██████╗ ██╗███████╗                               
██╔════╝ ██║██╔══██╗██║██╔════╝                               
██║  ███╗██║██████╔╝██║███████╗                               
██║   ██║██║██╔══██╗██║╚════██║                               
╚██████╔╝██║██║  ██║██║███████║                               
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝╚══════╝                               
                                                              
██████╗  █████╗ ███████╗ █████╗ ██████╗ ██╗███████╗██╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝██║╚══███╔╝
██████╔╝███████║███████╗███████║██████╔╝██║███████╗██║  ███╔╝ 
██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║╚════██║██║ ███╔╝  
██████╔╝██║  ██║███████║██║  ██║██║  ██║██║███████║██║███████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚══════╝"""



basarili= r"""
 ██████╗ ██╗██████╗ ██╗███████╗                       
██╔════╝ ██║██╔══██╗██║██╔════╝                       
██║  ███╗██║██████╔╝██║███████╗                       
██║   ██║██║██╔══██╗██║╚════██║                       
╚██████╔╝██║██║  ██║██║███████║                       
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝╚══════╝                       
                                                      
██████╗  █████╗ ███████╗ █████╗ ██████╗ ██╗██╗     ██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██║     ██║
██████╔╝███████║███████╗███████║██████╔╝██║██║     ██║
██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║██║     ██║
██████╔╝██║  ██║███████║██║  ██║██║  ██║██║███████╗██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝
"""

filigran = r"""
███╗   ███╗██╗   ██╗███████╗████████╗██╗   ██╗███████╗                      
████╗ ████║██║   ██║██╔════╝╚══██╔══╝╚██╗ ██╔╝██╔════╝                      
██╔████╔██║██║   ██║███████╗   ██║    ╚████╔╝ ███████╗                      
██║╚██╔╝██║██║   ██║╚════██║   ██║     ╚██╔╝  ╚════██║                      
██║ ╚═╝ ██║╚██████╔╝███████║   ██║      ██║   ███████║                      
╚═╝     ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝                      
                                                                            
███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ """



def havaDurumu():
    os.system("cls||clear")
    print(colorama.Fore.GREEN + filigran)
    print(colorama.Fore.WHITE + "Lütfen Hava Durumunu Bulmak İstediğiniz Şehri Giriniz.")
    sehir = input(colorama.Fore.GREEN)
    api = f"https://geocoding-api.open-meteo.com/v1/search?name={sehir}&count=1&language=tr&format=json"
    try:
        r = requests.get(api)
        data = r.json()
        enlem = data["results"][0]["latitude"]
        boylam = data["results"][0]["longitude"]
        print(enlem,boylam)
        params ={
            "latitude": enlem,
            "longitude": boylam,
            "current": ["temperature_2m"],
            "hourly": ["temperature_2m"],
            "timezone": "auto",
        }
        havaApi = "https://api.open-meteo.com/v1/forecast"
        r = requests.get(havaApi,params=params)
        data = r.json()
        current = data["current"]
        if r.status_code == 200:
            print(f"Şu An Ki Sıcaklık: {current["temperature_2m"]}")
    except KeyError:
        print(colorama.Fore.RED + "Hata! Şehir Bulunamadı Tekrar Dene!")
        time.sleep(2)
    except Exception as hata:
        print(colorama.Fore.RED + f"Beklenmedik Bir Hata Oluştu Bize Bildirin...,{hata}")
        print(colorama.Fore.BLUE + "https://musty.com")
        print("Devam Etmek İçin Herhangi Bir Tuşa Basın...")
        input()
        start()





def urlKisalt():
    os.system("cls||clear")
    print(colorama.Fore.GREEN + filigran)
    print(colorama.Fore.WHITE + "Lütfen Kısaltmak İstediğiniz Linki Giriniz:")
    uzunLink = input().strip()

    if not uzunLink.startswith("http"):
        uzunLink = "https://" + uzunLink

    if not uzunLink:
        print(colorama.Fore.RED + "Uzun Link Boş Olamaz!")
        time.sleep(2)
        urlKisalt()
        return

    
    apiUrl = "http://tinyurl.com/api-create.php"

    params = {"url": uzunLink}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    try:
        r = requests.get(
            apiUrl, 
            params=params, 
            headers=headers,
            timeout=15,
            verify=True,
            proxies={}
        )
        
        if r.status_code == 200:
            kısaUrl = r.text.strip()
            print(colorama.Fore.GREEN + f"Url Başarıyla Kısaltıldı: {kısaUrl}")
        else:
            print(colorama.Fore.RED + f"Hata! Status: {r.status_code}")
            print(r.text)
            
    except Exception as hata:
        print(colorama.Fore.RED + f"Beklenmedik Hata: {hata}")




def webhookMesaj():
    os.system("cls")
    print(colorama.Fore.GREEN + filigran)
    print()
    print(colorama.Fore.WHITE + "Lütfen Webhook URL'ini Giriniz.")
    WEBHOOK_URL = input(colorama.Fore.GREEN)
    print(colorama.Fore.WHITE+"Lütfen Mesajı Yazınız!")
    mesaj = input(colorama.Fore.GREEN)
    print(colorama.Fore.WHITE+"Lütfen Bota İsim Veriniz!")
    isim = input(colorama.Fore.GREEN)
    data = {
        "content": mesaj,
        "username": isim
    }
    try:
        r = requests.post(WEBHOOK_URL,json=data)
        if r.status_code == 204:
            print(colorama.Fore.WHITE+"Mesaj Başarıyla Gönderildi")
        print(colorama.Fore.BLUE + "Lütfen Yapmak İstediğiniz İşlemi Seçin")
        print(colorama.Fore.WHITE + "1 = IP Sorgulama")
        print("2 = Webhook Mesaj")
        print("3 = Çıkış")
        islem = input(colorama.Fore.GREEN)
        if islem == "1":
            ipSorgu()
        elif islem == "2":
            webhookMesaj()
        elif islem == "3":
            sys.exit()
        else:
            print(colorama.Fore.RED + "Hatalı Seçim Menüye Dönülüyor!")
            time.sleep(2)
            start()

    except Exception as hata:
        
        print(colorama.Fore.RED + f"MESAJ GÖNDERİLİRKEN BİR HATA OLUŞTU! {hata}")
        print()
        print("Menüye Dönem İçin Bir Tuşa Bas...")
        input()
        start()

def ipSorgu():
    os.system("cls")
    print(colorama.Back.BLACK+colorama.Fore.GREEN + filigran)
    print()
    print(colorama.Fore.BLUE+"Sorgulanacak IP Adresini Giriniz!")
    ip =input(colorama.Fore.WHITE)
    r = requests.get(f"http://ipwho.is/{ip}")
    data = r.json()
    sec = data.get("security",{})
    con = data.get("connection",{})
    try:
        print(colorama.Fore.WHITE + f"Ülke: {data["country"]}")
        print(f"Şehir: {data["city"]}")
        print(f"Kıta: {data["continent"]}")
        print(f"Bölge: {data["region"]}")
        print(f"Enlem Kordinatları: {data["latitude"]}")
        print(f"Boylam Kordinatları: {data["longitude"]}")
        print(f"VPN: {sec.get('vpn', 'Bilinmiyor')}")
        print(f"Proxy: {sec.get('proxy', 'Bilinmiyor')}")
        print(f"Tor: {sec.get('tor', 'Bilinmiyor')}")
        print(f"İnternet Servis Sağlayıcısı: {con.get("isp","Bilinmiyor")}")
    except KeyError:
        print(colorama.Fore.RED + "Geçersiz IP adresi Lütfen Tekrar Deneyin!")
        time.sleep(2)
        ipSorgu()
    print()
    print(colorama.Fore.BLUE + "Lütfen Yapmak İstediğiniz İşlemi Seçin")
    print(colorama.Fore.WHITE + "1 = IP Sorgulama")
    print("2 = Webhook Mesaj")
    print("3 = Çıkış")
    print("4 = URL Kısaltıcı")
    islem = input(colorama.Fore.GREEN)
    if islem == "1":
        ipSorgu()
    elif islem == "2":
        webhookMesaj()
    elif islem == "3":
        urlKisalt()
    elif islem == "4":
        sys.exit()
    else:
        print(colorama.Fore.RED + "Hatalı Seçim Menüye Dönülüyor!")
        time.sleep(2)
        start()





def start():
    os.system("cls")
    print(colorama.Fore.GREEN + filigran)
    print()
    print()
    print(colorama.Fore.YELLOW + """                                Made By: """ + colorama.Fore.RED + "@Musty.9182")
    print()
    print()

    print(colorama.Fore.BLUE + "Lütfen Yapmak İstediğiniz İşlemi Seçin")
    print(colorama.Fore.WHITE + "1 = IP Sorgulama     4 = Hava Durumu")
    print("2 = Webhook Mesaj    5 = Çıkış")
    print("3 = URL Kısaltıcı     ")
    islem = input(colorama.Fore.GREEN)
    if islem == "1":
        ipSorgu()
    elif islem == "2":
        webhookMesaj()
    elif islem == "3":
        urlKisalt()
    elif islem == "4":
        havaDurumu()
    elif islem == "5":
        sys.exit()
    else:
        print(colorama.Fore.RED + "Hatalı Seçim Menüye Dönülüyor!")
        time.sleep(2)
        start()


if __name__ == "__main__":
    os.system("title Multi Tool By Musty")
    defaultSifre = "sa"
    print(colorama.Fore.GREEN + filigran)
    print()
    print(colorama.Fore.BLUE + "Lütfen Şifreyi Giriniz!")
    alinanSifre = input(colorama.Fore.WHITE)
    if alinanSifre == defaultSifre:
        os.system("cls||clear")
        print(colorama.Fore.GREEN + basarili)
        time.sleep(2)
        start()
    else:
        os.system("cls || clear")
        print(colorama.Fore.RED + basarisiz)
        input()


