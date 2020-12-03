import math
dataFile = open("testdata", "w")
for i in range(1,240):
    x = 120
    y = i%60 + 1
    z = 36
    line = str(x) + "," + str(y) + "," + str(z) + "\n"
    dataFile.write(line)
dataFile.close
print "Generated Data"