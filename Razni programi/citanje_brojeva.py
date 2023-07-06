string_stotice = ['sto', 'dvjesto','tristo','cetristo','petsto','sesto','sedamsto','osamsto', 'devetsto']
string_desetice = ['deset','dvadeset','trideset','cetrdeset','pedeset','sezdeset','sedamdeset','osamdeset','devedeset'] 
string_11_19 = ['jedanaest','dvanaest','trinaest','cetrnaest','petnaest','sestnaest','sedamnaest','osamnaest','devetnaest']
string_jedinice = ['nula','jedan', 'dva', 'tri', 'cetiri', 'pet', 'sest', 'sedam', 'osam', 'devet']

while True:
    try:
        broj = int(input('Upisi troznamenkasti broj ili manji:'))
    except ValueError:
        continue
    if broj <-999:
      continue
    else:
        break   

brojString=[]
if broj <0:
     brojString.append('minus')
     
broj = abs(broj)
stotica = int(broj / 100)

if stotica != 0:
    brojString.append(string_stotice[stotica-1])
    broj = broj - stotica*100

if broj >= 11 and broj <= 19:
    brojString.append(string_11_19[broj-11])

else: 
    desetica = int(broj/10)

    if desetica != 0:
        brojString.append(string_desetice[desetica-1])
        broj = broj - desetica*10
    if (stotica and broj != 0) or (desetica and broj != 0) or (not stotica and not desetica and broj >= 0 and broj <= 9):
        brojString.append(string_jedinice[broj])


print(' '.join(brojString))  
