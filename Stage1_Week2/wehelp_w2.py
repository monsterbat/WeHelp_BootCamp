"""
WeHelp BootCamp Assignemt - Week 2
Release date: 2022/09/26
Authored by SC Siao
"""


# Question 1

def calculate(min, max, step):
    sum=range(min,max+1,step)
    # print(sum)
    
    summary=0
    for s in sum:
        summary=summary+s
    print(summary)

print("Question 1")
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

# Question 2
def avg(data):
    salary_calculator=data["employees"]
    member_quantity=len(salary_calculator)
    member_count=[0]
    count=1
    while len(member_count)<member_quantity:
        member_count=member_count+[count]
        count=count+1


    salary_sum=0
    manager_filter_list_num=0
    for employees_data in member_count:
        all=salary_calculator[employees_data]
        # print(all)
        manager_filter=all["manager"]
        salary_filter=all["salary"]
        if manager_filter==False:
            salary_sum=salary_sum+salary_filter
            manager_filter_list_num=manager_filter_list_num+1


    salary_avg=salary_sum/manager_filter_list_num
    print("Question 2")
    print(salary_avg)

avg({
    "employees":[{
        "name":"John",
        "salary":30000,
        "manager":False
    },
    {
        "name":"Bob",
        "salary":60000,
        "manager":True
    },{
        "name":"Jenny",
        "salary":50000,
        "manager":False
    },{
        "name":"Tony",
        "salary":40000,
        "manager":False
    }]

})

# Question 3
def func(a):
    def _func(b,c):
        calculate=a+(b*c)
        # return calculate
        print(calculate)
    return _func
print("Question 3")    
# 請用你的程式補完這個函式的區塊
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# Question 4
# def maxProduct(nums):
#     first_num=max(nums)
#     nums.remove(first_num)
#     second_num=max(nums)
#     result=first_num*second_num
#     print(result)
def maxProduct(nums):
    multiply_list=[]
    
    for nums_ls1 in nums:
        for nums_ls2 in nums:
            if nums_ls1==nums_ls2:
                continue
            else:
                multiply_list=multiply_list+[nums_ls1*nums_ls2]
    # print(multiply_list)
    multi_ls=[]
    for multi in set(nums):
        if nums.count(multi)>1:
            multi_ls.append(multi)
    # print(multi_ls)
    for multi_multiply in multi_ls:
        multi_items=multi_multiply*multi_multiply
        print(multi_items)
        multiply_list.append(multi_items)
    result=max(multiply_list)
    print(result)
#
print("Question 4")
maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10

# Question 5
def twoSum(nums, target):
    nums_1_result=-1
    nums_2_result=-1
    for nums_1 in nums:
        nums_1_result=nums_1_result+1
        for nums_2 in nums:
            nums_2_result=nums_2_result+1
            target_cal=nums_1+nums_2
            result=[nums_1_result,nums_2_result]
            if target==target_cal:
                return result
print("Question 5")   
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# Question 6
def maxZeros(nums):
    zero_count=0
    nums_count=[]
    for nums_ls in nums:
        if nums_ls==0:
            zero_count=zero_count+1
        else:
            nums_count=nums_count+[zero_count]
            zero_count=0
    nums_count=nums_count+[zero_count]
    print(max(nums_count))
print("Question 6")   
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3