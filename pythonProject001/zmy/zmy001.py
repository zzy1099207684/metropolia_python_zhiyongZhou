import pandas as pd
import matplotlib.pyplot as plt

path = './x.csv';
file = pd.read_csv(path);
varList = [];
resList = [];
for i in range(file.shape[1]):
    val = file.iloc[:, i]
    data = {'values': list(val)}
    df = pd.DataFrame(data)
    variance = df['values'].var()
    tempDict = {'name': variance, 'dataSet':val}
    resList.append(tempDict)
    varList.append(variance)
varList.sort(reverse=True)
biggest = varList[0];
secondBig = varList[1];
biggestList = [];
secondBigList = [];
for i in resList:
    if(i.get('name') == biggest ):
        biggestList = i.get('dataSet')
    elif(i.get('name') == secondBig ):
        secondBigList = i.get('dataSet')


plt.scatter(list(biggestList), list(secondBigList), label='assignment', color='b', marker='o')
plt.grid(True)
plt.xlabel('x-biggestList', fontsize = 14)
plt.ylabel('y-secondBigList', fontsize = 14)
plt.legend()
plt.show()


