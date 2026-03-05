## 课程目标
掌握函数、面向对象、装饰器、异常处理、文件操作
## 课程内容
### 1. 函数
**python与C语言对比**
| 特性 | C 语言 | Python |
|------|--------|--------|
| 返回类型 | 必须声明 `int func()` | 不需要声明 |
| 参数类型 | 必须声明 | 不需要（可选类型注解） |
| 默认参数 | C99 不支持 | ✅ 支持 |
| 可变参数 | `va_list` 复杂 | `*args, **kwargs` 简洁 |
| 返回多值 | 只能返回一个（靠指针模拟） | ✅ 返回元组 |
| 函数作为参数 | 函数指针 | ✅ 一等公民 |

#### 1.1 函数定义
```python
def 函数名(参数1, 参数2=默认值, *args, **kwargs):
    """文档字符串"""
    # 函数体
    return 返回值
```
| 参数类型 | 语法 | 说明 |
|----------|------|------|
| 位置参数 | `def f(a, b)` | 按位置传入 |
| 默认参数 | `def f(a, b=10)` | 可不传，用默认值 |
| `*args` | `def f(*args)` | 接收任意数量位置参数→元组 |
| `**kwargs` | `def f(**kwargs)` | 接收任意数量关键字参数→字典 |
| 仅关键字参数 | `def f(*, key)` | `*` 后的参数必须用关键字传 |

```python
# === 函数定义与调用 ===

def greet(name, greeting="你好"):
    """打招呼函数"""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hello"))
print(greet(greeting="Hi", name="Charlie"))  # 关键字参数
```
```python
# === *args 和 **kwargs ===

def debug_print(*args, **kwargs):
    print(f"  位置参数: {args}")
    print(f"  关键字参数: {kwargs}")

debug_print(1, 2, 3, name="Alice", age=20)
```

```python
# === 返回多个值 ===

def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = analyze([3, 1, 4, 1, 5, 9])
print(f"最小={lo}, 最大={hi}, 平均={avg:.1f}")
```
```python
# === 默认参数陷阱 ===

# ❌ 错误：可变对象作默认参数
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] ← 共享了同一个列表！

# ✅ 正确写法
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_append(1))  # [1]
print(good_append(2))  # [2] ← 每次都是新列表
```
#### 1.2 作用域（LEGB 规则）

Python 查找变量的顺序：

| 作用域 | 说明 |
|--------|------|
| **L** - Local | 函数内部 |
| **E** - Enclosing | 外层嵌套函数 |
| **G** - Global | 模块全局 |
| **B** - Built-in | 内置（`print`, `len` 等） |

```python
# === 作用域 LEGB ===

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(f"inner: {x}")      # local
    inner()
    print(f"outer: {x}")          # enclosing

outer()
print(f"global: {x}")             # global

# global / nonlocal
counter = 0
def increment():
    global counter
    counter += 1

increment()
increment()
print(f"counter = {counter}")
```
#### 1.3 Lambda 与高阶函数

```python
# lambda 参数: 表达式
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")
```
```python
# 常用于排序
students = [("Alice", 90), ("Bob", 78), ("Charlie", 85)]
students.sort(key=lambda s: s[1], reverse=True)
print(f"按成绩排序: {students}")
```
```python
# map / filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"map: {doubled}")
print(f"filter: {evens}")
```
#### 1.4 类型注解
```python
# === 类型注解 ===

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, times: int = 1) -> list[str]:
    return [f"Hello, {name}!"] * times

print(add(1, 2))
print(greet("Alice", 3))
```

### 2. 面向对象
```c
// C: 结构体 + 函数
typedef struct {
    char name[50];
    int age;
} Student;

void greet(Student *s) {
    printf("Hello, %s!", s->name);
}
```

```python
# Python: 类 = 数据 + 方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, {self.name}!")
```

| 概念 | 说明 |
|------|------|
| `__init__` | 构造方法（C 的初始化函数） |
| `self` | 实例自身引用（C 的 `this` 指针） |
| 属性 | `self.xxx`，实例绑定的数据 |
| 方法 | 类内定义的函数，第一个参数是 `self` |

```python
# === 类的定义与实例化 ===

class Student:
    school = "Python大学"  # 类变量（所有实例共享）
    
    def __init__(self, name, age, score=0):
        self.name = name     # 实例变量
        self.age = age
        self.score = score
    
    def introduce(self):
        return f"我是 {self.name}，{self.age} 岁，来自 {self.school}"
    
    def is_passed(self):
        return self.score >= 60

s1 = Student("Alice", 20, 90)
s2 = Student("Bob", 21, 55)

print(s1.introduce())
print(f"{s2.name} 是否及格: {s2.is_passed()}")
```
#### 2.1 封装
Python 用命名约定实现访问控制：`_` 前缀表示私有，`__` 前缀会触发名称改写。
```python
# === 封装与 @property ===

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # 约定私有
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("余额不能为负数")
        self._balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        return self._balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(f"余额: {acc.balance}")
acc.withdraw(200)
print(f"余额: {acc.balance}")

try:
    acc.balance = -100
except ValueError as e:
    print(f"错误: {e}")
```
#### 2.2 继承
```python
# === 继承 ===

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现 speak()")

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 喵喵！"

# 多态
animals = [Dog("旺财"), Cat("咪咪"), Dog("大黄")]
for animal in animals:
    print(f"  {animal.speak()}")

# isinstance 检查
print(f"\nDog 是 Animal? {isinstance(Dog('x'), Animal)}")
```
#### 2.3 多态
```python
# === 多态 ===
# 定义一个基类（父类）
class Animal:
    def speak(self):
        pass

# 定义子类 Dog
class Dog(Animal):
    def speak(self):
        return "汪汪汪"

# 定义子类 Cat
class Cat(Animal):
    def speak(self):
        return "喵喵喵"

# 定义子类 Cow
class Cow(Animal):
    def speak(self):
        return "哞哞哞"

# 这是一个使用多态的函数
# 它不关心传入的对象具体是什么类型，只关心对象是否有 speak() 方法
def animal_sound(animal_obj):
    print(f"{animal_obj.__class__.__name__} 叫声: {animal_obj.speak()}")

# 实例化对象
dog = Dog()
cat = Cat()
cow = Cow()

# 调用同一个函数，传入不同的对象，产生不同的结果
print("----- 多态演示 -----")
animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
```
#### 2.4 魔方方法

| 方法 | 作用 | 触发方式 |
|------|------|----------|
| `__init__` | 构造方法 | `obj = Class()` |
| `__str__` | 字符串表示 | `print(obj)` / `str(obj)` |
| `__repr__` | 调试表示 | 交互式环境直接输入 obj |
| `__len__` | 长度 | `len(obj)` |
| `__eq__` | 相等比较 | `obj1 == obj2` |
| `__add__` | 加法 | `obj1 + obj2` |
| `__getitem__` | 下标访问 | `obj[key]` |
| `__contains__` | 成员判断 | `x in obj` |
```python
# === 魔术方法 ===

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 = {v1}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 == Vector(1,2): {v1 == Vector(1, 2)}")
print(f"|v2| = {abs(v2):.2f}")
```
#### 2.5 类方法与静态方法
| 类型 | 装饰器 | 第一个参数 | 用途 |
|------|--------|-----------|------|
| 实例方法 | 无 | `self` | 操作实例数据 |
| 类方法 | `@classmethod` | `cls` | 操作类数据，工厂方法 |
| 静态方法 | `@staticmethod` | 无 | 工具函数，不依赖实例或类 |
```python
# === 类方法与静态方法 ===

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_str):
        """工厂方法：从字符串创建"""
        y, m, d = map(int, date_str.split("-"))
        return cls(y, m, d)
    
    @staticmethod
    def is_leap_year(year):
        """静态方法：判断闰年"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

d = Date.from_string("2024-03-15")
print(f"日期: {d}")
print(f"2024 是闰年? {Date.is_leap_year(2024)}")
```
### 3.装饰器
> 装饰器 = 接收函数作为参数，返回新函数的高阶函数。
> Django 中大量使用：`@login_required`, `@api_view`, `@cache_page` 等。

### 核心概念

```python
@decorator        # 语法糖
def func():       # 等价于: func = decorator(func)
    pass
```
```python
# === 第一个装饰器 ===

import time
from functools import wraps

def timer(func):
    @wraps(func)  # 保留原函数信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  [{func.__name__}] 耗时: {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

result = slow_sum(1_000_000)
print(f"  结果: {result}")
print(f"  函数名: {slow_sum.__name__}")  # wraps 保留了原名
```
```python
# === 带参数的装饰器 ===

def retry(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  第 {attempt} 次失败: {e}")
                    if attempt == max_retries:
                        raise
        return wrapper
    return decorator

@retry(max_retries=3)
def unreliable():
    import random
    if random.random() < 0.7:
        raise ConnectionError("连接失败")
    return "成功!"

try:
    print(unreliable())
except ConnectionError:
    print("  最终失败")
```
```python
# === 多个装饰器叠加 ===

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

# 执行顺序：bold(italic(greet)) → <b><i>Hello, Alice</i></b>
print(greet("Alice"))
```
**常用内置装饰器**

| 装饰器 | 来源 | 用途 |
|--------|------|------|
| `@property` | 内置 | 属性访问器 |
| `@classmethod` | 内置 | 类方法 |
| `@staticmethod` | 内置 | 静态方法 |
| `@functools.wraps` | functools | 保留被装饰函数信息 |
| `@functools.lru_cache` | functools | 函数结果缓存 |
| `@dataclasses.dataclass` | dataclasses | 自动生成 `__init__` 等 |
### 4. 异常处理 
#### 4.1 try-except-else-finally
```python
try:
    # 可能出错的代码
except 异常类型 as e:
    # 处理异常
else:
    # 没有异常时执行
finally:
    # 无论是否异常都执行（清理资源）
```
| 子句 | 作用 | 是否必须 |
|------|------|----------|
| `try` | 包裹可能出错的代码 | ✅ 必须 |
| `except` | 捕获并处理异常 | ✅ 至少一个 |
| `else` | 无异常时执行 | ❌ 可选 |
| `finally` | 始终执行（清理资源） | ❌ 可选 |

```python
# === try-except 基本用法 ===

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为 0")
        return None
    except TypeError as e:
        print(f"错误：类型不匹配 - {e}")
        return None
    else:
        print(f"计算成功: {a}/{b} = {result}")
        return result
    finally:
        print("  [清理完毕]")

safe_divide(10, 3)
print()
safe_divide(10, 0)
```
#### 4.2 常见异常
| 异常 | 触发场景 | 示例 |
|------|---------|------|
| `ZeroDivisionError` | 除以零 | `1/0` |
| `TypeError` | 类型不匹配 | `'a' + 1` |
| `ValueError` | 值不合法 | `int('abc')` |
| `IndexError` | 索引越界 | `[1,2][5]` |
| `KeyError` | 字典键不存在 | `d['bad']` |
| `FileNotFoundError` | 文件不存在 | `open('xxx')` |
| `AttributeError` | 属性不存在 | `None.x` |
#### 4.3 raise 与自定义异常
```python
# === raise 与自定义异常 ===

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足: 余额 {balance}，尝试取款 {amount}")

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("取款金额必须大于 0")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(1000, 1500)
except InsufficientFundsError as e:
    print(f"错误: {e}")
    print(f"  差额: {e.amount - e.balance}")
```
#### 4.4 最佳实践
| 原则 | 说明 |
|------|------|
| 精确捕获 | 捕获具体异常类型，不要裸 `except:` |
| 最小 try 范围 | `try` 块只包含可能出错的代码 |
| 不要静默吞掉 | `except: pass` 是反模式 |
| EAFP > LBYL | 先做再说（try）优于先检查再做（if） |

### 5. 文件操作
#### 5.1文件打开模式

| 模式 | 说明 | 文件不存在时 |
|------|------|-------------|
| `'r'` | 只读（默认） | 报错 |
| `'w'` | 只写（**清空**文件） | 创建 |
| `'a'` | 追加写入 | 创建 |
| `'x'` | 创建写入（已存在则报错） | 创建 |
| `'b'` | 二进制模式后缀 | `'rb'`, `'wb'` |

> ✅ **始终使用 `with` 语句**，它保证文件会被正确关闭，即使发生异常。

```python
# === 写入与读取 ===

# 写入
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

# 读取（推荐：逐行迭代，内存友好）
with open("demo.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"  行{i}: {line.strip()}")

# 追加
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("追加的第四行\n")

# 一次读取全部
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"\n全部内容:\n{content}")
```

#### 5.2 JSON 文件处理
```python
# === JSON 读写 ===

import json

# 写入 JSON
data = {
    "name": "Alice",
    "age": 20,
    "courses": ["Python", "Math"],
    "graduated": False
}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON
with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"类型: {type(loaded)}")
print(f"姓名: {loaded['name']}, 课程: {loaded['courses']}")
```
#### 5.3CSV 文件处理
```python
import csv

# 写入
students = [["name", "age", "score"], ["Alice", 20, 90], ["Bob", 21, 85]]
with open("students.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(students)

# 用 DictReader 读取
with open("students.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"  {row['name']}, 成绩 {row['score']}")
```
#### 5.4 上下文管理器
```python
# === 自定义上下文管理器 ===

from contextlib import contextmanager
import time

@contextmanager
def timer(name="计时器"):
    start = time.time()
    print(f"[{name}] 开始")
    yield
    print(f"[{name}] 耗时: {time.time() - start:.4f}s")

with timer("求和"):
    total = sum(range(1_000_000))
    print(f"  结果: {total}")
```

### 6.同步与异步编程

| 场景 | 同步（阻塞） | 异步（非阻塞） |
|------|-------------|---------------|
| 下载 3 个文件（每个 2s） | 串行 6s | 并发 ~2s |
| 数据库查询 + API 调用 | 依次等待 | 同时发起 |
| Django 4.x | 传统视图 | `async def view()` |

```
同步：  ──任务A(2s)──任务B(2s)──任务C(2s)──  总计 6s
异步：  ──任务A(等I/O)──
        ──任务B(等I/O)──
        ──任务C(等I/O)──                     总计 ~2s
```

### 核心概念

| 概念 | 说明 |
|------|------|
| 协程 (Coroutine) | `async def` 定义的函数，可以暂停和恢复 |
| `await` | 等待一个异步操作完成，期间让出控制权 |
| 事件循环 (Event Loop) | 调度和执行协程的引擎 |
| `asyncio` | Python 标准异步库 |

```python
# === 同步 vs 异步对比 ===

import asyncio
import time

# 同步版本
def sync_download(name, seconds):
    print(f"  [{name}] 开始下载...")
    time.sleep(seconds)
    print(f"  [{name}] 完成")

start = time.time()
sync_download("文件A", 1)
sync_download("文件B", 1)
sync_download("文件C", 1)
print(f"同步总耗时: {time.time() - start:.1f}s\n")

# 异步版本
async def async_download(name, seconds):
    print(f"  [{name}] 开始下载...")
    await asyncio.sleep(seconds)  # 非阻塞等待
    print(f"  [{name}] 完成")

async def main():
    start = time.time()
    await asyncio.gather(
        async_download("文件A", 1),
        async_download("文件B", 1),
        async_download("文件C", 1),
    )
    print(f"异步总耗时: {time.time() - start:.1f}s")

await main()
```
```python
# === 异步注意事项 ===

import asyncio

# ❌ 常见错误：在异步中用 time.sleep（会阻塞整个事件循环）
# time.sleep(1)  # 阻塞！
# ✅ 正确：用 await asyncio.sleep(1)

# 信号量限流（限制并发数量）
async def limited_download(sem, name, delay):
    async with sem:  # 获取信号量
        print(f"  [{name}] 开始 (并发槽)")
        await asyncio.sleep(delay)
        print(f"  [{name}] 完成")

async def main():
    sem = asyncio.Semaphore(2)  # 最多 2 个并发
    tasks = [limited_download(sem, f"文件{i}", 1) for i in range(5)]
    await asyncio.gather(*tasks)

await main()
```
### 6 并发编程
#### 并发 vs 并行 vs 异步

| 概念 | 说明 | 实现 |
|------|------|------|
| **并发** | 交替执行多个任务 | 多线程 `threading` |
| **并行** | 真正同时执行 | 多进程 `multiprocessing` |
| **异步** | 非阻塞 I/O | `asyncio`（上一节已学） |

#### GIL（全局解释器锁）

| 要点 | 说明 |
|------|------|
| 什么是 GIL | 同一时刻只允许一个线程执行 Python 字节码 |
| 影响 | **CPU 密集型** 多线程无法利用多核 |
| 不影响 | **I/O 密集型**（网络、文件），GIL 在 I/O 等待时释放 |
| 解决 | CPU 密集型 → 多进程；I/O 密集型 → 多线程或异步 |

> Django 主要是 **I/O 密集型**（数据库查询、HTTP 请求），多线程有效。

```python
# === 多线程 ===

import threading
import time

def download(name, seconds):
    print(f"  [{name}] 开始下载...")
    time.sleep(seconds)
    print(f"  [{name}] 完成 ({seconds}s)")

# 顺序执行
start = time.time()
download("文件A", 1)
download("文件B", 2)
print(f"顺序: {time.time() - start:.1f}s\n")

# 多线程并发
start = time.time()
t1 = threading.Thread(target=download, args=("文件A", 1))
t2 = threading.Thread(target=download, args=("文件B", 2))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"多线程: {time.time() - start:.1f}s")
```
#### 6.1 线程池
```python
# === ThreadPoolExecutor ===

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch_url(url, delay):
    time.sleep(delay)
    return f"{url} -> 200 OK ({delay}s)"

urls = [
    ("https://api.example.com/users", 1),
    ("https://api.example.com/posts", 2),
    ("https://api.example.com/comments", 1.5),
    ("https://api.example.com/albums", 0.8),
]

start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_url, url, d): url for url, d in urls}
    for future in as_completed(futures):
        print(f"  {future.result()}")

print(f"\n总耗时: {time.time() - start:.1f}s (顺序需 {sum(d for _, d in urls)}s)")
```
### 7. HTTP与网络请求
#### HTTP 方法

| 方法 | 用途 | Django 对应 |
|------|------|-------------|
| `GET` | 获取资源 | `request.GET` |
| `POST` | 创建资源 | `request.POST` |
| `PUT` | 全量更新 | `request.data` (DRF) |
| `PATCH` | 部分更新 | `request.data` (DRF) |
| `DELETE` | 删除资源 | 删除操作 |

####  常用状态码

| 状态码 | 含义 | Django |
|--------|------|--------|
| `200` | OK | 正常响应 |
| `201` | Created | 创建成功 |
| `301/302` | 重定向 | `redirect()` |
| `400` | Bad Request | 表单验证失败 |
| `401` | Unauthorized | 未登录 |
| `403` | Forbidden | 无权限 |
| `404` | Not Found | `get_object_or_404()` |
| `500` | Server Error | 服务器异常 |
#### 7.1 requests库
```python
# === GET 请求 ===

import requests

response = requests.get("https://httpbin.org/get", params={"name": "Alice", "age": 20})
print(f"状态码: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")
data = response.json()
print(f"参数: {data['args']}")
```
```python
# === POST 请求 ===

import requests

# 发送 JSON
response = requests.post(
    "https://httpbin.org/post",
    json={"username": "alice", "email": "alice@example.com"},
    headers={"Authorization": "Bearer fake-token"}
)
data = response.json()
print(f"发送的数据: {data['json']}")
print(f"Auth: {data['headers'].get('Authorization')}")

# 发送表单
response = requests.post(
    "https://httpbin.org/post",
    data={"username": "alice", "password": "123456"}
)
print(f"表单数据: {response.json()['form']}")
```

```python
# === 错误处理与超时 ===

import requests

# 超时
try:
    response = requests.get("https://httpbin.org/delay/5", timeout=3)
except requests.Timeout:
    print("请求超时！")

# 状态码检查
response = requests.get("https://httpbin.org/status/404")
print(f"状态码: {response.status_code}, 成功? {response.ok}")

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"HTTP 错误: {e}")
```

```python
# === Session（保持登录状态） ===

import requests

session = requests.Session()
session.headers.update({"User-Agent": "MyApp/1.0"})

# 设置 Cookie
session.get("https://httpbin.org/cookies/set/session_id/abc123")

# 后续请求自动携带
response = session.get("https://httpbin.org/cookies")
print(f"Cookies: {response.json()['cookies']}")
session.close()
```

### 8日志系统
#### print vs logging

| 对比 | `print()` | `logging` |
|------|-----------|-----------|
| 级别控制 | ❌ | ✅ DEBUG/INFO/WARNING/ERROR/CRITICAL |
| 输出目标 | 控制台 | 控制台 + 文件 + 网络... |
| 格式化 | 手动 | 自动（时间、文件、行号） |
| Django | ❌ | ✅ `settings.LOGGING` |

| 级别 | 用途 |
|------|------|
| `DEBUG` | 开发调试 |
| `INFO` | 正常运行 |
| `WARNING` | 警告（默认级别） |
| `ERROR` | 错误 |
| `CRITICAL` | 严重错误 |


```python
# === logging 基础 ===

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger("myapp")
logger.debug("调试信息：x = 42")
logger.info("用户 Alice 登录成功")
logger.warning("磁盘使用率 80%")
logger.error("数据库连接失败")
```

```python
# === 在业务代码中使用 ===

import logging

logger = logging.getLogger("myapp.orders")

def process_order(order_id, amount):
    logger.info(f"处理订单 #{order_id}, 金额: {amount}")
    if amount <= 0:
        logger.error(f"订单 #{order_id} 金额无效: {amount}")
        raise ValueError("金额必须大于 0")
    if amount > 10000:
        logger.warning(f"订单 #{order_id} 大额交易: {amount}")
    logger.info(f"订单 #{order_id} 处理完成")

try:
    process_order(1001, 500)
    process_order(1002, 50000)
    process_order(1003, -10)
except ValueError:
    pass
```
### 9. 单元测试
#### 为什么要测试？

| 原因 | 说明 |
|------|------|
| 防止回归 | 修改后自动验证旧功能 |
| 文档作用 | 测试说明了预期行为 |
| 重构信心 | 有测试才敢重构 |
| Django 内置 | `manage.py test` |

#### unittest vs pytest

| 工具 | 风格 | 特点 |
|------|------|------|
| `unittest` | 类 + 方法 | Python 内置，Django 默认 |
| `pytest` | 函数 + assert | 更简洁，社区主流 |

#### 常用断言

| 方法 | 验证 |
|------|------|
| `assertEqual(a, b)` | a == b |
| `assertTrue(x)` / `assertFalse(x)` | 布尔值 |
| `assertIn(a, b)` | a in b |
| `assertIsNone(x)` | x is None |
| `assertRaises(Exc)` | 抛出异常 |
| `assertAlmostEqual(a, b)` | 浮点近似 |

```python
# test_math.py
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3), (-1, -2, -3), (0, 0, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected
```

```bash
pytest test_math.py -v
```