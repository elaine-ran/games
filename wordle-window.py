from termcolor import colored
import random
import csv

lol=[]
alb=[]
with open("lyrics.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[0] not in lol and row[0]!='Song':
        lol.append(row[0])
        alb.append(row[1])

class Album:
    def __init__(self,title):
        self.title=title
        self.tracklist=[]

class Song:
    def __init__(self,title):
        self.title=title
        self.lyrics=[]

    def assignalbum(self,theindex):
        self.album=albumlist[theindex]
        albumlist[theindex].tracklist.append(self.title)

    def assignlyrics(self):
        with open("lyrics.csv", 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
              if row[0]==self.title:
                self.lyrics.append(row[2])

def createstuff():
    driver_list = []
    for i in range(len(lol)):
        driver_list.append(Song(lol[i]))
    for i, driver in enumerate(driver_list):
        variable_name = lol[i].replace(" ", "_")
        globals()[variable_name] = driver
    return driver_list

def createmorestuff():
    driver_list = []
    for i in range(len(alb)):
        driver_list.append(Album(alb[i]))
    for i, driver in enumerate(driver_list):
        variable_name = alb[i].replace(" ", "_")
        globals()[variable_name] = driver
    return driver_list

def assign():
    for x in range(len(masterlist)):
        masterlist[x].assignalbum(x)
        masterlist[x].assignlyrics()

def cleanup():
    for x in albumlist:
        if '(' in x.title:
            bruh=x.title[:x.title.index('(')-1]
        else:
            bruh=x.title
        for y in morealbums:
            if bruh==y.title:
                y.tracklist+=x.tracklist

def taylorwordle():
    """A game in which you try to guess the Taylor Swift song based on the lyrics!"""
    print('Welcome to Guess the Taylor Swift Song!'+'\n')
    tries=6
    gamewon=False
    secretsong=masterlist[random.randint(0,len(masterlist))]
    if '(' in secretsong.title:
        alttitle=secretsong.title[:secretsong.title.index('(')-1]
    elif '[' in secretsong.title:
        alttitle=secretsong.title[:secretsong.title.index('[')-1]
    else:
        alttitle=secretsong.title
    prev=[]
    while tries > 0 and gamewon==False:
        print('Guess the song using this lyric!'+'\n')
        ummm=colored(secretsong.lyrics[random.randint(0,len(secretsong.lyrics))],'green',attrs=['reverse'])
        print(ummm)
        print('You have '+str(tries)+' tries left!')
        answer=str(input("\n"+"Make a guess: "+"\n"))
        tries-=1
        prev.append(answer)
        if answer==secretsong.title or answer==alttitle:
            gamewon=True
        elif answer != '':
            ugh=answer+" (Taylor’s Version)"
            for x in morealbums:
                if answer in x.tracklist:
                    answeralbum=x
                elif ugh in x.tracklist:
                    answeralbum=x
                else:
                    answeralbum=None
            if answeralbum==None:
                print('Not a valid Taylor Song, maybe try changing the capitalization?')
            else:
                for y in morealbums:
                    if secretsong.title in y.tracklist:
                        secalbum=y
                if answeralbum==secalbum:
                    print("Close... That's the right album but not the right song!")
    if gamewon:
        print('Congratulations! The song was '+secretsong.title+'!')
    elif tries == 0:
        print('Sorry! The song was '+secretsong.title+'! Better luck next time!')

def taylorlyric():
    print('Welcome to Finish the Taylor Swift lyrics!'+'\n')
    rounds=1
    score=0.0
    while rounds < 7:
        print('Round '+str(rounds))
        secretsong=masterlist[random.randint(0,len(masterlist)-1)]
        thetitle=secretsong.title
        if '(' in secretsong.title:
            thetitle=secretsong.title[:secretsong.title.index('(')-1]
        print('What is the next lyric? (Right song name earns 0.5 points)'+'\n')
        randlyric=random.randint(0,len(secretsong.lyrics)-2)
        ummm=colored(secretsong.lyrics[randlyric],'green',attrs=['reverse'])
        print(ummm)
        answer=str(input("\n"+"Finish the lyrics: "+"\n"))
        rounds+=1
        if answer==secretsong.lyrics[randlyric+1]:
            score+=1
        elif answer==thetitle:
            score+=0.5
            print("That's the right song, but the right lyric was: "+secretsong.lyrics[randlyric+1])
        else:
            print('The right answer was: '+"'"+secretsong.lyrics[randlyric+1]+"' from "+colored(secretsong.title,'yellow',attrs=['reverse']))
        print('Your score is '+str(score)+'/6!')
    if rounds==7:
        print('Your final score is '+str(score)+'/6!')

def alltoowell():
    score=0
    fullscore=len(masterlist[1].lyrics)
    keepplaying=True
    while score<fullscore and keepplaying:
        answer=str(input('Enter a lyric: '+"\n"))
        if answer in masterlist[1].lyrics:
            score+=1
        print('So far you have...('+str(score)+'/'+str(fullscore)+')')
        also=str(input('Do you want to keep entering lyrics? ')).lower()
        if also == 'no':
            keepplaying=False
    if not keepplaying:
        print('Your full score is ('+str(score)+'/'+str(fullscore)+')')

albumlist=createmorestuff()
masterlist=createstuff()
TS=Album('Taylor Swift')
F=Album('Fearless')
SN=Album('Speak Now')
R=Album('Red')
NEN=Album('1989')
rep=Album('reputation')
L=Album('Lover')
fo=Album('folklore')
ev=Album('evermore')
M=Album('Midnights')
morealbums=[TS,F,SN,R,NEN,rep,L,fo,ev,M]
assign()
cleanup()
choice=str(input('Enter 1 to play "Guess The Taylor Swift Song"'+'\n'+'Enter 2 to play "Finish the Taylor Swift lyrics"'+'\n'+'Enter 3 to play "Do You Know All the Lyrics to All Too Well"?'+'\n'))
if choice=='1':
    taylorwordle()
elif choice=='2':
    taylorlyric()
elif choice=='3':
    alltoowell()
