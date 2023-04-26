import matplotlib
import matplotlib.pyplot as plt
#matplotlib.rc("font",family='Adobe Kaiti Std')  # 解决中文不显示的情况 - 非完全解决

# 打印matplotlib中的内置样式
# print(plt.style.available)

# 设置绘图样式
plt.style.use('seaborn-notebook')
plt.rcParams['font.sans-serif']=['SimHei'] # 解决中文不显示的情况 - 非完全解决

input_values = [1, 2, 3, 4, 5] # 改变plot()数据点对应的默认设置
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)



plt.show()