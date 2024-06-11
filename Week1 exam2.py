# Week1 exam2

# number = 123.456
# formatted_number0 = "{:5.2f}".format(number)
# formatted_number1 = "{:6.2f}".format(number)
# formatted_number2 = "{:7.2f}".format(number)
# formatted_number3 = "{:10.2f}".format(number)
# print(formatted_number0,formatted_number1, formatted_number2, formatted_number3)  # 输出：  123.46
# print(f"{formatted_number0}\n{formatted_number1}\n{formatted_number2}\n{formatted_number3}")



# expression = input("请格式 M OP N 输入一个算式表达式：")
# M, OP, N = expression.split()

# M = float(M)
# N = float(N)

# result = 0
# if OP == '+':
#     result = M + N
# elif OP == '-':
#     result = M - N
# elif OP == '*':
#     result = M * N
# elif OP == '/':
#     result = M / N

# formatted_result = "{:.2f}".format(result)
# print(formatted_result)




s = input("请格式 M OP N 输入一个算式表达式：")
print("{:.2f}".format(eval(s)))