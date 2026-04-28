s_year, s_month, s_day = map(int, input().split())
e_year, e_month, e_day = map(int, input().split())
year = e_year - s_year
month = e_month - s_month
day = e_day - s_day
days = year * 360 + month * 30 + day
monthly = days // 30
if monthly > 36:
    monthly = 36
A = ((days // 360) + 1) // 2 - 1
if A < 0:
    A = 0
yearly = 0
for i in range(1, days // 360 + 1):
    A = (i + 1) // 2 - 1
    yearly += (A + 15)
print(yearly, monthly)
print(f'{days}days')