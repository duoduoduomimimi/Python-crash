import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取最高温度和日期
    highs, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# print(highs)



# 根据最高温度绘制图形
plt.style.use('seaborn')
# 解决绘图时，中文不显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图形格式
ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
