import matplotlib.pyplot as plt
import math

# 生成数据
x_values = range(1, 5001)
y_values = [math.pow(x, 3) for x in x_values]

# 设置绘图样式
plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei'] # 解决中文不显示的情况 - 非完全解决
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.GnBu, s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方数", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 5100, 0, 150000000000])

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()