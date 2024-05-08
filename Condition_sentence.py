"""  if 条件:
        aaa
        else:
        bbbb"""

# 注意缩进问题，没有统一缩进会导致程序报错；一般会用4个空格，pycharm会自动加4个空格；或者用tab键也会是4个空格

# print("开始")
# if True :
#     print("123")
# else:
#     print("456")
# print("结束")


username = input("please input username")
password = input("please input password")
if username == "Susan" and password == "666":
    print("congratulation to log in successfully")
else:
    print("log failed")
