while True:
    try:
        cent=float(input("Change owed: "))
    except ValueError:
        continue
    if cent <0:
      continue
    else:
        break            


quarters = round(cent // 0.25)
cent=cent-quarters*0.25
cent = round(cent, 2)

dimes = round(cent // 0.10)
cent=cent-dimes*0.1
cent = round(cent, 2)

nickels = round(cent // 0.05)
cent=cent-nickels*0.05
cent = round(cent, 2)

pennies = cent// 0.01


Sum_coins= quarters + dimes + nickels + pennies
print('q:' + str(quarters))
print('c:' + str(cent))
print('d:' + str(dimes ))
print('c:' + str(cent))
print('n:' + str(nickels))
print('c:' + str(cent))
print('p:' + str(pennies))
print(Sum_coins)


while True:
    try:
        cent=float(input("Change owed: "))
    except ValueError:
        continue
    if cent <0:
      continue
    else:
        break            

cent=int(cent*100)
print(cent)
quarters = cent // 25
cent=cent-quarters*25


dimes = cent // 10
cent=cent-dimes*10


nickels = cent // 5
cent=cent-nickels*5


pennies = cent


Sum_coins= quarters + dimes + nickels + pennies

print('q:' + str(quarters))
print('c:' + str(cent))
print('d:' + str(dimes ))
print('c:' + str(cent))
print('n:' + str(nickels))
print('c:' + str(cent))
print('p:' + str(pennies))
print(Sum_coins)