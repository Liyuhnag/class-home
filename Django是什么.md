## Django是什么

Django的官网：https://www.djangoproject.com/

Django 是一个高级 Python Web 框架，鼓励快速开发和简洁、务实的设计。由经验丰富的开发者打造，它解决了网页开发的大部分麻烦，让你可以专注于写应用，无需重新发明轮子。

## Django的安装以及第一个项目

1. 使用`uv init --python 3.11.10`  创建uv环境
2. 下载django `uv add django`
3. 进入虚拟环境 `.venv\Scripts\activate`
4. 使用如下命令创建一个名叫`blog_project`的项目
5. 输入`python manage.py runserver` 运行服务器启动测试

![Install worked!](https://pythondjango.cn/django/basics/2-installation-use.assets/install_worked.png)

## Django的MTV设计模式

### 经典的MVC设计模式及其优点

MVC即 Model-View-Controller(模型-视图-控制器) ，是经典的软件开发设计模式。

- **Model (模型) **： 简而言之即数据模型。模型不是数据本身（比如数据库里的数据），而是抽象的描述数据的构成和逻辑关系。通常模型包括了数据表的各个字段（比如人的年龄和出生日期）和相互关系（单对单，单对多关系等)。Web开发框架会根据模型的定义来自动生成数据表。
- **View (视图)**： 主要用于显示数据，用来展示用户可以看到的内容或提供用户可以输入或操作的界面。数据来源于哪里？当然是数据库啦。那么用户输入的数据给谁? 当然是给控制器啦。
- **Controller(控制器)**：应用程序中处理用户交互的部分。通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据（比如增加或更新数据表）。

如果把MVC比喻成一个粽子，那么View就是最外面一层的绿色玉米叶，是吃货们可以直接看到的。Controller就是中间那层熟糯米，而粽子的核心自然是最里面那一层的肉馅Model模型了。现在大家知道中学和大学数学建模的重要性了吧?

MVC最大的优点是实现了软件或网络应用开发过程中数据、业务逻辑和用户界面的分离，使软件开发更清晰，也是维护变得更容易。这与静态网页设计中使用html和css实现了内容和样式的分离是同一个道理。

### Django如何遵循MVC设计模式的

Django的MVT设计模式由Model(模型), View(视图) 和Template(模板)三部分组成，分别对应单个app目录下的models.py, views.py和templates文件夹。它们看似与MVC设计模式不太一致，其实本质是相同的。Django的MVT设计模式与经典的MVC对应关系如下。

- **Django Model(模型)**: 这个与经典MVC模式下的模型Model差不多。
- **Django View(视图)**: 这个与MVC下的控制器Controller更像。视图不仅负责根据用户请求从数据库读取数据、指定向用户展示数据的方式(网页或json数据), 还可以指定渲染模板并处理用户提交的数据。
- **Django Template(模板)**: 这个与经典MVC模式下的视图View一致。模板用来呈现Django view传来的数据，也决定了用户界面的外观。Template里面也包含了表单，可以用来搜集用户的输入内容。

Django MVT设计模式中最重要的是视图(view), 因为它同时与模型(model)和模板(templates)进行交互。当用户发来一个请求(request)时，Django会对请求头信息进行解析，解析出用户需要访问的url地址，然后根据路由urls.py中的定义的对应关系把请求转发到相应的视图处理。视图会从数据库读取需要的数据，指定渲染模板，最后返回响应数据。这个过程如下图所示：

![Django-2](https://pythondjango.cn/django/basics/2-installation-use.assets/Django-2.png)

## Django模型

Model (模型) 简而言之即数据模型，是一个Django应用的核心。模型不是数据本身（比如数据表里的数据), 而是抽象的描述数据的构成和逻辑关系。

每个Django的模型(model)实际上是个类，继承了`models.Model`。每个Model应该包括属性(字段)，关系（比如单对单，单对多和多对多)和方法。当你定义好Model模型后，Django的接口会自动帮你在数据库生成相应的数据表(table)。这样你就不用自己用SQL语言创建表格或在数据库里操作创建表格了，是不是很省心？

### 模型的组成

一个标准的Django模型分别由模型字段、META选项和方法三部分组成。我们接下来对各部分进行详细介绍。Django官方编码规范建议按如下方式排列：

- 定义的模型字段：包括基础字段和关系字段
- 自定义的Manager方法：改变模型
- `class Meta选项`: 包括排序、索引等等(可选)。
- `def __str__()`：定义单个模型实例对象的名字(可选)。
- `def save()`：重写save方法(可选)。
- `def get_absolute_url()`：为单个模型实例对象生成独一无二的url(可选)
- 其它自定义的方法。

#### 模型的字段

`models.Model`提供的常用模型字段包括基础字段和关系字段。

##### 基础字段

**CharField() **

一般需要通过max_length = xxx 设置最大字符长度。如不是必填项，可设置blank = True和default = ''。如果用于username, 想使其唯一，可以设置`unique = True`。如果有choice选项，可以设置 choices = XXX_CHOICES

**TextField() **

适合大量文本，max_length = xxx选项可选。

**DateField() 和DateTimeField() **

可通过default=xx选项设置默认日期和时间。

- 对于DateTimeField: default=timezone.now - 先要`from django.utils import timezone`
- 如果希望自动记录一次修改日期(modified)，可以设置: `auto_now=True`
- 如果希望自动记录创建日期(created),可以设置`auto_now_add=True`

**EmailField() **

如不是必填项，可设置blank = True和default = '。一般Email用于用户名应该是唯一的，建议设置unique = True

**IntegerField(), SlugField(), URLField()，BooleanField()**

可以设置blank = True or null = True。对于BooleanField一般建议设置`defaut = True or False`

**FileField(upload_to=None, max_length=100) - 文件字段 **

- upload_to = "/some folder/"：上传文件夹路径
- max_length = xxxx：文件最大长度

**ImageField (upload_to=None, max_length=100,)- 图片字段 **

- upload_to = "/some folder/": 指定上传图片路径

##### 关系字段

**OneToOneField(to, on_delete=xxx, options) - 单对单关系**

- to必需指向其他模型，比如 Book or 'self' .
- 必需指定`on_delete`选项(删除选项): i.e, "`on_delete = models.CASCADE`" or "`on_delete = models.SET_NULL`" .
- 可以设置 "`related_name = xxx`" 便于反向查询。

**ForeignKey(to, on_delete=xxx, options) - 单对多关系**

- to必需指向其他模型，比如 Book or 'self' .
- 必需指定`on_delete`选项(删除选项): i.e, "`on_delete = models.CASCADE`" or "`on_delete = models.SET_NULL`" .
- 可以设置"default = xxx" or "null = True" ;
- 如果有必要，可以设置 "`limit_choices_to =` ",
- 可以设置 "`related_name = xxx`" 便于反向查询。

**ManyToManyField(to, options) - 多对多关系**

- to 必需指向其他模型，比如 User or 'self' .
- 设置 "`symmetrical = False` " 表示多对多关系不是对称的，比如A关注B不代表B关注A
- 设置 "`through = 'intermediary model'` " 如果需要建立中间模型来搜集更多信息。
- 可以设置 "`related_name = xxx`" 便于反向查询。

示例：一个人加入多个组，一个组包含多个人，我们需要额外的中间模型记录加入日期和理由。

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

对于`OneToOneField`和`ForeignKey`, `on_delete`选项和`related_name`是两个非常重要的设置，前者决定了了关联外键删除方式，后者决定了模型反向查询的名字。

##### on_delete删除选项

Django提供了如下几种关联外键删除选项, 可以根据实际需求使用。

- `CASCADE`：级联删除。当你删除publisher记录时，与之关联的所有 book 都会被删除。
- `PROTECT`: 保护模式。如果有外键关联，就不允许删除，删除的时候会抛出ProtectedError错误，除非先把关联了外键的记录删除掉。例如想要删除publisher，那你要把所有关联了该publisher的book全部删除才可能删publisher。
- `SET_NULL`: 置空模式。删除的时候，外键字段会被设置为空。删除publisher后，book 记录里面的publisher_id 就置为null了。
- `SET_DEFAULT`: 置默认值，删除的时候，外键字段设置为默认值。
- `SET()`: 自定义一个值。
- `DO_NOTHING`：什么也不做。删除不报任何错，外键值依然保留，但是无法用这个外键去做查询。

##### related_name选项

`related_name`用于设置模型反向查询的名字，非常有用。在文初的`Publisher`和`Book`模型里，我们可以通过`book.publisher`获取每本书的出版商信息，这是因为`Book`模型里有`publisher`这个字段。但是`Publisher`模型里并没有`book`这个字段，那么我们如何通过出版商反查其出版的所有书籍信息呢？

Django对于关联字段默认使用`模型名_set`进行反查，即通过`publisher.book_set.all`查询。但是`book_set`并不是一个很友好的名字，我们更希望通过`publisher.books`获取一个出版社已出版的所有书籍信息，这时我们就要修改我们的模型了，将`related_name`设为`books`, 如下所示：

```python
# models.py
from django.db import models
 
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
 
    def __str__(self):
        return self.name

# 将related_name设置为books
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher,on_delete=models.CASCADE, related_name='books')
    add_date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.name
```

我们再来对比一下如何通过publisher查询其出版的所有书籍，你觉得哪个更好呢?

1. 设置`related_name`前：`publisher.book_set.all`
2. 设置`related_name`后：`publisher.books.all`

#### 模型的META选项

- `abstract=True`: 指定该模型为抽象模型
- `proxy=True`: 指定该模型为代理模型
- `verbose_name=xxx`和`verbose_name_plural=xxx`: 为模型设置便于人类阅读的别名
- `db_table= xxx`: 自定义数据表名
- `odering=['-pub-date']`: 自定义按哪个字段排序，`-`代表逆序
- `permissions=[]`: 为模型自定义权限
- `managed=False`: 默认为True，如果为False，Django不会为这个模型生成数据表
- `indexes=[]`: 为数据表设置索引，对于频繁查询的字段，建议设置索引
- `constraints=`: 给数据库中的数据表增加约束。

#### 模型的方法

##### 标准方法

以下三个方法是Django模型自带的三个标准方法：

- `def __str__()`：给单个模型对象实例设置人为可读的名字(可选)。
- `def save()`：重写save方法(可选)。
- `def get_absolute_url()`：为单个模型实例对象生成独一无二的url(可选)
