#nathan broadbent
#10/18
import random
win=0
playerHealth= 100
mHealth=100
print("""your lone hero is surrounded by a massive army of trolls.
their decaying green bodies strectch out, melting into the horizon.
your hero unsheathes his sword for the last fight of his life""")
choice=input("fight or run")

while choice =="fight":
    playerDamage= random.randint(5,10)
    print("you deal",playerDamage,"to the trolls killing hundreds of them")
    mHealth-=playerDamage
    if mHealth>0:
        mDamage=random.randint(0,50)
        print("the trolls deal",mDamage,"to you in retaliation")
        playerHealth-=mDamage
    if playerHealth<=0:
        print("you have died")
        break
    elif  mHealth<=0:
        win=1
        print("you have killed the hordes of trolls coming against your hero you win")
        break
    elif playerHealth>=0 and mHealth>=0:
        print("you have ",playerHealth,"health left")
        print('the trolls have health',mHealth, ' left')
        choice=input("fight or run")
        if choice == "fight":
            print("you attack again")
        elif choice=="run":
            break


if choice =="run":
    print("you live to see another day but you are a coward")
if win==0:
    print("game over")
else:
    print("you win")
