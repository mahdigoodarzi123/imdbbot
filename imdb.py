from typing import Text
from selenium import webdriver
from time import  sleep
import os



path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , 'chromedriver.exe')



browser = webdriver.Chrome()


birthday_list = []


def birthday():
    browser.get('https://www.imdb.com/?ref_=nv_home')
    browser.find_element_by_xpath('//*[@id="__next"]/main/div/div[4]/div[8]/div/section[2]/div/a').click()
    xpath1 = '//*[@id="main"]/div/div[3]/'
    xpath3 = '/div[2]/h3'
    for i in range(1,21):
        pone = 'div['
        ptwo = str(i)
        pthree = ']'
        xpath2 = pone + ptwo + pthree
        xpath = xpath1 + xpath2 + xpath3
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(2)




def top_movies():
    browser.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/'
    xpath3 = '/td[2]'
    for i in range(1,251):
        pone = "tr["
        ptwo = str(i)
        pthree = "]"
        xpath2 = pone + ptwo +pthree
        xpath = xpath1 +xpath2 + xpath3
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(1)





def top_series():
    browser.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')


    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/'
    for i in range(1,251):
        pone = 'tr['
        ptwo = str(i)
        pthree = ']'
        xpath2 = pone + ptwo + pthree
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(1)




def popular_movies():
    browser.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm')
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/'
    for i in range(1,21):
        pone = 'tr['
        ptwo = str(i)
        pthree = ']'
        xpath2 = pone + ptwo + pthree
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(2)
    




def popular_tv():
    browser.get('https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv')
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['
    for i in range(1,21):
        pone = str(i)
        ptwo = ']'
        xpath2 = pone + ptwo
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(2)


def popular_actors():
    browser.get('https://www.imdb.com/search/name/?match_all=true&ref_=nv_cel_m')
    xpath1 = '//*[@id="main"]/div/div[3]/div['
    for i in range(1,41):
        pone = str(i)
        ptwo = ']/div[2]/h3'
        xpath2 = pone + ptwo 
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        print(name.text)
        sleep(2)



def box_office():
    browser.get('https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm')
    xpath1 = '//*[@id="boxoffice"]/table/tbody/tr['
    for i in range(1,8):
        pone = str(i)
        ptwo = ']'
        xpath2 = pone + ptwo
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        print(pone + ": "  + name.text)
        sleep(2)







imdb250topm = []
def imdb250movies():
    browser.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['
    for i in range(1,251):
        pone = str(i)
        ptwo = ']/td[2]/a'
        xpath2 = pone + ptwo
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        imdb250topm.append(name.text)





def searchmovie():
    thing = input("what do you wanna search? ")    
    #serching part
    url1 = 'https://www.imdb.com/find?q='
    url2 = thing
    url3 = '&ref_=nv_sr_sm'
    url = url1 + url2 + url3 
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
    
    therealname = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1').text

    
    #checking if that movie is in 250 top or not
    imdb250movies()
    if therealname in imdb250topm :
        value = True
    else :
        value = False
    #till here
     
    browser.get(url) 
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
      
    rate = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
    print("rate: " + rate.text)
    year = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/span')
    time = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[3]')
    Summary = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[2]')
    print("year: " + year.text + "      time: " + time.text )
    print("summary is: " +Summary.text)
    
    if value == True :
        xpath1 = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div['
        for i in range(1,8):
            pone = str(i)
            ptwo = ']'
            xpath2 = pone + ptwo
            xpath = xpath1 + xpath2
            actors = browser.find_element_by_xpath(xpath)
            print('actors: ' + actors.text)
            sleep(1)
        topchecker = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div')
        print(topchecker.text)


    elif value == False :
        xpathone = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[3]/div[2]/div[2]/div['
        for j in range(1,8):
            p1 = str(j)
            p2 = ']'
            xpathtwo = p1 + p2
            wxpath = xpathone + xpathtwo
            actors2 = browser.find_element_by_xpath(wxpath)
            print("actors: " + actors2.text)
            sleep(1)












imdb250series = []
def imdb250seriestop():
    browser.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
    
    xpath1 = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['
    for i in range(1,251):
        pone = str(i)
        ptwo = ']/td[2]/a'
        xpath2 = pone + ptwo
        xpath = xpath1 + xpath2
        name = browser.find_element_by_xpath(xpath)
        imdb250series.append(name.text)








def searchseries():
    
    url1 = 'https://www.imdb.com/find?q='
    thing = input('what do you wanna search: ')
    url2 = '&ref_=nv_sr_sm'
    url = url1 + thing + url2
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
    
    therealname = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1').text
    
    imdb250seriestop()
    if therealname in imdb250series :
        value = True
    else:
        value = False

    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[1]').click()
    year = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span')
    time = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[4]')
    Summary = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]')
    print("year: " + year.text + "      time: " + time.text )
    print("summary is: " +Summary.text)
    rate = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]')
    print("rate: " + rate.text)



    if value == True :
        xpath1 = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[5]/div[2]/div[2]/div['
        for i in range(1,8):
            pone = str(i)
            ptwo = ']'
            xpath2 = pone + ptwo
            xpath = xpath1 + xpath2
            actors = browser.find_element_by_xpath(xpath)
            print('actors: ' + actors.text)
            sleep(1)
        topchecker = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div')
        print(topchecker.text)


# i didnt find any series with no reward for false value!!!!!
    if value == False :
        xpath1 = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[5]/div[2]/div[2]/div['
        for i in range(1,8):
            pone = str(i)
            ptwo = ']'
            xpath2 = pone + ptwo
            xpath = xpath1 + xpath2
            actors = browser.find_element_by_xpath(xpath)
            print('actors: ' + actors.text)
            sleep(1)
        topchecker = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div')
        print(topchecker.text)












while(True):
    sleep(4)
    print("help command: todays birthday=birthday , top rated moveis=top movies , top rated series= top series , searching movies=search movies , searching series=search series ,  box office=box office , popular actors=popular actors , popular movies=popular movies , popular series=popular series , exit=exit")
    command = input("your command: ")
    if command == "birthday" :
        birthday()
    elif command == "top movies":
        top_movies()
    elif command == "top series":
        top_series()
    elif command == "search movies":
        searchmovie()
    elif command == "search series":
        searchseries()
    elif command == "box office":
        box_office()
    elif command == "popular actors":
        popular_actors()
    elif command == "popular movies":
        popular_movies()
    elif command == "popular series":
        popular_tv()
    elif command == "exit":
        break
    sleep(4)