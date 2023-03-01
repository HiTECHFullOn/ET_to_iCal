import sys
sys.path.append('/Users/cosmosplendor/opt/anaconda3/lib/python3.9/site-packages')
import vobject
from datetime import datetime, timedelta
semester_start = datetime(2023, 3, 2, 0, 0, 0)
semester_end = '20230615T000000'
        
cal1 = vobject.iCalendar()

def cal(name, desc, loca, starttime, mins, dow, username):
    
    global cal1
    vevent = cal1.add('vevent')
    vevent.add('summary').value = name
    vevent.add('description').value = desc
    
    if 'TH' in dow:
        dtstart = semester_start + timedelta(hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'FR' in dow:
        dtstart = semester_start + timedelta(days=1, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'SA' in dow:
        dtstart = semester_start + timedelta(days=2, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'SU' in dow:
        dtstart = semester_start + timedelta(days=3, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'MO' in dow:
        dtstart = semester_start + timedelta(days=4, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'TU' in dow:
        dtstart = semester_start + timedelta(days=5, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
    elif 'WE' in dow:
        dtstart = semester_start + timedelta(days=6, hours=starttime[0], minutes=starttime[1])
        dtend = dtstart + timedelta(minutes=mins)
        
    vevent.add('dtstart').value = dtstart
    vevent.add('dtend').value = dtend
    vevent.add('dtstamp').value = semester_start
    vevent.add('location').value = loca
    vevent.add('rrule').value = 'FREQ=WEEKLY;INTERVAL=1;UNTIL='+semester_end+';BYDAY='+','.join(dow)

    with open(username+'.ics','wb') as f:
        f.write(cal1.serialize().encode('utf-8'))
    
