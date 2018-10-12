#nathan broadbent
#10/18
import random
##loops=0
##while True:
##    print("I have looped",loops,"times")
##    loops+=1
##    if loops>=2000:
##        break


##count=0
##
##while count >= 0:
##    count+=1
##    if count>100:
##        break
##    if  count==5 or count==25 or count==50 or count==75:
##        continue
##    print(count)

print("""your lone hero is surrounded by a massive army of trolls.
their decaying green bodies strectch out, melting into the horizon.
your hero unsheathes his sword for the last fight of his life""")

health=100
trolls=0
damage=3


while health > 0:
    damage=random.randint(5,10)
    trolls+=1
    health-=damage
    print("your hero swings and defeats an evil troll, but takes", damage,"damage points.\n")

print("Your hero fought valiantly and defeated", trolls,"trolls.")
print("but alas, your hero is no more.")
