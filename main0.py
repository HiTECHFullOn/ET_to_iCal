import everytimport as et
import iCal

url = 'https://everytime.kr/@BjAD7EkU6H8B6AivwRWB'
data = et.get_table(url)
list = data[0]
username = data[1]
ID = url[21:]
#ID와 username 중 무엇을 iCal에 반환해야 할지는 고민중... 일단 임시로 ID
for lesson in list:
    iCal.cal(lesson[0], lesson[1], lesson[2], lesson[3][0], lesson[3][1], lesson[4], ID)
if list == []:
    print("공개되지 않은 시간표거나 잘못된 링크입니다.")

