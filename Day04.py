#题目: 输入某年某月末日，判断这一天是这一年的第几天？

#分析: 输入 2019-5-20 是这一年的第几天
# 1月：31天
# 2月：28天 或者 29天 ？ 如何判断输入年份是否是闰年 
# （2019年不是闰年)
# 一般能被4整除的年份是闰年，
# 不能被4整除的年份是平年；
# 而当遇到世纪年（也就是整百年），就只有能被400整除才是闰年，否则就是平年。
# 3月：31天
# 4月：30天
# 5月：第20天
# 31+28+31+30+20= 140

datetime=input("请输入日期(格式:2010-10-1)不按格式输入可能会出错:")
year = int(datetime.split('-')[0])
month= int(datetime.split('-')[1])
day = int(datetime.split('-')[2])
# days_in_month_tuple=(31,28,31,30,31,30,31,31,30,31,30,31)
# sum = 0
#没有对输入进行判断，所以在输入不正确的时候程序可能会出错
def leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)): # 不是百年的情况 只要满足整除4即可
        return True
    if (year % 100 == 0) and (year % 400 == 0): # 百年的情况 要同时满足 整除400
        return True
    print("False")
    return False

# if (leap_year(year)== False) or (month <=2):# 不是闰年 或者月份比小于等于2 的
#     for i in range(0,month-1):
#         sum += days_in_month_tuple[i]
#     sum += day
# else:
#     for i in range(0,month-1):
#         sum += days_in_month_tuple[i]
#     sum +=day
#     sum +=1 # 闰年加一天
# print("第{}天".format(sum))

#方法2：
days_in_month_tuple=(0,31,59,120,151,181,212,243,273,304,334)# 如果日期在第一个月，则没有前一个月需要加
                                                             # 如果日期是2月1 日，则需要加上一月的31天
if (leap_year(year)== False) or (month <=2):# 不是闰年 或者月份比小于等于2 的
    sum = days_in_month_tuple[month-1]
    sum += day
else:
    sum = days_in_month_tuple[month-1]
    sum +=day
    sum +=1 # 闰年加一天
print("第{}天".format(sum))
#为什么方法二比方法一更好呢?