import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


data = pd.read_excel("convertcsv (1).xlsx")



df= pd.DataFrame(data[['events/teamId','events/type/displayName','events/playerId','events/x','events/y','events/endX','events/endY']])


df.drop(df[df['events/teamId'] != 167].index, inplace = True)
df.drop(df[df['events/type/displayName'] != 'Pass' ].index, inplace = True)
df.drop(df[df['events/playerId'] != 73084].index, inplace = True)








df2 = pd.DataFrame(df)


df2.reset_index(drop=True, inplace=True)

print(df2)
count_nan_in_df = df2.isnull().sum().sum()
print ('Count of NaN: ' + str(count_nan_in_df))

df2['events/x'] = df2['events/x'].astype(int)
df2['events/y'] = df2['events/y'].astype(int)
df2['events/endX'] = df2['events/endX'].astype(int)
df2['events/endY'] = df2['events/endY'].astype(int)

df2['events/x'] = df2['events/x'] * 1.2
df2['events/y'] = df2['events/y'] * .8
df2['events/endX'] = df2['events/endX'] * 1.2
df2['events/endY'] = df2['events/endY'] * .8



#Create figure
fig=plt.figure()
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)

#Pitch Outline & Centre Line
plt.plot([0,0],[0,90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")
plt.plot([65,65],[0,90], color="black")

#Left Penalty Area
plt.plot([16.5,16.5],[65,25],color="black")
plt.plot([0,16.5],[65,65],color="black")
plt.plot([16.5,0],[25,25],color="black")

#Right Penalty Area
plt.plot([130,113.5],[65,65],color="black")
plt.plot([113.5,113.5],[65,25],color="black")
plt.plot([113.5,130],[25,25],color="black")

#Left 6-yard Box
plt.plot([0,5.5],[54,54],color="black")
plt.plot([5.5,5.5],[54,36],color="black")
plt.plot([5.5,0.5],[36,36],color="black")

#Right 6-yard Box
plt.plot([130,124.5],[54,54],color="black")
plt.plot([124.5,124.5],[54,36],color="black")
plt.plot([124.5,130],[36,36],color="black")

#Prepare Circles
centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
centreSpot = plt.Circle((65,45),0.8,color="black")
leftPenSpot = plt.Circle((11,45),0.8,color="black")
rightPenSpot = plt.Circle((119,45),0.8,color="black")

#Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

#Prepare Arcs
leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

#Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)

#Tidy Axes
plt.axis('off')

#for i in range(len(df2)):
#   plt.plot([int(df2["events/x"][i]), int(data["events/endX"][i])],
#            [int(data["events/y"][i]), int(data["events/endY"][i])],
#             color="blue")

for i in range(len(df2)):
   plt.plot([(df2["events/x"][i]), (data["events/endX"][i])],
            [(data["events/y"][i]), (data["events/endY"][i])],
             color="blue")


plt.plot(int(df2["events/x"][i]),int(df2["events/y"][i]),"o", color="green")

plt.show()

