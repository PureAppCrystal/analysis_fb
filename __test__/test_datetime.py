# 파이썬에서 날짜와 시간을 다루는 방법
import datetime


now = datetime.datetime.now()
print(now)


# string formating
nowdate = now.strftime('%Y-%m-%d')
nowtime = now.strftime('%H-%M-%S')
print(nowdate)
print(nowtime)

# string -> datetime
str_date_time = '2017-10-16 12:23:40'
datetime1 = datetime.datetime.strptime(str_date_time, '%Y-%m-%d %H:%M:%S')
print(type(datetime1))
print(datetime1)

# 날짜나 시간 변경
datetime2 = datetime1.replace(day=20)
print(datetime1)
print(datetime2)

# 날짜만 관리하기 위한 datetime.date
d = datetime.date(2015, 1, 1)
print(type(d))
# 시간만 관리하기 위한 datetime.time
t = datetime.time(6, 0, 0)
print(type(t))

print(d, t)

# date와 time을 합치기
dt = datetime.datetime.combine(d, t)
print(type(dt))
print(dt)

# datetime 에서 년 월 일 시 분 초 각각 접근하기
dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday()) 
print(dt.hour)
print(dt.minute)
print(dt.second)

t = dt.timetuple()
print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

# 날짜, 시간 더하기
# 10초 더하기 datetime.timedelta(seconds=+1)
# 10분 더하기 datetime.timedelta(minutes=+1)
# 1시간 더하기 datetime.timedelta(hours=+1)
# 1일 더하기 datetime.timedelta(dates=+1)
# 1주 더하기 datetime.timedelta(weeks=+1)
# 1달 더하기 datetime.timedelta(weeks=+1)

now = datetime.datetime.now()
print("-----now-----")
print(now)
print("-------------")

# now1 = now + datetime.timedelta(month=1)
# print(now1)
now1 = now + datetime.timedelta(weeks=1)
print(now1)
now1 = now + datetime.timedelta(days=1)
print(now1)
now1 = now + datetime.timedelta(hours=1)
print(now1)
now1 = now + datetime.timedelta(minutes=1)
print(now1)
now1 = now + datetime.timedelta(seconds=1)
print(now1)


dt1 = datetime.datetime.strptime('2017-10-16', '%Y-%m-%d')
dt2 = datetime.datetime.strptime('2017-10-27', '%Y-%m-%d')
dt3 = dt2 - dt1

print(dt1)
print(dt2)
print(dt3)


