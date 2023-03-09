# action
import math
import random

print("hello reptile")
print("1\
2\
3")  # 这一个逻辑行书写为三个物理行使用\，输出还是123


# 函数定义 def 函数名（参数）->类型:
def min(a: int, b: int) -> bool:
    return a > b


print(min(1, 2))
print(pow(2, 4))


def nop():
    pass  # pass代表无操作占位符，如果一开始函数功能没有想好，可以用pass代替，即可以让代码先跑起来


# python具有强大的数据类型转化功能
print("int('12'):", int('12'))
print(int(12.3))
print(str(1.23))
print(bool(1))
print(bool(0))
print(bool(''))
# 函数的参数分为可变类型和不可变类型，其调用结果是不同的
# 1.可变类型：类似于c++的引用传递，如列表，字典
# 2.不可变类型，类似c++的值传递，如整数，字符串，元组等
a = [1, 2, 3]
b = a  # python中变量的赋值，其实是地址的赋值，a指向上面对象的地址，将a赋值给b，其实是a和b指向同一块地址，所以，如果改变a，则b也会变,改变b，a也会变
a.append(5)
print(b)
b.append(6)
print(a)


# 默认参数要指向不可变对象，例子在下面
def test_add(a=[]):
    a.append('End')
    return a


print(test_add())  # ['End']
print(test_add())  # ['End','End']
print(test_add())  # ['End','End','End']
# 出现这样的原因是[]是可变参数，刚开始是空值，进行第一次添加后[]的值已经被修改为['End']，所以再执行函数时，是在这个的基础上再加End
# 可以将a指向不可变对象避免这种情况比如a=None
# 高阶函数
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))  # len是一个求长度的函数，该函数可以作为另外一个函数的参数
# 输出结果如下：
# ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
# python六大数据类型
# 1.数字：包含int，complex（复数）,float（浮点数）bool(布尔类型)
# 2.字符串（String）
# 3.列表（List）：[1，2，3]
# 4.字典（Dictionary）：{"name":"poge","age":3}
# 5.元组（Tuple）:(1,'hello',3)
# 6.集合(set):{'a','b','c','d'}
# type查看数据类型
# 当python中多个变量相同时，不是每一个地址存储一个数字，而是只存一个地址，让多个变量指向它
a = 6
b = 6
c = 6
print(id(a), id(b), id(c))  # 地址是相同的
# 如果修改a的值，bc的地址不变，会把a的值重新存一个地址，让a指向它
a = 8
print(id(a), id(b), id(c))
# tips Python具有自动内存管理功能，如果一个值没有任何变量指向，
# 则Python自动将其删除，因此，一般Python程序员不需要太多考虑内存管理的问题
# （这就是Python与C语言最大的区别，自动内存回收机制！），
# 但显式使用del命令删除不再使用的值，仍然是一个优秀程序员需要具备的基本素养
# tips python用and代替&&,or代替||
# 数值运算
"""
//表示整除(向下取整)，取商的整数部分,与c++不同，在python中即使是int除以int，如果除不完的话，还是会显示小数点后面的数
**表示幂"""
print(4 // 3)
print(4 ** 3)
print(math.gcd(3, 4))  # 求最大公约数
print(random.randint(1, 2000))  # 生成1到2000的随机数
"""在字符串中，双引号和单引号没有区别，当字符串为模块字符串时，即占据多行时，使用三引号"""
# raw字符串的格式为r'',专门用来解决转义字符比如f=open('D:\new.txt')，
# \n是换行符，从而不能打开正确的位置，raw字符串所有的字符都是直接按照字面意思来解释的，
# 所以可以用f=open(r'D"\new.txt')代替
# 字符串切片
s = "python"
print(s[0:])
print(s[::-1])  # 字符串逆转
print(s[::2])  # 输出2的倍数下标的字符
print(s[::3])
# 连接字符串
print('py' + 'th' + 'on')
# 修改字符串
S = s.replace('p', 'T')  # 将p修改为C,返回为一个新的字符串
print(S)
print(s)
# List(列表) 变量名=[元素1，元素2,...，元素n]
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 2)
a = ['a', 1]
b = ['b', 2]
x = [a, b]
print(x)
print(x[0][1])  # 相当于二维数组
