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
plt.figure(figsize=(15, 6))

# 绘制阶段考试成绩的密度分布图
plt.subplot(1, 3, 1)
sns.kdeplot(phase_exam_scores, color='skyblue', shade=True)
plt.title("Density Distribution of Phase Exam Scores")
plt.xlabel("Score")
plt.ylabel("Density")

# 绘制期中考试成绩的密度分布图
plt.subplot(1, 3, 2)
sns.kdeplot(midterm_exam_scores, color='lightgreen', shade=True)
plt.title("Density Distribution of Midterm Exam Scores")
plt.xlabel("Score")
plt.ylabel("Density")

# 绘制期末考试成绩的密度分布图
plt.subplot(1, 3, 3)
sns.kdeplot(final_exam_scores, color='lightcoral', shade=True)
plt.title("Density Distribution of Final Exam Scores")
plt.xlabel("Score")
plt.ylabel("Density")

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()