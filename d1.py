from datetime import datetime, timedelta

current = datetime.now()
new_time = current - timedelta(days = 5)

print(new_time.strftime("%A"))