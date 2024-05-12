import pandas as pd
import matplotlib.pyplot as plt

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 按组分组并计算阶段考试、期中考试和期末考试成绩的平均值
group_averages_midterm = scores.groupby('group')['midterm exam'].mean()
group_averages_phase = scores.groupby('group')['phase exam'].mean()
group_averages_final = scores.groupby('group')['final exam'].mean()

# 设置图像尺寸和比例
plt.figure(figsize=(16, 6))

# 绘制阶段考试曲线
plt.subplot(1, 3, 1)  # 创建第一个子图
plt.plot(group_averages_phase.index, group_averages_phase.values, marker='o', color='steelblue', linewidth=2)
plt.title("Average Phase Exam Score by Group")
plt.xlabel("Group")
plt.ylabel("Average Phase Exam Score")
plt.grid(True, linestyle='--', alpha=0.5)
for x, y in zip(group_averages_phase.index, group_averages_phase.values):
    plt.text(x, y, str(round(y, 2)), ha='center', va='bottom', fontsize=10)

# 绘制期中考试曲线
plt.subplot(1, 3, 2)  # 创建第二个子图
plt.plot(group_averages_midterm.index, group_averages_midterm.values, marker='o', color='steelblue', linewidth=2)
plt.title("Average Midterm Exam Score by Group")
plt.xlabel("Group")
plt.ylabel("Average Midterm Exam Score")
plt.grid(True, linestyle='--', alpha=0.5)
for x, y in zip(group_averages_midterm.index, group_averages_midterm.values):
    plt.text(x, y, str(round(y, 2)), ha='center', va='bottom', fontsize=10)

# 绘制期末考试曲线
plt.subplot(1, 3, 3)  # 创建第三个子图
plt.plot(group_averages_final.index, group_averages_final.values, marker='o', color='steelblue', linewidth=2)
plt.title("Average Final Exam Score by Group")
plt.xlabel("Group")
plt.ylabel("Average Final Exam Score")
plt.grid(True, linestyle='--', alpha=0.5)
for x, y in zip(group_averages_final.index, group_averages_final.values):
    plt.text(x, y, str(round(y, 2)), ha='center', va='bottom', fontsize=10)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()