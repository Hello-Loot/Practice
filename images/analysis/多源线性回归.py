import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import numpy as np

# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")

# 提取阶段考试、期中考试和期末考试成绩
phase_exam_scores = scores['phase exam']
midterm_exam_scores = scores['midterm exam']
final_exam_scores = scores['final exam']

# 创建包含阶段考试、期中考试和期末考试成绩的新数据框
data = pd.DataFrame({'Phase Exam': phase_exam_scores,
                     'Midterm Exam': midterm_exam_scores,
                     'Final Exam': final_exam_scores})

# 使用多元线性回归模型拟合数据
reg_model = LinearRegression()
reg_model.fit(data[['Phase Exam', 'Midterm Exam']], data['Final Exam'])

# 获取回归方程的系数和截距
coefficients = reg_model.coef_
intercept = reg_model.intercept_

# 绘制3D散点图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Phase Exam'], data['Midterm Exam'], data['Final Exam'], c='blue', marker='o', alpha=0.8)

# 添加拟合平面
x = data['Phase Exam']
y = data['Midterm Exam']
x_mesh, y_mesh = np.meshgrid(x, y)
z = coefficients[0] * x_mesh + coefficients[1] * y_mesh + intercept
ax.plot_surface(x_mesh, y_mesh, z, alpha=0.1, color='red', edgecolor='none')

# 设置坐标轴标签
ax.set_xlabel('Phase Exam')
ax.set_ylabel('Midterm Exam')
ax.set_zlabel('Final Exam')

# 设置图表标题
plt.title("Relationship between Phase Exam, Midterm Exam, and Final Exam Scores")

# 设置图例
scatter_proxy = plt.Rectangle((0, 0), 1, 1, fc="blue")
surface_proxy = plt.Rectangle((0, 0), 1, 1, fc="red", alpha=0.3)
ax.legend([scatter_proxy, surface_proxy], ['Data Points', 'Regression Plane'])

# 设置视角
ax.view_init(elev=20, azim=-45)

# 调整图像边界
ax.dist = 12

plt.show()