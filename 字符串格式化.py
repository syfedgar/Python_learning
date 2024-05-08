"""
2.1 %
  name = input("please input your name")
  age = input("please input age")
  text = "I'm %s,%d" %(name,age)

  当格式化字符串中有%时，需要用%%用于让电脑知道其为%，而不是占位符 %s,or , %d
2.2 format(recommended)
  text = "I'm {0}, {1}years old, name is {0}".format("name","age")

  text = "I'm {n1}, {n2}years old, name is {n1}".format(n1="name",n2="age")


  text = "I'm {n1}, {n2}years old, name is {n1}"
  data1 = text.format(n1="name",n2="age")
  data2 = text.format()
2.3 f(for version 3.6 or newer)

  action = "run"
  text = f"I like to {action}"

"""

# count = 0
# while count < 3:
#     count += 1
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "Edgar" and password == "1983":
#         print("登录成功")
#         break
#     else:
#         message = ("用户名或密码输入错误，剩余错误次数：{}次").format(3 - count)
#         print(message)

count = 0
while count < 3:
    count += 1
    age = input("请输入你的年龄：")
    age = int(age)
    if age == 8:
        print("你猜对了！")
        break
    else:
        print("你猜错了！")

    if count == 3:
        choice = input("是否还继续玩(Y/N)？")
        if choice == "N":
            break
        elif choice == "Y":
            count = 0
            continue
        else:
            print("输入错误！")
            break
    else:
        continue
