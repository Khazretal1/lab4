from datetime import datetime, timedelta

def sec_diff(date1, date2):
    diff = date1 - date2
    return diff.total_seconds()

date_format =  "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(input("Enter 1st date (YYYY-MM-DD HH:MM:SS): "), date_format) 
date2 = datetime.strptime(input("Enter 1st date (YYYY-MM-DD HH:MM:SS): "), date_format) 


print(sec_diff(date1, date2))