# 1. Python数据类型

- 可以通过在类内定义```__getitem__```方法，使用python的切片特性，并且可以直接迭代
- 可以使用```collections.namedtuple```快速构建类型
- 如果一个集合类型没有实现```__contains__```方法，in操作会按顺序进行一次迭代搜索
