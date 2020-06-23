"""
解决乱码
res.content.decode('utf-8')



"""

import re
import requests
import tkinter as tk
import webbrowser

url = 'http://www.qmaile.com/'

resp = requests.get(url)

#  解决乱码
resp.encoding = resp.apparent_encoding
response = resp.text

# 正则 获取数据
res = re.compile('<option value="(.*?)" selected')
reg = re.findall(res, response)
# print(reg)
one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]
five = reg[5]

# 画板
root = tk.Tk()

root.title('VIP电影免费观看')    # 标题

root.geometry('700x250+500+170')   # 画板的长宽 后面两个值的意思是出现的屏幕位置

l1 = tk.Label(root, text='播放接口:(需手动选择接口)', font=('Arial', 12), )
l1.grid()

l2 = tk.Label(root, text='播放链接:', font=('Arial', 12), )
l2.grid(row=6, column=0)

t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)

# 播放接口
var = tk.StringVar()
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='播放接口5', variable=var, value=five)
r5.grid(row=4, column=1)

# 播放函数
def get_data():
    webbrowser.open(var.get()+t1.get())


# 播放按钮
b1 = tk.Button(root, text='播放',font=('Arial', 12), width=8, command=get_data)
b1.grid(row=7, column=1)

# 清除函数
def del_Text():
    t1.delete(0, 'end')


b1 = tk.Button(root, text='清除',font=('Arial', 12), width=8,command=del_Text)
b1.grid(row=8, column=1)



root.mainloop()