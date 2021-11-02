import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

plt.style.use('seaborn')
fig,ax=plt.subplots(4)
fig.suptitle("Calories Information According to Heart Rate\nby Shakil Mahmud")
fig.tight_layout(pad=3)

ax[0].set_title('Duration',color='red',size=10)
ax[0].plot(df['Duration'],color='red',marker='o',markersize=3,linewidth=0.5,label='Duration')
ax[0].set_xlabel('serial axis',color='red',size=9)
ax[0].set_ylabel('Duration',color='red',size=9)
ax[0].legend(loc='upper right')

ax[1].set_title('Pulse',color='green',size='10')
ax[1].plot(df['Pulse'],color='green',marker='o',markersize=2,linewidth=0.5,label='Pulse')
ax[1].set_xlabel('series axis',color='green',size=9)
ax[1].set_ylabel('Pulse',color='green',size=9)
ax[1].legend(loc='upper right')

ax[2].set_title('Maxpulse',color='blue',size='10')
ax[2].plot(df['Maxpulse'],color='blue',marker='o',markersize=2,linewidth=0.5,label='Maxpulse')
ax[2].set_xlabel('series axis',color='blue',size=9)
ax[2].set_ylabel('Maxpulse',color='blue',size=9)
ax[2].legend(loc='upper right')

ax[3].set_title('Calories',color='purple',size='10')
ax[3].plot(df['Calories'],color='purple',marker='o',markersize=2,linewidth=0.5,label='Calories')
ax[3].set_xlabel('series axis',color='purple',size=9)
ax[3].set_ylabel('Calories',color='purple',size=9)
ax[3].legend(loc='upper right')

plt.show()
