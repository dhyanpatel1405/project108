import random
import plotly.express as px
import plotly.figure_factory as ff

count=[]
dice_answer=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_answer.append(dice1+dice2)
    count.append(i)

fig=ff.create_distplot([dice_answer],['👍👍'])
#print(dice1,dice2)
fig.show()