import matplotlib.pyplot as plt
#line
X = [1,2,3,4,5,6,7,8,9,10,11,12]
Y1= [153,144,216,345,890,1121,1872,1792,1521,737,326,143]
Y2 = [1532,1521,1231,974,753,329,221,198,265,543,1216,1673]
plt.plot(X,Y1,Y2)
plt.show()

#bar
plt.bar(X,Y1,color="red")
plt.bar(X,Y2,color="blue")
plt.legend()
plt.show()

