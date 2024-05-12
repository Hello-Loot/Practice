
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 提取阶段考试、期中考试和期末考试成绩
phase_exam_scores = scores['phase exam']
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']

# 创建成绩相关性矩阵
correlation_matrix = scores[['phase exam', 'midterm exam', 'final exam']].corr()

# 绘制两两关系图
plt.figure(figsize=(12, 4))

# 阶段考试 vs. 期中考试
plt.subplot(1, 2, 1)
plt.scatter(phase_exam_scores, midterm_exam_scores, color='blue')
plt.xlabel('Phase Exam Scores')
plt.ylabel('Midterm Exam Scores')
plt.title('Phase Exam vs. Midterm Exam')

# 阶段考试 vs. 期末考试
plt.subplot(1, 2, 2)
plt.scatter(phase_exam_scores, final_exam_scores, color='red')
plt.xlabel('Phase Exam Scores')
plt.ylabel('Final Exam Scores')
plt.title('Phase Exam vs. Final Exam')

plt.tight_layout()
plt.show()
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取学生成绩数据

# 提取阶段考试、期中考试和期末考试成绩以及组别
phase_exam_scores = scores['phase exam']
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']
groups = scores['group']

# 创建包含成绩和组别的新数据框
data = pd.DataFrame({'Phase Exam': phase_exam_scores,
                     'Midterm Exam': midterm_exam_scores,
                     'Final Exam': final_exam_scores,
                     'Group': groups})

# 绘制散点图
sns.pairplot(data, hue='Group')
plt.suptitle("Scatter Plot of Exam Scores by Group")
plt.show()
"""