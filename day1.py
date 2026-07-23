



#2026-07-23

test_cases = ["用例1", "用例2", "用例3"]
for case in test_cases:
    print("正在执行:", case)
    



# Day 1 作业：测试用例统计器
# 给你一个用例列表，统计其中包含"失败"的有几个

test_results = ["通过", "失败", "通过", "失败","失败","失败", "失败", "通过", "通过"]
fail_count = 0

for result in test_results:
    if result == "失败":
        fail_count = fail_count + 1

print("总用例数:", len(test_results))
print("失败用例数:", fail_count)
print("通过率:", (len(test_results) - fail_count) / len(test_results) * 100, "%")


# 先看一眼，不用完全理解
def run_test(case_name):
    print("执行用例:", case_name)
    return "通过"

result = run_test("登录测试")
print(result)



#函数就是解决这个问题的：把重复逻辑装进一个盒子，起个名字，以后直接喊名字就行。
# 如果想对三批不同的用例统计失败数，代码会变成这样：
#第一批
test_results_1 =["通过", "失败", "通过"]
fail_count = 0
for r in test_results_1:
    if r == "失败":
        fail_count = fail_count + 1
print("第一批用例失败数:", fail_count)

#第二批，几乎一模一样的代码又写一遍
test_results_2 =["通过", "失败", "失败"]
fail_count = 0
for r in test_results_2:
    if r == "失败":
        fail_count = fail_count + 1
print("第二批用例失败数:", fail_count)

#第三批
test_results_3 =["通过", "通过", "失败"]
fail_count = 0
for r in test_results_3:
    if r == "失败":
        fail_count = fail_count + 1
print("第三批用例失败数:", fail_count)

#第四批
test_results_4 =["通过", "失败", "失败"]
fail_count = 0
for r in test_results_4:
    if r == "失败":
        fail_count = fail_count + 1
print("第四批用例失败数:", fail_count)



#函数的定义与调用
# 定义函数：def 函数名(参数):
def count_fail(results):
    fail = 0
    for r in results:
        if r == "失败":
            fail = fail +1
            return fail        #return 把结果"扔出来"

#调用函数
bugs_1 = ["通过", "失败", "通过","失败"]
bugs_2 = ["失败", "失败", "失败"]
bugs_3 = ["通过", "通过", "通过"]

print("批次1失败数:",count_fail(bugs_1))
print("批次2失败数:",count_fail(bugs_2))
print("批次3失败数:",count_fail(bugs_3))

#默认参数（不传就用默认值）
def run_test(case_name,retry=2):
    for i in range(1,retry+1):
        print(f"第{i}次执行:{case_name}")
    print("---")
    
run_test("登录测试")                # 没传 retry，默认重试 2 次
run_test("支付测试",retry=5)        # 传了就用 5 次

#多个参数
def assert_eaqual(actual,expected):
    if actual == expected:
        print("PASS")
    else:
        print(f"FAIL,期望{expected},实际{actual}") 

assert_eaqual(100,100)
assert_eaqual("abc","ABC")
assert_eaqual([1,2,3],[1,2,3])

#函数的作用域（别踩坑）,记住一句话：函数里定义的变量只活在函数里，出去了就不认。
x = 10   # 全局变量

def change():
    x = 5   # 这是函数内部的局部变量，和外边的 x 是两个东西
    print("函数内:", x)

change()
print("函数外:", x)   # 还是 10，没变