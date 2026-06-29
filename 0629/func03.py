dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict2 = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
# for key in dict1:
#     print(f"{key}: {dict1[key]}")

# 딕셔너리를 순서대로 출력하는 기본 폼
# for key, value in dict1.items():
#     print(f"{key}: {value}")


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='Charlie', age=35, city='Chicago')