#导入csv模块
import csv
from matplotlib import pyplot as plt
 
#指定文件名，然后使用 with open() as 打开
filename = 'runs/detect/train4/results.csv'
with open(filename) as f:
        #创建一个阅读器：将f传给csv.reader
        reader = csv.reader(f)
        #使用csv的next函数，将reader传给next，将返回文件的下一行
        header_row = next(reader)
        train_loss=[]
        for row in reader:
                train_loss.append(float(row[9]))
        print(train_loss)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(train_loss,c='blue')
#设置图形的格式
plt.title("Train loss graph", fontsize=24)
plt.xlabel('train_loss',fontsize=16)
plt.ylabel("", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)
 
plt.show()

        
        # for index, column_header in enumerate(header_row):
                # print(index, column_header)
        
        