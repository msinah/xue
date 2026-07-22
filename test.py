# # 函数
# def sum(x, y): # 定义函数
#     s = x+y     # 处理过程
#     return s   # 返回结果
# a=1
# b=2
# sum(a,b)

users = {"张三": "123456"}
def reg(username, password):
    if users.get(username): # 如果用户中存在username这个key
        print("用户已存在")
    else:
        users[username] = password # 向users字典中添加元素
        print("添加成功")

def login(username, password):
    if not users.get(username):
        print("用户不存在")
    elif users[username] == password:
        print("登录成功")
    else:
        print("密码错误")

# reg("李四","1")
login("李四","1")


def add(x: (int, float), y: (int, float)) -> (int, float):  # ->指返回值类型
    s = x+y
    return s

add(x=1, y=2)

def add(x, y):
    s = x + y
    d = x - y
    return s, d  # 返回操作结果
    print(d)   
    print(s)   # 不会执行
sum = add(3, 5)
print(sum)  # 打印返回值
sum,diff = add(3, 6)
print(sum,diff)# 打印返回值

def calc(x: int, y: int, type='add'):   # type为计算类型，支持add加，sub减，mul乘，div除，默认为加。
    if type == 'add': 
        return x + y
    if type == 'sub':   # 不需要elif，因为如果满足上个条件，就return终止了。
        return x - y
    if type == 'mul': 
        return x * y
    if type == 'div':
        return x / y   
print(calc(1, 3, 'sub'))

def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def func(x,y):
    sum = add(x,y)  # 调用加法函数
    result = mul(sum, 2)   # 调用乘法函数
    return result

add = lambda x,y: x+y
print(add(3,2))