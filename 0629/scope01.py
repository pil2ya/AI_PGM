# # vartest_global.py
# a = 1 
# def vartest(): 
#     global a 
#     a = a+1

# a = vartest() 
# print(a)

def add(a, b):
    """
    두 수를 더하는 함수
    """
    return a + b     
# add = lambda a, b: a + b 이렇게도 가능

result = add(5, 3)
print(result)   # output: 8

print(add.__doc__)  # add 변수를 정의해놓은 docstring을 출력함.

