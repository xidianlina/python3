'''
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
'''

import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))
    
    birthDate=datetime.date(1985,5,8)    
    print(birthDate.strftime('%d/%m/%Y'))

    birthNextDay=birthDate+datetime.timedelta(days=1)
    print(birthNextDay.strftime('%d/%m/%Y'))

    firstBirthday=birthDate.replace(year=birthDate.year+1)
    print(firstBirthday.strftime('%d/%m/%Y'))
