# Day 2 作业：简易测试框架
# 作业1：写一个函数，接收用例名和实际结果、期望结果，返回 "PASS" 或 "FAIL"
def check_result(case_name,actual,expected):
    if actual == expected:
        return f"{case_name}:PASS"
    else:
        return f"{case_name}:FAIL--期望{expected},实际{actual}"
    
    
# 作业2：写一个函数，接收多个用例的结果列表，打印汇总报告
def summary(results):
    total = len(results)
    passed = 0
    for r in results:
        if "PASS" in r:
            passed = passed + 1
    print(f"总计： {total}") 
    print(f"通过: {passed}")
    print(f"失败: {total - passed}")
    
# 作业3：模拟跑一组接口用例
r1 = check_result("登录接口",200,200)
r2 = check_result("下单接口","成功","成功")
r3 = check_result("支付接口",500,200)
r4 = check_result("查询接口",500,200)

results = [r1,r2,r3,r4]
for r in results:
    print(r)
print ("\n---- 汇总报告 ----")
summary(results)
    
