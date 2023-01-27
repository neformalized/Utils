invest = 1000
dayly = 4
cast = 10

#

#days = round(100/dayly, 2)

#######################

#print("==========================================================")
#print("-------------")
#print("standart plan")
#print("-------------")
#print("Begin sum: {}$ | Begin percent: {}% | Days to multiply: {}".format(invest, dayly, round(days, 1)));

#totalInvest = invest

#for i in range(1, cast):
#    totalInvest *= 2
#    print("round {} - {:,}$ - x{} - days {}".format(i, totalInvest, round(totalInvest/invest), round(days * i)))
#

#totalInvest *= 2

#print("----------------------------------------------------------")
#print("round {} - {:,}$ - x{} - days {}".format(i + 1, totalInvest, round(totalInvest/invest), round(days * (i + 1))))
#print("----------------------------------------------------------")
#print()

#days = round(days * (i + 1))

#######################

days = 365

print("==========================================================")
print("-------------")
print("reinvest plan")
print("-------------")
print("Begin sum: {}$ | Begin percent: {}% | Period {}".format(invest, dayly, days));

totalInvest = invest

for i in range(1, days):
    totalInvest = totalInvest + (totalInvest * (dayly/100))
    if(i % 7 == 0): print("Day {} - {:,}$ | x{:,}".format(i, round(totalInvest), round(totalInvest/invest, 2)));
#

totalInvest = totalInvest + (totalInvest * (dayly/100))

print("----------------------------------------------------------")
print("Day {} - {:,}$ | x{:,}".format(i + 1, round(totalInvest), round(totalInvest/invest, 1)));
print("----------------------------------------------------------")