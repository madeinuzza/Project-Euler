# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


months = {"January" : 31, "February" : 28, "March": 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}
months_leap = {"January" : 31, "February" : 29, "March": 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}


def is_it_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        return True 

count_day = 366
# def january_first_1901(count_day):
#     for month in sorted(months):
#         count_day += months[month]
#     return count_day

# print(january_first_1901(count_day))
count_sundays = 0
for year in range(1901, 2001):
    if is_it_leap_year(year) == True:
        for month in sorted(months_leap):
            if count_day % 7 == 0: 
                count_sundays += 1 
            count_day += months_leap[month]
    else:
        for month in sorted(months):
            if count_day % 7 == 0: 
               count_sundays += 1
            count_day += months[month]

print(count_sundays) 
        