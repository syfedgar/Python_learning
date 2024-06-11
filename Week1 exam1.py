# Week1 exam
# 描述
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求： 
# 如果输入值是0，直接输出"Hello World" 

# 如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）

# 如果输入值小于0，以垂直方式输出"Hello World"


    # 获取用户输入的整数
user_input = int(input("请输入一个整数: "))
    
    # 定义字符串
message = "Hello World"
    
if user_input == 0:
        # 输入值是0，直接输出
        print(message)
elif user_input > 0:
        # 输入值大于0，以两个字符一行方式输出
    for i in range(0, len(message), 2):
        print(message[i:i+2])
else:
        # 输入值小于0，以垂直方式输出
    for char in message:
        print(char)

