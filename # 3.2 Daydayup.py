# 天天向上的力量
# print(1.001**365)
# print(0.999**365)

# # #daydayup Q1
# dayup = pow(1.001, 365)
# daydown = pow(0.999, 365)
# print("向上:{:.2f}, 向下{:.2f}".format(dayup,daydown))


# # daydayup Q2
# dayfactor = 0.01
# dayup =pow(1+dayfactor, 365)
# daydown = pow(1-dayfactor,365)
# print("向上:{:.2f}, 向下{:.2f}".format(dayup,daydown))

# daydayup Q3 workday +1%, weekend -1%
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

#daydayup Q4 workday +?%, weekend -1%

# def dayUP(df):
#     dayup = 1
#     for i in range(365):
#         if i % 7 in [6,0]:
#             dayup = dayup*(1 - 0.01)
#         else:
#             dayup = dayup*(1 + df)
#         return dayup
# dayfactor = 0.01
# while dayUP(dayfactor) < 37.78:
#     dayfactor += 0.001
# print("工作日努力的参数是:{:.3f}".format(dayfactor))

# GRIT: Perserverance and passion for long-term goals
#       坚毅，对长期目标的持续激情及持久耐力；是获得成功最重要的因素之一；