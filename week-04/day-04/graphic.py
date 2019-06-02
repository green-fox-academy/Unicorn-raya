from views import emoji,message,mention,thank
import matplotlib.pyplot as plt
import numpy as np

n = 20
# X = np.arange(n)
# # np.random.uniform(0.5, 1.0, n) 在[0.5 1.0)随机生成n个浮点数
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

para = thank

X = [ x[0] for x in para]
Y1 = np.array([float(x[1]) for x in para])

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')

for x, y in zip(X, Y1):
    plt.xticks(rotation=90)
    plt.text(x, y + 0.05, '%s' % y, ha='center', va='bottom')

plt.show()

plt.close()