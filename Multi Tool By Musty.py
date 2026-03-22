import requests
import os
import colorama
import json
import time
import sys


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
WEBHOOK_URL = ""  # ← Kendi Webhook Url'ni Yaz

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





def start():
    os.system("cls")
    print(colorama.Fore.GREEN + filigran)
    print()
    print()
    print(colorama.Fore.YELLOW + """                                Made By: """ + colorama.Fore.RED + "@Musty.9182")
    print()
    print()

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


if __name__ == "__main__":
    os.system("title Multi Tool By Musty")
    start()

