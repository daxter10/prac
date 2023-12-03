import matplotlib.pyplot as plt

x=[i for i in range(0,100)]

# z= 2*x + 3*y

y1=[(8-2*i) for i in x]
y2=[(9-3*i) for i in x]

plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot(x,y1,marker=".",c="r",lw="2")
plt.plot(x,y2,marker=".",c="b",lw="2")

z=[]

pt=[[0,0],[0,8],[1,6],[3,0]]

for point in pt:
    x,y=point
    val=2*x+3*y
    z.append(val)

print("feasible area is under points: ",z)
print("maximum optimum value is: ",max(z))
print("minimum optimum value is: ",min(z))

plt.grid(True)
plt.show()










