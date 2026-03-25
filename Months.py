import datetime
for month in range (1,13):
    date_obj=datetime.date(2024, month, 1)
    print(date_obj.strftime("%B"))