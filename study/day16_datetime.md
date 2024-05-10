# 获取当前时间
```python
from datetime import datetime 

now = datetime.now() 
print("now =", now)  #  2024-05-10 10:18:25.886157
print("year =", now.year) # 2024 
print("month =", now.month) # 5 
print("day =", now.day)  # 10 

print("hour =", now.hour) # 10 
print("minute =", now.minute) # 18 
print("second =", now.second) # 25 

print("timestamp =",now.timestamp()) # 1715307579.923927
```

# 格式化日期和时间
```python
from datetime import datetime 

new_date = datetime(2023,12,31,12,30,59)
print("now =", new_date)  #  2023-12-31 12:30:59
print("year =", new_date.year) # 2023
print("month =", new_date.month) # 12
print("day =", new_date.day)  # 31

print("hour =", new_date.hour) # 12 
print("minute =", new_date.minute) # 30
print("second =", new_date.second) # 59 
```

## strftime()方法 格式化时间
```python
from datetime import datetime 

new_date = datetime(2023,12,31,12,30,59)
print("now =", new_date)  #  2023-12-31 12:30:59

# 格式化成2023-12-31 12:30:59格式
print(new_date.strftime("%Y-%m-%d %H:%M:%S")) # 2023-12-31 12:30:59

# 格式化成2023-12-31格式
print(new_date.strftime("%Y-%m-%d")) # 2023-12-31

# 格式化成12:30:59格式
print(new_date.strftime("%H:%M:%S")) # 12:30:59
```

## strptime: string convert To datetime
```python
from datetime import datetime 

date_str = "2023-12-31 12:30:59"
new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("now =", new_date)  #  2023-12-31 12:30:59
```


