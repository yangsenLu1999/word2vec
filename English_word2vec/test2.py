import matplotlib.pyplot as plt

# 创建Figure和Axes对象
fig, ax = plt.subplots()

# 绘制数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y, linestyle=':', color='red', marker='o')

# 添加标签和标题
ax.set_xlabel('X Label/mmmmm', fontsize=20)
ax.set_ylabel('Y Label', fontsize=12)
ax.set_title('My Plot', fontsize=14)

# 设置刻度和范围
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_xlim([0, 6])
ax.set_ylim([0, 12])

# 添加图例
ax.legend(['line1'])

# 显示图形
plt.show()