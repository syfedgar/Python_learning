#Daydayup_Final
 

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日努力的参数是:{:.3f}".format(dayfactor))

# def dayUP(df):  
#     dayup = 1  
#     for i in range(365):  
#         if i % 7 in [6, 0]:  # 周六和周日  
#             dayup *= (1 - 0.01)  
#         else:  
#             dayup *= (1 + df)  
#     return dayup  
  
# dayfactor = 0.01  
# precision = 1e-3  # 设置一个精度阈值  
# while dayUP(dayfactor) < 37.78:  
#     dayfactor += precision  
#     if dayUP(dayfactor) >= 37.78:  # 检查是否已经超过目标值，如果是，则跳出循环  
#         break  
  
# print("工作日努力的参数是:{:.3f}".format(dayfactor))