import random
from colorama import init, Fore, Back, Style

init()

credit = 1000

iphoneCredit = 10

#if prize = 0 (iphone), the user wins
win = 0
lose = 0

count = 0

prizeAmount = 15000


# 0=iphone
prizeList = [0,1,2,3,4,5,6,7,8,9,10]

prizeScale = [0.027,1.83,2.49,3.6,4.8,6.2,8.57,10.88,16.2,25.35,20.253]

prizeAmount = [0,0,0,0,0,0,0,0,0,0,0]

for idx in range(0,len(prizeScale)):
    prizeAmount[idx] = (prizeScale[idx]*prizeAmount)


prizeRewards = [0,150,100,50,20,10,0,-1,-3,-5,-10]

prizeDic = {
    "0":0,
    "1":150,
    "2":100,
    "3":50,
    "4":20,
    "5":10,
    "6":5,
    "7":3,
    "8":2,
    "9":1,
    "10":0,
}

prizeCountDic = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "10":0,
}

#print prize
def printPrizeMessage(prize):

    prizeMessage = ""

    prizeint = int(prize)

    if (prizeint == 0):
        prizeMessage = "You have won the Iphone! Congratulations"

    elif (prizeint == 1):
        prizeMessage = f"{Fore.MAGENTA}You have won the 1st prize, 150 credits! :){Style.RESET_ALL}"

    elif (prizeint == 2):
        prizeMessage = f"{Fore.BLUE}You have won the 2nd prize, 100 credits! :){Style.RESET_ALL}"

    elif (prizeint == 3):
        prizeMessage = f"{Fore.CYAN}You have won the 3rd prize, 50 credits! :){Style.RESET_ALL}"

    elif (prizeint == 4):
        prizeMessage = f"{Fore.WHITE}You have won the 4th prize, 20 credits! :){Style.RESET_ALL}"

    elif (prizeint == 5):
        prizeMessage = "You have won the 5th prize, 10 credits! :|"

    elif (prizeint == 6):
        prizeMessage = "You have won the 6th prize, 5 credits! :("

    elif (prizeint == 7):
        prizeMessage = "You have won the 6th prize, 3 credits! :("

    elif (prizeint == 8):
        prizeMessage = "You have won the 6th prize, 2 credits! :("

    elif (prizeint == 9):
        prizeMessage = "You have won the 6th prize, 1 credits! :("

    elif (prizeint == 10):
        prizeMessage = "You have won the 6th prize, 0 credits! :("


    print("\n" + prizeMessage)

def checkCredit(credit):
    intCredit = int(credit)

    if (intCredit < 0):
        return False
    else:
        return True

def printStat():
    for x in range(11):
        prizeCount = prizeCountDic[str(x)]
        prob = round((prizeCount / count) * 100, 2)
        print(str(x) + ": " + str(prizeCount) + " (" + str(prob) + "%)")

while (win != 1 and lose != 1 and credit > 0):
    print("Your credit: " + str(credit))

    print("Enter the number you wish to draw")

    num = int(input())

    for x in range(num):

        #count
        count += 1

        prize = (random.choices(prizeList, weights=(0.027,1.83,2.49,3.6,4.8,6.2,8.57,10.88,16.2,25.35,20.253), k=1))

        prizeCountDic[str(prize[0])] += 1

        #print the prize
        printPrizeMessage(prize[0])

        if (prize[0] == 0):
            win = 1
            break

        credit -= iphoneCredit

        credit += prizeDic[str(prize[0])]

        if (not checkCredit(credit)):
            lose = 1
            break


if (credit < 0 or lose == 1):
    print("Total tries: " + str(count))
    print("You have lost, don't gamble thx!!!")
    print("Statistics:")
    printStat()


elif (win == 1):
    print("Well done, you are lucky!")
    print("Total tries: " + str(count))
    print("Statistics:")
    printStat()
