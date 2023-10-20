def statisWords(tx):
    resultDic = {};
    tx = tx.replace(' ', '').upper();

    resultDic = statisticsNum(tx);
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    dcList = list(resultDic.keys())
    for i in words:
        if i not in dcList:
            resultDic[i] = 0;
    return sorted(resultDic.items());

def statisPariWords(tx):
    tx = tx.replace(' ', '').upper();
    tempList = [];
    for i in range(len(tx)-1):
        tempList.append(tx[i:i+2])
    resultDic = statisticsNum(tempList);
    return resultDic;

def statisticsNum(tx):
    resultDic = {};
    for i in tx:
        if i not in resultDic:
            resultDic[i] = 1;
        else:
            resultDic[i] = resultDic.get(i) + 1;
    return resultDic;


print(statisWords('abc'))
print(statisPariWords('abcdefg'))
