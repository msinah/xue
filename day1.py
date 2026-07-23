



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

#函数就是解决这个问题的：把重复逻辑装进一个盒子，起个名字，以后直接喊名字就行。
