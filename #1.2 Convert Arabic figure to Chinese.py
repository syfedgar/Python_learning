#1.2 Convert Arabic figure to Chinese
# Chinese_Figure = "零一二三四五六七八九"
# Math_Figure = input("请输入0到9的阿拉伯数字:")
# print(Chinese_Figure[eval(Math_Figure[0]):(eval(Math_Figure[-1]) + 1 )])

template = "零一二三四五六七八九"

s = input("请输入阿拉伯数字：")
for c in s:
    print(template[eval(c)], end="")