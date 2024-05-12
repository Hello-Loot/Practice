import pandas as pd
import matplotlib.pyplot as plt

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

print("学生成绩数据：")
print(scores.head())

# 数据的概要信息
print("\n数据的概要信息：")
scores.info()

# 列名
print("\n列名：")
print(scores.columns)

# 给出数据的概略信息
print("\n数据的概略信息：")
print(scores.describe())

import pandas as pd
import matplotlib.pyplot as plt

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 按组分组并计算期末考试成绩的平均值
group_averages_final = scores.groupby('group')['final exam'].mean()

# 设置图像尺寸和比例
plt.figure(figsize=(8, 6))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

# 绘制曲线图
plt.plot(group_averages_final.index, group_averages_final.values, marker='o', color='steelblue', linewidth=2)

# 设置标题、标签和图例
plt.title("Average Final Exam Score by Group", fontsize=16)
plt.xlabel("Group", fontsize=12)
plt.ylabel("Average Final Exam Score", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.5)

# 显示每个数据点的数值标签
for x, y in zip(group_averages_final.index, group_averages_final.values):
    plt.text(x, y, str(round(y, 2)), ha='center', va='bottom', fontsize=10)

# 显示图表
plt.show()