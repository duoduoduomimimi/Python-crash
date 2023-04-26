import matplotlib.pyplot as plt

# 生成数据
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# 自动计算数据
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# 设置绘图样式
plt.style.use('seaborn')
plt.rcParams['font.sans-serif']=['SimHei'] # 解决中文不显示的情况 - 非完全解决
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)  绘制单个点
ax.scatter(x_values, y_values, c=(0.0, 0.7, 0.2), s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()