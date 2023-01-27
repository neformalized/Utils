import os

#

dir = "D:\\Log\\BNBUSDT\\"

#

for file in os.listdir(dir):
    
    lines = open("{}{}".format(dir, file), "r").readlines()
    
    maximum = 0
    
    for line in lines:
        
        d = line.split("|")
        
        if(float(d[1]) > maximum): maximum = float(d[1])
        if(float(d[3]) > maximum): maximum = float(d[3][0: -2])
    #
    
    d = lines[-1].split("|")
    
    print("{} - total: {}$,{}$({}) | max: {}$;".format(file, d[1], d[3][0: -2], d[2], maximum))
#