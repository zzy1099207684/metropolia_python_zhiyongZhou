# 215x+710y=5
import math


def xunhuan(a, b, list3):
    list = [];
    list2 = [];

    if (0 == b):
        list.append(int(a));
        list.append(int(1));
        list.append(int(b));
        list3.append(list);
        # print(f"{list[0]}, {list[1]}, {list[2]}")
        return list;
    if (0 != b):
        list = xunhuan(b, a % b, list3);
        d = list[0];
        x = list[2];
        y = list[1] - math.floor(a / b) * list[2];
        list2.append(d)
        list2.append(x)
        list2.append(y)
        list3.append(list2);
        # print(f" {list2[0]}, {list2[1]}, {list2[2]}")
        return list2;
    return list3;

a=215;
b=710;
list3 = [];
result = xunhuan(a, b, list3)
list3.reverse();
for i in list3:
    print(i)

