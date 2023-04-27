from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表中
resluts = []
for roll_num in range(1000):
    reslut = die.roll()
    resluts.append(reslut)

# print(resluts)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = resluts.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')






