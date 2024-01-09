import requests
from bs4 import BeautifulSoup

url1 = ( "https://www.tportal.hr/horoskop/")

def horoskop(odabir_perioda,odabir_znaka):
    url2 = ( f"{d1[odabir_perioda]}/{d[odabir_znaka]}" )
    url= url1 + url2
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    o= soup.find("div", {"class":"col-start-1 col-span-12 flex flex-col gap-[18px] text-[calc(1rem*20/16)] leading-[27px] font-medium lg:col-span-8 xlg:col-start-4"})
    
    return o.get_text().strip()
    

    
    
if __name__ == "__main__": 
    soup = BeautifulSoup(requests.get(url1).content, "html.parser")
    znak=soup.find_all('li', class_='horoscope__sign_card')
    
    
    znak_list=[]
    for i  in znak:
        znak_list.append(i.p.text.strip())
    

    znak_list_index = []
    for i in znak_list:
        znak_list_index.append(znak_list.index(i))
    
    d = dict(zip(znak_list_index, znak_list))

    print('Horoskopski znakovi:', d, sep='\n')
    odabir_znaka=int(input('\n'+'Izaberi broj od 0-11 za željeni horoskopski znak: '))

    url3=url1+f"dnevni/{d[odabir_znaka]}" 

    soup = BeautifulSoup(requests.get(url3).content, "html.parser")
    period1=soup.find('ul', class_='flex gap-x-[21px] justify-center lg:flex-col lg:justify-start lg:gap-y-[18px]')
    period2=period1.find_all('li')

    period_list=[]
    for i in period2:
       period_list.append(i.text.strip().lower())
    

    d1 = dict(zip(znak_list_index, period_list))

    print('\n'+'Vremenski period:', d1, sep='\n')
    odabir_perioda=int(input('\n'+'Izaberi broj od 0-2 za željeni period: '))
    d1.update([(2, 'mjesecni')])
    
   
    print(horoskop(odabir_perioda, odabir_znaka))
