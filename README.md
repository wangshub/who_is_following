# github 用户 followers 分析

**如何分析一个github用户的followers？**

周末手痒，用python分析了一下自己 [github](https://github.com/wangshub) 的 **followers** 用户，统计结果如下

## 问题分析

在github上，一个用户的主页显示如下，主要对如下用户信息进行提取
- 用户名称
- 所在的位置
- 用户仓库、stars、Followers、Following数量
- 去年一年的贡献度

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngknl9cckj20uh0g6wfm.jpg)

我们需要对上图红框里面的数据进行提取，最直接的方法是使用`requests`，通过`BeautifulSoup`对`html`中的信息进行提取。

## 一些弯路

最开始没打算用爬虫的方式来获取用户信息，因为github有公开的[REST API v3](https://developer.github.com/v3/)可以对指定用户的信息进行访问，并且已经有打包好的[PyGithub](https://github.com/PyGithub/PyGithub)方便调用。但是我实验下来有如下问题所以放弃使用[REST API v3](https://developer.github.com/v3/)
1. API请求频率有限制，无法运用多线程快速获取批量的用户信息
2. 不知道是不是小BUG，通过API无法获得用户去年一年的贡献度**contributions**

## 工具

- **python 3** ： 彻底告别我的py2
- **BeaufulSoup** ：从HTML或XML文件中提取数据
- **Requests** ： 请求网页
- **多进程** ： 为了更快
- **pyecharts** ： 美的令人窒息的绘图工具

## 操作步骤

1. 获取目标用户如`https://github.com/wangshub?page=1&tab=followers`的所有followers；
2. 改变`page`编号，便利所有用户；
3. 提取用户关键信息，保存成`csv`文件；
4. 数据清洗，过滤；
5. 利用[pyecharts](https://github.com/pyecharts/pyecharts)绘图；
6. 进行地点词频统计； 

## 实验结果

截止`2018-01-15`,我的github账号一共有`1214`名follower，分析结果如下

### 用户地点分析

排除掉没有填写地点信息的用户，将中文转化成pinyin后，词云如下

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngljy93kjj20rs0nwtdv.jpg)

用户基本上都是来自`北京、上海、深圳`等地

### 去年一年用户贡献度分析

如果看用户是否活跃，肯定是看`contributions`啦

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngln8yfgij20m80b4t94.jpg)

可以看出超过一般多的用户，去年的贡献度都在都在 **1~50** 之间，新的一年要加油啦。其中一年贡献最多的用户是[@dragon-yuan](https://github.com/dragon-yuan), 在2017年有整整 **4,197** 个贡献度，不多说了，前去关注一波。

### 用户followers分析

哇，有大牛，别拦着我，我要去点关注了

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngmed2kovj20m80b474m.jpg)

### 用户仓库数量分析

通过爬取用户的仓库数量，进行统计如下
![](https://ws1.sinaimg.cn/large/c3a916a7gy1fnglp9onenj20m80b4jrs.jpg)

可以看到一个有意思的现象，有少数的人仓库数量超过了**1000**，打开这几位仁兄的github主页，大部分是fork的项目，其中仓库最多的用户有**13100个**仓库，叫[@ProgrammerAndHacker](https://github.com/ProgrammerAndHacker)，他是这么介绍自己的
```
I follow best programmer and hacker， 
Do you want to hacked by them? ^_^ 
Best programmers and hackers are here: 
...
```

### 用户stars分析

都说点击star是一个好习惯，

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngm1vx9oij20m80b4dg8.jpg)

不得不说，github上面还是有点赞狂魔的，这位老铁[@chenruibin](https://github.com/chenruibin)一共点击了`10100`个赞，真是好习惯～

### 用户 following 分析

![](https://ws1.sinaimg.cn/large/c3a916a7gy1fngm814cbgj20m80b43yw.jpg)

同样是[@ProgrammerAndHacker](https://github.com/ProgrammerAndHacker)这位仁兄，一共follow了**19600**个用户，严重怀疑是不是机器人。

## 最后

不搞了，我要去写论文了TAT，要代码的，来这里自己找