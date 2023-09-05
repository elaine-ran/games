class Driver:
    """Instance Attributes:
    1. name: [str] the name of the driver
    2. wins: [list] list of race wins, can be empty
    3. poles: [list] list of poles, can be empty
    4. fastestlaps: [list] list of fastest laps, can be empty
    5. podiums: [list] list of podiums, can be empty
    6. points: [int] number of points the driver has scored this season
    7. trackpoints: [dictionary] a dictionary in the format {'Race': [int] points earned}
    8. championshipleader: [bool] True or False
    """
    def __init__(self,name):
        self.name=name
        self.wins=[]
        self.poles=[]
        self.fastestlaps=[]
        self.podiums=[]
        self.points=0
        self.trackpoints={}
        self.championshipposition=None
        self.championshipleader=False

    def updatetrackpoints(self,Circuit,points,FL=False,pole=False):
        """updates the driver's trackpoints dictionary and updates the list of wins,
        poles, FLs and podiums accordingly. Also udpates the lists of the Race.
        Preconditions:
        - Race is a Race object.
        - points is an int that represents how many points the driver earned
        - FL, automatically set to False, only enter in True if the driver had the
            fastest lap of that race
        - pole, automatically set to False, only enter in True if the driver was the
            pole sitter of that race
        """
        self.trackpoints[Circuit.name]=points
        self.points+=points
        if points >= 25:
            self.wins.append(Circuit.name)
            Circuit.winner=self
            self.podiums.append(Circuit.name)
            Circuit.podium['Winner']=self
        if FL == True:
            self.fastestlaps.append(Circuitname)
            Circuit.fastestlap=self
        if pole == True:
            self.poles.append(Circuit.name)
            Circuit.polesitter=self
        if points in [15,16]:
            self.podiums.append(Circuit.name)
            Circuit.podium['Third']=self
        if points in [18,19]:
            self.podiums.append(Circuit.name)
            Circuit.podium['Second']=self

    def updatesprinttrackpoints(self,Race,points):
        self.points+=points
        self.trackpoints[Race.name+' Sprint']=points
        if points == 8:
            Race.sprintwinner=self

    def setchampionshipposition(self,number):
        self.championshipposition=number
        self.championshipleader=False
        if number==1:
            self.championshipleader=True
        if number==0:
            self.championshipposition=None

    def stats(self):
        if len(self.wins)==0:
            yeswin=None
        else:
            yeswin=str(self.wins)
        if len(self.poles)==0:
            yespole=None
        else:
            yespole=str(self.poles)
        if len(self.fastestlaps)==0:
            yesfl=None
        else:
            yesfl=str(self.fastestlaps)
        if len(self.podiums)==0:
            yespod=None
        else:
            yespod=str(self.podiums)
        if self.championshipleader == True:
            print(self.name+" is currently the championship leader! "+"\n"+self.name+"'s 2023 season: "+"\n"+"Points: "+str(self.points)+" ("+str(self.championshipposition)
            +")."+"\n"+"Wins: "+str(yeswin)+"." +"\n"+ "Poles: "
            +str(yespole)+"."+"\n"+ "Fastest Laps: "+str(yesfl)+"."+"\n"+ "Podiums: "+str(yespod))
        else:
            print (self.name+"'s 2023 season: "+"\n"+"Points: "+str(self.points)+" ("+str(self.championshipposition)
            +")."+"\n"+"Wins: "+str(yeswin)+"." +"\n"+ "Poles: "
            +str(yespole)+"."+"\n"+ "Fastest Laps: "+str(yesfl)+"."+"\n"+ "Podiums: "+str(yespod))
        answer=str(input("See the track points dictionary? Y/N "))
        if answer in ['Yes','Y','YES','y','yes']:
            for x in self.trackpoints:
                print(x+": "+str(self.trackpoints[x]))


class Race:
    """Instance Attributes:
    1. name: [str] the name of the circuit/country (whichever one is most popular))
    2. winner: [driver object] the corresponding winning Driver
    3. polesitter: [driver object] the corresponding pole sitter Driver
    4. fastestlap: [driver object] the corresponding Driver with the fastest lap
    5. laptime: [float] number of seconds of the fastest lap
    6. qualitime: [float] number of seconds of the fastest qualification time
    7. podium: [dictionary] keys are (strings) positions, values are driver objects (e.g:
        {'Winner': Driver, 'Second': Driver etc.})
    """
    def __init__(self,name):
        self.name=name
        self.winner=None
        self.polesitter=None
        self.fastestlap=None
        self.podium={}
        self.laptime = 0.0
        self.qualitime= 0.0
        self.pointscorers={}
        for x in ['1','2','3','4','5','6','7','8','9','10']:
            self.pointscorers[x]=0

    def settimes(self,laptime,qualitime):
        self.laptime=laptime
        self.qualitime=qualitime

    def stats(self):
        if self.name=='Imola':
            print('The Imola Grand Prix was canceled due to flooding in the area.')
            return None
        if self.name in sprintlist:
            print (self.name+" Sprint Race Stats: "+"\n"+"Winner: "+self.sprintwinner.name+".")
        print (self.name+" Race Stats:"+"\n"+"Winner: "+self.winner.name+"."+"\n"+"Pole Sitter: "
        +self.polesitter.name+' ('+self.qualitime+')'+"."+"\n"+"Fastest Lap: "+self.fastestlap.name+' ('+self.laptime+')'+
        "."+"\n"+"Podium: "+str([self.podium['Winner'].name,self.podium['Second'].name,self.podium['Third'].name]))
        answer=str(input("See all points scorers? Y/N "))
        if answer in ['Yes','Y','YES','y','yes']:
            for k in range(len(gps)):
                if gps[k]==self.name:
                    for x in self.pointscorers:
                        for y in range(len(driverlist)):
                            if driverlist[y].name==self.pointscorers[x]:
                                print(x+". "+self.pointscorers[x]+' - '+str(emptylist[k][y]))

def createdrivers():
    driver_list = []
    for i in range(len(driverlist)):
        driver_list.append(Driver(driverlist[i]))
    for i, driver in enumerate(driver_list):
        hold=driverlist[i].index(' ')
        variable_name = driverlist[i][hold+1:hold+4].upper()
        globals()[variable_name] = driver
    return driver_list

def createraces():
    race_list = []
    for i in range(len(gps)):
        race_list.append(Race(gps[i]))
    for i, race in enumerate(race_list):
        variable_name = gps[i].replace(" ", "_")
        globals()[variable_name] = race
    return race_list

def createresultlists():
    race_list_vars=[]
    for name in gps:
        race_name = name.lower().replace(" ", "") + "list"
        globals()[race_name] = []
        race_list_vars.append(globals()[race_name])
    return race_list_vars

def sprintraceudpdate(Race):
    if Race.name in sprintlist:
        raceindex=sprintlist.index(Race.name)
        bruh=sprintresultlist[raceindex]
        for x in range(len(driverlist)):
            driverlist[x].updatesprinttrackpoints(Race,bruh[x])
    else:
        return None

def oneraceupdates(Race):
    """Calls the class update function for one particular race.
    Preconditions: Race is a race object.
    """
    sprintraceudpdate(Race)
    raceindex=gps.index(Race.name)
    bruh=resultlists[raceindex]
    for x in range(len(driverlist)):
        driverlist[x].updatetrackpoints(Race,bruh[x],False,False)

def allflsupdate():
    """Updates the fastest lap lists for everything"""
    for x in range(len(racelist)):
        for y in driverlist:
            if y.name==fls[x]:
                y.fastestlaps.append(racelist[x].name)
                racelist[x].fastestlap=y

def allpolesupdate():
    """Updates the pole lists for everything"""
    for x in range(len(racelist)):
        for y in driverlist:
            if y.name==poles[x]:
                y.poles.append(racelist[x].name)
                racelist[x].polesitter=y

def alltimesupdate():
    for x in range(len(racelist)):
        racelist[x].settimes(laptimes[x],qualitimes[x])

def createnewlist():
    copylist=[]
    for x in driverlist:
        copylist.append(x)
    return copylist

def createanotherlist():
    copylist=createresultlists()
    for k in range(len(copylist)):
        for x in resultlists[k]:
             copylist[k].append(x)
    return copylist

def sortchampionship():
    i=1
    while i < 19:
        maximum=0
        for x in copylist:
            if x.points>maximum:
                maximum=x.points
                championshipleader=x
            if x.points==0:
                x.setchampionshipposition(0)
                copylist.remove(x)
        copylist.remove(championshipleader)
        championshipleader.setchampionshipposition(i)
        i+=1

def setpointsforrace(Race):
    raceindex=gps.index(Race.name)
    bruh=resultlists[raceindex]
    newlist=createnewlist()
    i=1
    while i<11:
        hold=0
        for x in range(len(newlist)):
            if bruh[x]>hold:
                hold=bruh[x]
                plswork=newlist[x]
        if hold in bruh:
            bruh.remove(hold)
        if plswork in newlist:
            newlist.remove(plswork)
            Race.pointscorers[str(i)]=plswork.name
        i+=1

def allraceupdates():
    for x in range(len(racelist)):
        if fls[x] != '':
            oneraceupdates(racelist[x])
            setpointsforrace(racelist[x])

def whatwouldyoulike():
    answer=str(input("Whose season results would you like to see? "+"\n"+"Press return for race stats. "+"\n"))
    if answer=='':
        twoanswer=str(input("Which race results would you like to see? "))
        for y in racelist:
            if y.name==twoanswer:
                return y.stats()
    for x in driverlist:
        if x.name==answer:
            return x.stats()

sprintresultlist=[[],[],[],[],[],[]]
driverlist=['Max Verstappen','Sergio Perez','Charles Leclerc','Carlos Sainz','George Russell','Lewis Hamilton','Lando Norris',
'Oscar Piastri','Pierre Gasly','Esteban Ocon','Valtteri Bottas','Guanyu Zhou','Lance Stroll','Fernando Alonso',
'Kevin Magnussen','Nico Hulkenberg','Yuki Tsunoda','Logan Sargeant','Alex Albon','Nyck deVries']
gps=['Bahrain','Jeddah','Australia','Baku','Miami','Imola','Monaco','Spain',
'Canada','Austria','Silverstone','Hungary','Spa','Zandvoort','Monza',
'Singapore','Suzuka','Qatar','COTA','Mexico','Interlagos','Las Vegas','Abu Dhabi']
fls=['Guanyu Zhou','Max Verstappen','Sergio Perez','George Russell','Max Verstappen','','Lewis Hamilton','Max Verstappen','Sergio Perez','Max Verstappen','','','','',
'','','','','','','','','','']
poles=['Max Verstappen','Sergio Perez','Max Verstappen','Charles Leclerc','Sergio Perez','','Max Verstappen','Max Verstappen','Max Verstappen','Max Verstappen','','',
'','','','','','','','','','','','']
laptimes=['1:33.996','1:31.906','1:20.235','1.43.370','1:29.708','0.00.000','1:15.650',
'1:16.330','1:14.481','1:07.012','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000',
'0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000']
qualitimes=['1:29.708','1:28.265','1:16.732','1.40.203','1:26.841','0.00.000','1:11.365',
'1:12.272','1:25.858','1.04.391','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000',
'0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000','0.00.000']
sprintlist=['Baku','Austria','Spa','Qatar','COTA','Interlagos']
driverlist=createdrivers()
racelist=createraces()
resultlists=createresultlists()
resultlists[0]=[25,18,0,12,6,10,0,0,2,0,4,0,8,15,0,0,0,0,1,0]
resultlists[1]=[19,25,6,8,12,10,0,0,2,4,0,0,0,15,1,0,0,0,0,0]
resultlists[2]=[25,11,0,0,0,18,8,4,0,0,0,2,12,15,0,6,1,0,0,0]
resultlists[3]=[18,25,15,10,5,8,2,0,0,0,0,0,6,12,0,0,1,0,0,0]
resultlists[4]=[26,18,6,10,12,8,0,0,4,2,0,0,0,15,1,0,0,0,0,0]
resultlists[6]=[25,0,8,4,10,13,2,1,6,15,0,0,0,18,0,0,0,0,0,0]
resultlists[7]=[26,12,0,10,15,18,0,0,1,4,0,2,8,6,0,0,0,0,0,0]
resultlists[8]=[25,9,12,10,0,15,0,0,0,4,1,0,2,18,0,0,0,0,6,0]
resultlists[9]=[26,15,18,12,4,6,10,0,2,0,0,0,1,8,0,0,0,0,0,0]
sprintresultlist[0]=[6,8,7,4,5,2,0,0,0,0,0,0,1,3,0,0,0,0,0,0,0]
sprintresultlist[1]=[8,7,0,6,1,0,0,0,0,2,0,0,5,4,0,3,0,0,0,0,0]
emptylist=createanotherlist()
allraceupdates()
allflsupdate()
allpolesupdate()
alltimesupdate()
copylist=createnewlist()
sortchampionship()
whatwouldyoulike()
