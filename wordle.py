from termcolor import colored
import random
# opening the file in read mode
my_file = open("sgb-words.txt", "r")

# reading the file
data = my_file.read()

data_into_list = data.split("\n")
my_file.close()
secretword=data_into_list[random.randint(0,len(data_into_list))].upper()
rules="Enter a five letter word for each guess."+"\n"+"For example, pretend the secret word was 'HELPS', If a letter in your guess is in the secret word, and is in the right position, it will show up with a green highlight"+"\n"+colored('H','green',attrs=['reverse'])+'APPY'+"\n"+"If a letter in your guess is in the word, but is not in the right position, it will show up in yellow"+"\n"+colored('L','yellow',attrs=['reverse'])+'UCKY'+"\n"+"If a letter in your guess is not in the word at all, it will show up in red"+"\n"+colored('TRAIN','red',attrs=['reverse'])+"\n"+"Good Luck!"
def wordle():
    print('WORDLE')
    dumb=str(input('Do you want a rules refresher?'+"\n"))
    if dumb in ['Yes','YES','y','Y','yes']:
        print(rules)
    tries=6
    gamewon=False
    secretword=data_into_list[random.randint(0,len(data_into_list))].upper()
    prev=[]
    while tries > 0 and gamewon==False:
        answervalid=False
        print('You have '+str(tries)+' tries left!')
        answer=str(input("Make a guess: "+"\n")).upper()
        while answervalid==False:
            if answer.lower() in data_into_list and len(answer)==5 and answer not in prev:
                answervalid=True
            elif len(answer)!=5:
                print('Must be a five letter word, try again!')
                answer=str(input("Make a guess: "+"\n")).upper()
            elif answer in prev:
                print('You already guessed that, try again!')
                answer=str(input("Make a guess: "+"\n")).upper()
            else:
                print('Not a real word, try again!')
                answer=str(input("Make a guess: "+"\n")).upper()
        greenlist=[]
        yellowlist=[]
        yellowlist2=[]
        graylist=[]
        printedresult=''
        for x in range(len(answer)):
            if answer[x]==secretword[x]:
                greenlist.append(x)
            elif answer[x] in secretword:
                if answer[x] not in yellowlist2:
                    yellowlist.append(x)
                    yellowlist2.append(answer[x])
                else:
                    graylist.append(x)
            else:
                graylist.append(x)
        for x in range(len(answer)):
            if x in greenlist:
                printedresult+=colored(answer[x],'green',attrs=['reverse'])
            if x in yellowlist:
                printedresult+=colored(answer[x],'yellow',attrs=['reverse'])
            if x in graylist:
                if x not in yellowlist:
                    printedresult+=colored(answer[x],'red',attrs=['reverse'])
        print(printedresult)
        tries-=1
        prev.append(answer)
        if answer==secretword:
            gamewon=True
    if gamewon:
        print('Congratulations! The word was '+answer+'!')
    if tries == 0:
        print('Sorry! The word was '+secretword+'! Better luck next time!')
#wordle()
