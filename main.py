# 这是一个示例 Python 脚本。

# 按 Ctrl+F5 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 F9 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

#元组
#获取元素索引 index()
t=(1,2,3); print(t.index(1))

# 统计元素出现的个数 count()
t = (1, 2, 3, 2, 1, 2, 3)
num = t.count(2)
print(num)

#切片
name = "abcdefg"
print(name[2:5:1]) # cde

list1 = ['小明', 18, 1.71, True]
print(list1[0:2])  # ['小明', 18]
print(name[2:5:2])

#集合
s = {'a', 'b', 'c'}
s = set()  # 创建空集合
s = set(['a', 'b', 'c'])  # 将列表转为集合

#添加元素  add()
s = set(); s.add('a')
print(s)

#更新集合(批量添加多个) update()
s = {'a', 'b'}; s1=set(['b', 'c']); s.update(s1)
print(s)

#字典 get(key, default=None)
d = {'a': 1, 'b': 2, 'c': 3};
print(d.get('a'))

import copy  # 必须导入copy模块
d = {"1": "男", "2": [1, 2, 3]}
# 1. 直接赋值：b和d指向同一个对象（完全引用）
b = d
# 2. 浅拷贝：两种写法效果一样，都只拷贝父对象，不拷贝子对象
# 写法1：字典自带的.copy()方法
c1 = d.copy()
# 写法2：copy模块的copy()方法
c2 = copy.copy(d)
# 测试：修改浅拷贝对象的不可变元素（字符串）
c2["1"] = "dsfsd"
# 测试：修改原对象的可变子元素（列表）
d["2"].remove(1)
# 打印id（内存地址），看对象是不是同一个
print("id(b):", id(b))
print("id(d):", id(d))
print("id(c2):", id(c2))
# 打印字典内容，看修改后谁变了
print("d:", d)
print("b:", b)
print("c2:", c2)


#章节2
age=int(input("今年多大了？"))
#2.判断是否满18岁
#if语句以及缩进部分的代码是一个完整的语法块
if age>=18:
    print("可以进网吧嗨皮……")
else:
    print("你还没长大，应该回家写作业！")
#3.思考！-无论条件是否满足都会执行
    print("这句代码什么时候执行?")

age = -1
# 要求人的年龄在 0-120 之间
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩要求只要有一门成绩 > 60 分就算合格
python_score = 60.0001
c_score = 100
if python_score > 60 or c_score > 60:
    print("你真牛逼")
else:
    print("你是个fw")

#练习3: 定义一个布尔型变量（True\False） is_employee ，编写代码判断是否是本公司员工如果不是提示不允许入内
is_employee = True
# 如果不是提示不允许入内
if not is_employee:
    print("非公勿内")
else:
    print("老板快进")


# 在开发中，使用 if 可以 判断条件，使用 else 可以处理 条件不成立 的情况
# 但是，如果希望 再增加一些条件，条件不同，需要执行的代码也不同 时，就可以使用 elif
# 语法格式如下：
#   if 条件1:
#       条件1满足执行的代码
#   elif 条件2:
#       条件2满足时，执行的代码
#   elif 条件3:
#       条件3满足时，执行的代码
#   else:
#       以上条件都不满足时，执行的代码

# 练习：
# 1. 定义 score 变量记录考试分数
# 2. 如果分数是 大于等于 90分 应该显示 优
# 3. 如果分数是 大于等于 80分 并且 小于 90分 应该显示 良
# 4. 如果分数是 大于等于 70分 并且 小于 80分 应该显示 中
# 5. 如果分数是 大于等于 60分 并且 小于 70分 应该显示 差
# 6. 其它分数显示 不及格
coore = 50
if coore >= 90:
    print("优")
elif coore >= 80 and coore < 90:
    print("良")
elif coore >= 70 and coore < 80:
    print("中")
elif coore >= 60 and coore < 70:
    print("差")
else:
    print("不及格")
# 拓展: score >= 80 and score < 90 可以简化为 80<= score < 90

# 在开发中，使用 if 进行条件判断，如果希望 在条件成立的执行语句中 再 增加条件判断，就可以使用 if 的嵌套
# if 的嵌套的应用场景就是：在之前条件满足的前提下，再增加额外的判断
# if 的嵌套的语法格式，除了缩进之外和之前的没有区别
# 语法格式如下：
# if 条件 1:
#   条件1满足执行的代码
#   if条件1基础上的条件2:
#       条件2满足时，执行的代码
#       #条件2不满足的处理
#   else:
#       条件2不满足时，执行的代码
# #条件1不满足的处理
# else:
#   条件1不满足时，执行的代码\

# 练习：火车站安检
# 1. 定义布尔型变量 has_ticket 表示是否有车票
# 2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 3. 首先检查是否有车票，如果有，才允许进行 安检
# 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 如果超过 20 厘米，提示刀的长度，不允许上车
# 如果不超过 20 厘米，安检通过
# 5. 如果没有车票，不允许进门

has_ticket = False
knife_length = 20.001
if has_ticket:
    if knife_length <20:
        print("上车吧")
    else:
        print("管制道具，禁止上车")
else:
    print("没有车票，禁止上车")


#定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 定义整数型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 201
# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    print("有车票，可以开始安检...")
    # 安检时，需要检查刀的长度，判断是否超过 20 厘米    # 如果超过 20 厘米，提示刀的长度，不允许上车
    if knife_length >= 20:
        print("不允许携带 %d 厘米长的刀上车" % knife_length)
    # 如果不超过 20 厘米，安检通过
    else:
        print("安检通过，祝您旅途愉快……")
# 如果没有车票，不允许进门
else:
    print("大哥，您要先买票啊")



#循环
#1.定义重复次数计数器
i=1
#2.使用while判断条件
while i<=100:
    print("媳妇儿,我错了")
    print(i)
    i=i+1
print("循环结束后的i=%d"%i)

# 计算 0 ~ 100 之间所有数字的累计求和结果
# 0. 定义最终结果的变量
result = 0
# 1. 定义一个整数的变量记录循环的次数
i = 0
# 2. 开始循环
while i <= 100:
    print(i)
# 每一次循环，都让 result 这个变量和 i 这个计数器相加
    result += i
# 处理计数器
    i += 1
print("0~100之间的数字求和结果 = %d" % result)\

# 需求进阶: 计算0~100之间所有 偶数 的累计求和结果
# 开发步骤
# 1. 编写循环 确认 要计算的数字
# 2. 添加 结果 变量，在循环内部 处理计算结果
# 0. 最终结果
result = 0
# 1. 计数器
i = 0
# 2. 开始循环
while i <= 100:
    # 判断偶数
    if i % 2 == 0:
        print(i)
        result += i
    # 处理计数器
    i += 1
print("0~100之间偶数求和结果 = %d" % result)


