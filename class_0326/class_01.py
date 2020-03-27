# 冒泡排序算法


def bubble(mylist):
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
        print(f"第{i}次运行结果为{mylist}")
    return mylist


if __name__ == '__main__':
    mylist = [23, 56, 3, 5, 99, 88, 42]
    print(bubble(mylist))
