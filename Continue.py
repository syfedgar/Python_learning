# 结束本次循环，开始下一次循环

# print("begin")
# while True:
#     print(1)
#     continue
#     print(2)
#     print(3)
# print("close")


print("begin")
i = 1
while True:
    if i == 7:
        i = i +1
        continue
    print(i)
    i = i + 1
    if i == 101:
        break
print("over")