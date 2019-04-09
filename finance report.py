i1=21
i2=21
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as md
a2=0.0198
b2=0.0072
asd2=0.055562186
bsd2=0.036423419
corr2=0.26
print("The averaged monthly returns(%) of Alphabet Inc.(GOOG): 1.98 %")
print("The SD(%) of Alphabet Inc.(GOOG): ",asd2*100,"%")
print("The averaged monthly returns(%) of Coca-Cola(KO): ",b2*100,"%")
print("The SD(%) of Coca-Cola(KO): ",bsd2*100,"%")
print("The Correlation coefficient between GOOG & KO: ",corr2*100," %")
cov=float(corr2*asd2*bsd2)
x1=[]
y1=[]
print("Expected Return:")
print("GOOG:KO")
for i2 in range(i2):
    k=float((a2*((100-int(i2)*5)/100)+\
    b2*((0+int(i2)*5)/100)))
    k1=k*100
    print(str(20-i2),":",str(i2),"   ","%.3f" % k1,"%")
    y1.append(float("%.3f" % k1))

else:
    print("\n")
print("Volatility:")
print("GOOG:KO")
for i1 in range(i1):
    v=float((((20-int(i1))*(1/20))**2)*(asd2**2)+\
    ((int(i1)*(1/20))**2)*(bsd2**2)+\
    2*cov*(20-int(i1))/20*int(i1)/20)**(1/2)
    v1=v*100
    print(str(20-i1),":",str(i1),"   ","%.3f" %v1,"%")
    x1.append(float("%.3f" % v1))

else:
    print("\n")
x=x1
y=y1
plt.plot(x,y,linewidth = 2)
plt.plot(x,y,marker='o',color='blue')
plt.xlabel("Volatility(%)")
plt.ylabel("Monthly return(%)")
plt.title("volatility vs. monthly return")
plt.savefig("plot.png",dpi=300,fprmat="png")
