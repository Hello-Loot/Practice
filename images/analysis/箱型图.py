import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 创建数据框
# 读取学生成绩数据
scores = pd.read_excel(r"C:\Users\lenovo\Desktop\StudentsPerformance1.xlsx")
df = pd.DataFrame(scores)

# 设置图形参数
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))
fig.subplots_adjust(wspace=0.4)

# 绘制并列箱线图
for i, exam in enumerate(['final exam', 'phase exam', 'midterm exam']):
    ax = axes[i]
    sns.boxplot(data=df, x='group', y=exam, ax=ax)
    ax.set_title(f'Exam: {exam}')
    ax.set_xlabel('Group')
    ax.set_ylabel('Score')

# 显示图形
plt.tight_layout()
plt.show()