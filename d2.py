from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today +timedelta(days = 1)

print(yesterday.strftime("%A"))
print(today.strftime("%A"))
print(tomorrow.strftime("%A"))