import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

data = pd.read_excel("convertcsv (1).xlsx")



df= pd.DataFrame(data[['events/teamId','events/period/displayName','events/type/displayName','events/playerId','events/x','events/y','events/endX','events/endY']])


df.drop(df[df['events/teamId'] != 167].index, inplace = True)
df.drop(df[df['events/type/displayName'] != 'Pass' ].index, inplace = True)
df.drop(df[df['events/playerId'] != 136741].index, inplace = True)
#df.drop(df[df['events/period/displayName'] != 'SecondHalf'].index, inplace = True)



df.reset_index(drop=True, inplace=True)

print(df)



df['events/x'] = df['events/x'].astype(int)
df['events/y'] = df['events/y'].astype(int)
df['events/endX'] = df['events/endX'].astype(int)
df['events/endY'] = df['events/endY'].astype(int)

df['events/x'] = df['events/x'] * 1.2
df['events/y'] = df['events/y'] * .8
df['events/endX'] = df['events/endX'] * 1.2
df['events/endY'] = df['events/endY'] * .8

fig, ax = plt.subplots(figsize=(13.5, 8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

# this is how we create the pitch
pitch = Pitch(pitch_type='statsbomb', orientation='horizontal',
              pitch_color='#22312b', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)

# Draw the pitch on the ax figure as well as invert the axis for this specific pitch
pitch.draw(ax=ax)
plt.gca().invert_xaxis()

kde = sns.kdeplot(
        df['events/x'],
        df['events/y'],
        shade = True,
        shade_lowest=True,
        alpha=.5,
        n_levels=10,
        cmap = 'magma'
)

# use a for loop to plot each pass
for x in range(len(df['events/x'])):
    if df['events/type/displayName'][x] == 'Pass':
        plt.plot((df['events/x'][x], df['events/endX'][x]), (df['events/y'][x], df['events/endY'][x]), color='green')
        plt.scatter(df['events/x'][x], df['events/y'][x], color='yellow')




plt.title('Bernardo Silva vs Manchester United', color='white', size=20)



plt.show()