# __author : 12265
# date: 2020/3/31


# 位置参数、关键字参数
def welcome(name, hope):
    print(f'Hello {name},欢迎加入python实战圈')
    print(f'{hope}')


# 默认参数
def welcome_default(name, hope='我希望你能坚持下去'):
    print(f'Hello {name},欢迎加入python实战圈')
    print(f'{hope}')


# 可变参数  *接受任意数量的元组   ** 接收字典可变参数
def welcome_tuple(*name, hope='我希望你能坚持下去'):
    print(f'Hello {name},欢迎加入python实战圈')
    print(f'{hope}')


def welcome_dict(first_name, last_name, **employee_info):
    employee = {}
    employee['first_name'] = first_name
    employee['last_name'] = last_name

    for key, value in employee_info.items():
        employee[key] = value
    return employee


def print_line():
    print('-' * 50)


if __name__ == '__main__':
    welcome('bob', '加油')  # 位置参数
    welcome(hope='努力向上', name='Li')  # 关键字参数
    print_line()
    welcome_default('jim')
    print_line()
    welcome_tuple('li', '张三', '李四')
    print_line()
    print(welcome_dict('刘', '德华', location='北京', dep='大数据'))
