import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 获取整体学生的阶段考试、期中考试和期末考试成绩数据
phase_exam_scores = scores['phase exam']
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']

# 设置图像尺寸和比例
plt.figure(figsize=(12, 6))

# 绘制阶段考试成绩的直方图和密度分布图
plt.subplot(1, 3, 1)  # 创建第一个子图
sns.histplot(phase_exam_scores, bins=10, color='skyblue', edgecolor='k', alpha=0.7)
sns.kdeplot(phase_exam_scores, color='skyblue', shade=True)
plt.title("Phase Exam Scores")
plt.xlabel("Score")
plt.ylabel("Frequency / Density")

# 绘制期中考试成绩的直方图和密度分布图
plt.subplot(1, 3, 2)  # 创建第二个子图
sns.histplot(midterm_exam_scores, bins=10, color='lightgreen', edgecolor='k', alpha=0.7)
sns.kdeplot(midterm_exam_scores, color='lightgreen', shade=True)
plt.title("Midterm Exam Scores")
plt.xlabel("Score")
plt.ylabel("Frequency / Density")

# 绘制期末考试成绩的直方图和密度分布图
plt.subplot(1, 3, 3)  # 创建第三个子图
sns.histplot(final_exam_scores, bins=10, color='lightcoral', edgecolor='k', alpha=0.7)
sns.kdeplot(final_exam_scores, color='lightcoral', shade=True)
plt.title("Final Exam Scores")
plt.xlabel("Score")
plt.ylabel("Frequency / Density")

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()