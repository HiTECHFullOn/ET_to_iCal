from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import iCal

def time(subject): #div.subject를 Tag로 입력받아 수업 시수와 시작시간을 시간단위로 리턴
    a = str(subject)
    height = int(a[a.find("height: ")+8 : a.find("px; ")])-2
    top = int(a[a.find("top: ")+5 : a.find("px;\">")])
    px = 50
    mins = int((height/px)*60+1)
    start = (int(((top/px)*60)//60), int(int((top/px)*60)%60))
    return [start, mins]

def get_table(url):
    driver = webdriver.Chrome('/Users/cosmosplendor/Desktop/python/chromedriver')
    driver.get(url)
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    td = soup.select('#container > div > div.tablebody > table > tbody > tr > td')
    subject = soup.select('#container > div > div.tablebody > table > tbody > tr > td > div > div.subject')
    username = soup.select_one('#container > aside > div.title > h1').get_text()
    subject_cnt = []        #요일별 과목 개수
    total_cnt = 0           #총 과목 개수
    for i in td:
        cnt = str(i).count('<h3>')
        subject_cnt.append(cnt)
        total_cnt+=cnt
    
    driver.quit()

    dow = ['MO','TU','WE','TH','FR','SA','SU']
    dow_list = []
    for i in range(len(subject_cnt)):
        for j in range(subject_cnt[i]):
            dow_list.append(dow[i])
    
    list = []

    k=0
    for i in subject :
        sub=[]
        sub.append(i.find('h3').get_text())     #과목명
        sub.append(i.find('em').get_text())     #교수명
        sub.append(i.find('span').get_text())   #장소
        sub.append(time(i))                     #시간정보
        sub.append([dow_list[k]])
        k+=1
        list.append(sub)
            
    daily = soup.select('#container > div > div.tablebody > table > tbody > tr > td')


    return [list, username]

