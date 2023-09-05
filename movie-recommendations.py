#movie recommender
from termcolor import colored
from urllib.request import Request, urlopen

def slicemiddle(s,t1,t2,yes):
    index1=s.index(t1)
    index2=index1+len(t1)
    index3=s.index(t2)
    index4=index3+len(t2)
    if yes:
        return s[index2:index3], index4
    return s[index2:index3]

def askuser():
    print(colored('Movie Recommendation Generator!','green'))
    answer=str(input('Movie: '))
    return answer.lower()

def openletterboxd(movie,yes):
    movie=movie.replace(' ','-')
    req = Request(
        url='https://letterboxd.com/film/'+movie+'/',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page = urlopen(req).read()
    html = page.decode("utf-8")
    title_index = html.find("<title>")
    start_index=title_index+len('<title>')
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    if yes:
        return slicemiddle(title,'&lrm;',' •',False),html
    return slicemiddle(title,'&lrm;',' •',False)

def openletterboxdsimilar(movie):
    movie=movie.replace(' ','-')
    req = Request(
        url='https://letterboxd.com/film/'+movie+'/similar/',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page = urlopen(req).read()
    html = page.decode("utf-8")
    return html

def findsimilar(html):
    alist=[]
    i=0
    while i<5:
        filmname, index4=slicemiddle(html,'data-film-slug="/film/','/" data-poster-url=',True)
        alist.append(filmname)
        html=html[index4:]
        i+=1
    return alist

def mainbody(movielist,og):
    returnlist=[]
    for movie in movielist:
        title=openletterboxd(movie,False)
        returnlist.append(title)
    print('Films similar to '+og+':'+'\n')
    for thing in range(len(returnlist)):
        print(str(thing+1)+'. '+returnlist[thing])
    return returnlist

def learnmore(alist):
    uh=['1','2','3','4','5']
    listig=[1,2,3,4,5]
    answer=str(input('If you would like to know more about one of the suggestions, enter in the corresponding number (if not, press any other key): '))
    if answer in uh:
        answer=int(answer)
        num=listig.index(answer)
        um,second=openletterboxd(alist[num],True)
        print('Brief Description of '+um+': '+'\n')
        astring=second[second.index('data-truncate="450"'):second.index('data-truncate="450"')+1000]
        des=slicemiddle(astring,'<p>','</p>',False)
        print(des)
    else:
        print('Thanks for using Movie Recommendation Generator!')

theanswer=askuser()
themovie=openletterboxd(theanswer,False)
thesim=findsimilar(openletterboxdsimilar(theanswer))
themain=mainbody(thesim,themovie)
learnmore(thesim)


							#<div class="truncate" data-truncate="450">
								#<p>On a fall night in 2003, Harvard undergrad and computer programming genius Mark Zuckerberg sits down at his computer and heatedly begins working on a new idea. In a fury of blogging and programming, what begins in his dorm room as a small site among friends soon becomes a global social network and a revolution in communication. A mere six years and 500 million friends later, Mark Zuckerberg is the youngest billionaire in history... but for this entrepreneur, success leads to both personal and legal complications.</p>
							#</div>

					#</div>
