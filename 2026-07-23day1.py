





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
