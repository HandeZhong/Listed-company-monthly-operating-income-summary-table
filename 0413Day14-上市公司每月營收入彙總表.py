"""
標題:111年上市公司每月營業收入彙總表.csv
日期:2022/04/13
作者:Han-De Zhong
資料來源:https://data.gov.tw/dataset/18420
"""
"""
#### 第1題 ######
請自行到 openData 找自己感興趣的題目來做
txt, CSV, XLSX, XLS
比如：
https://data.tycg.gov.tw/
https://data.taipei/
http://www.kaggle.com
先不找JSON, XML,  SOAP

#### 第2題 ######
分析數據
Max, Min, Ave,  Mid 中間值, 均值......
166-CSV-環境輻射即時監測資訊歷史資料-圖表-統計.py

#### 第3題 ######
畫圖表
156-作業答案-讀取excel顯示9個圖表.py
"""

import csv                                           # 匯入csv類別
import numpy as np                                   # 匯入numpy 類別，並設定為 np
import matplotlib.image as mpimg                     # 匯入image 類別，並設定為 mpimg
import matplotlib.pyplot as plt                      # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties   # 中文字體
from PIL import ImageTk, Image


# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun']           # 步驟一（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False           # 步驟二（解決座標軸負數的負號顯示問題）

list1=[]
list2=[]
listDate=[]
with open('上市公司每月營業收入彙總表.csv', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        print(header)
        x=0
        for row in read:
            print(row[1])
            list1.append(int(x))             # 第幾筆資料
            list2.append(float(row[5]))      # 取得當月營收
            listDate.append(row[0])          # 日期
            x=x+1

# 2. 最大 最小 平均
def findValue(value1):
    global sheet
    global list1
    global list2
    global listDate
    for i in range(1, len(list2)):
        try:
            curr = list2[i]  # 當月營收
            if value1 == curr:
                print("日期是:",listDate[i],"價格為:",list2[i])
        except:
            print("error-----------")

print("最大",max(list2))
print(findValue(max(list2)))
print("最小",min(list2))
print(findValue(min(list2)))   # <----

avg_value = 0 if len(list2) == 0 else sum(list2)/len(list2)
print("平均",avg_value)



# 3. 畫出圖表
plt.plot(list1,list2, 'g-')
plt.title("上市公司當月營收")
plt.show()
