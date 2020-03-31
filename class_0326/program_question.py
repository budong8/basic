# __author : 12265
# date: 2020/3/31


"""
1、对输入的整数数组，输出数组元素中的最大值、最大值的个数、最小值和最小值的个数
函数名称：max_and_min(list)
输入参数：list 整数数组
输出：list 整数数组，有四个值，分别表示最大值、最大值的个数、最小值和最小值的个数
示例：max_and_min([1,4,21,5,6,7,1,1])  =>  [21,1,1,3]
max_and_min([1])  =>  [1,1,1,1]
"""
import logging

logging.basicConfig(level=logging.INFO)


# 输出新的列表，列表有4个值，列表中的最大值，最大值个数，列表中的最小值、列表中最小值的个数
def max_and_min(mylist):
    max_list = max(mylist)
    min_list = min(mylist)
    max_count = 0
    min_count = 0
    for value in mylist:
        if value == max_list:
            max_count += 1
        elif value == min_list:
            min_count += 1
    return [max_list, max_count, min_list, min_count]


if __name__ == '__main__':
    logging.info(max_and_min([23, 45, 66, 66, 12, 66, 1, 3, 2, 2, 2, 2]))
