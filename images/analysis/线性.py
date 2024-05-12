"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取学生成绩数据


# 提取期中考试和期末考试成绩
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']

# 创建包含期中考试和期末考试成绩的新数据框
data = pd.DataFrame({'Midterm Exam': midterm_exam_scores,
                     'Final Exam': final_exam_scores})

# 设置图像风格
sns.set_style("whitegrid")

# 绘制散点图和趋势线
sns.regplot(data=data, x='Midterm Exam', y='Final Exam', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title("Scatter Plot of Midterm Exam and Final Exam Scores", fontsize=14)
plt.xlabel("Midterm Exam Score", fontsize=12)
plt.ylabel("Final Exam Score", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# 显示图像
plt.show()
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 提取期中考试和期末考试成绩
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']

# 创建包含期中考试和期末考试成绩的新数据框
data = pd.DataFrame({'Midterm Exam': midterm_exam_scores,
                     'Final Exam': final_exam_scores})

# 使用线性回归模型拟合数据
reg_model = LinearRegression()
reg_model.fit(data[['Midterm Exam']], data['Final Exam'])

# 获取回归方程的系数和截距
slope = reg_model.coef_[0]
intercept = reg_model.intercept_

# 绘制散点图和趋势线
sns.regplot(data=data, x='Midterm Exam', y='Final Exam')
plt.title("Scatter Plot of Midterm Exam and Final Exam Scores")
plt.xlabel("Midterm Exam Score")
plt.ylabel("Final Exam Score")

# 添加拟合直线
x = np.linspace(data['Midterm Exam'].min(), data['Midterm Exam'].max(), 100)
y = slope * x + intercept
plt.plot(x, y, color='red', label='Regression Line')

# 显示拟合公式
equation = f'Final Exam = {slope:.2f} * Midterm Exam + {intercept:.2f}'
plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.legend()
plt.show()

"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 读取学生成绩数据

# 提取阶段考试和期末考试成绩
phase_exam_scores = scores['phase exam']
final_exam_scores = scores['final exam']

# 创建包含阶段考试和期末考试成绩的新数据框
data = pd.DataFrame({'Phase Exam': phase_exam_scores,
                     'Final Exam': final_exam_scores})

# 使用线性回归模型拟合数据
reg_model = LinearRegression()
reg_model.fit(data[['Phase Exam']], data['Final Exam'])

# 获取回归方程的系数和截距
slope = reg_model.coef_[0]
intercept = reg_model.intercept_

# 绘制散点图和趋势线
sns.regplot(data=data, x='Phase Exam', y='Final Exam')
plt.title("Scatter Plot of Phase Exam and Final Exam Scores")
plt.xlabel("Phase Exam Score")
plt.ylabel("Final Exam Score")

# 添加拟合直线
x = np.linspace(data['Phase Exam'].min(), data['Phase Exam'].max(), 100)
y = slope * x + intercept
plt.plot(x, y, color='red', label='Regression Line')

# 显示拟合公式
equation = f'Final Exam = {slope:.2f} * Phase Exam + {intercept:.2f}'
plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.legend()
plt.show()

# 绘制线性回归图
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="test preparation course", y="final exam", hue="test preparation course", palette="Set1")
sns.lineplot(x=df["test preparation course"], y=results.fittedvalues, color='red', label="Regression Line")

# 设置图形标签
plt.title("Test Preparation Course vs Final Exam Score")
plt.xlabel("Test Preparation Course")
plt.ylabel("Final Exam Score")

# 显示图形
plt.legend()
plt.show()"""