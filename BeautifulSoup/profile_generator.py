#skripta omogućuje nasumično generiranje osobnog profila (ime, prezime, adresa, mob, email), broj generiranih profila određuje korisnik, svi podaci se povlaće s web stranica
#the script randomly generates profiles (name, surname, address, mobile number, email), number of profiles is user defined, all data is from the web


import requests
from bs4 import BeautifulSoup
import re
import random


while True:
    try:
        broj_profila=int(input('Unesite željeni broj profila: '))
    except ValueError:
        continue
    if broj_profila<1:
      continue
    else:
        break  


def ime_funk():
    url = ( "http://osobno-ime.hr/")
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    o= soup.find_all('span', class_='Lemma__LemmaSign')
    imena_list=[]
    for i in o:
        imena_list.append(i.text)
    return imena_list
    
imena=ime_funk()



def prezime_funk():
    url = ( "https://superportal.hr/2023/01/09/ovo-je-200-najcescih-prezimena-u-hrvatskoj-je-li-i-vase-medu-njima/")
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    o= soup.find('div', class_='td_block_wrap tdb_single_content tdi_88 td-pb-border-top td_block_template_1 td-post-content tagdiv-type').find_all('p')

    for i in o[3:4]:
        a=i.text

    a = a.replace("0","")
    a = a.replace("1","")
    a = a.replace("2","")
    a = a.replace("3","")
    a = a.replace("4","")
    a = a.replace("5","")
    a = a.replace("6","")
    a = a.replace("7","")
    a = a.replace("8","")
    a = a.replace("9","")

    prezimena_list = a.split()
    return prezimena_list

prezimena=prezime_funk()




def gradovi_funk():
    url = ( "https://sh.wikipedia.org/wiki/Popis_gradova_u_Hrvatskoj")
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    e= soup.find('div', class_='mw-content-ltr mw-parser-output').table

    o=e.find_all('a')
    gradovi_list=[]
    for i in o:
        gradovi_list.append(i.text)

    gradovi_list=(gradovi_list[::2])
    return gradovi_list

gradovi= gradovi_funk()


url = "https://www.posta.hr/pretrazivanje-ulica-u-gradu-zagrebu/1404?pojam=&tvrsta=zagreb&page=1"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

ulice_list=[]
ulice_list1=[]

def ulice_str1(soup, ulice_list):
    """scrape URLs from one page"""
    b = soup.find('div', class_='content-main').table
    c=b.find_all('td')
    for i in c[::2]:
        ulice_list.append(i.text)
    for i in ulice_list:
        a = 0
        for z in i:
            if z.isdigit() or (z == ")") or (z == "("):
                a = 1
        if(a == 0):
            ulice_list1.append(i)
    return ulice_list1

def ulice_vise_str():
    for i in range(0,500,20):
        url = "https://www.posta.hr/pretrazivanje-ulica-u-gradu-zagrebu/1404?pojam=&tvrsta=zagreb&page=1"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        ulice_list2= ulice_str1(soup, ulice_list)
        url = "https://www.posta.hr/pretrazivanje-ulica-u-gradu-zagrebu/1404?pojam=&tvrsta=zagreb&page="+ str(i)

        return ulice_list2
ulice=ulice_vise_str()

def full_profile():

    for i in range(broj_profila):
        ime = random.choice(imena)
        prezime = random.choice(prezimena)
        grad = random.choice(gradovi)
        ulica=random.choice(ulice)
        broj = random.randint(1,200)
        pozivni=(92,95,98,99,91)
        tel = f'Mob: 0{random.choice(pozivni)}-{random.randint(100, 999)}-{random.randint(1000,9999)}'
        l=('@gmail.com','@hotmail.com','@yahoo.com','@Outlook.com')
        email = 'Email: ' + ime.lower() + prezime.lower() + str(random.choice(l))
        print('-'*30)
        print(f'Ime prezime: {ime} {prezime} \nAdresa: {ulica}{broj}, {grad}- HR\n{tel}\n{email}')
    print('-'*30)
    
full_profile()



