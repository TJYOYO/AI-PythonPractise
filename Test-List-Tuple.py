# Python 中最常见的两种数据结构：列表（list）和元组（tuple）。
# 列表list是动态的，[], 长度大小不固定，可以随意地增加、删减或者改变元素（mutable）。
# 而元组tuple是静态的，(), 长度大小固定，无法增加删减或者改变（immutable）。
#

l = [1, 2, 'hello', 'world']  # 列表中同时含有int和string类型的元素
print(l)

tup = ('jason', 22)  # 元组中同时含有int和string类型的元素
print(tup)

print(l[1:3])  # 返回列表中索引从1到2的子列表

print(tup[1:3])  # 返回元组中索引从1到2的子元组

# Python 中的列表和元组都支持负数索引，-1 表示最后一个元素，-2 表示倒数第二个元素，以此类推。
print(l[-1])

# 列表和元组都可以随意嵌套
l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表

tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一个元组


# 两者也可以通过 list() 和 tuple() 函数相互转换
list((1, 2, 3))
[1, 2, 3]

tuple([1, 2, 3])
(1, 2, 3)

# build-in function
# count(item) 表示统计列表 / 元组中 item 出现的次数。
# index(item) 表示返回列表 / 元组中 item 第一次出现的索引。
# list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。
# reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，reversed() 返回一个倒转后的迭代器（上文例子使用 list() 函数再将其转换为列表）；
# sorted() 返回排好序的新列表。
l = [3, 2, 3, 7, 8, 1]
l.count(3)
2
l.index(7)
3
l.reverse()
l
[1, 8, 7, 3, 2, 3]
l.sort()
l
[1, 2, 3, 3, 7, 8]

tup = (3, 2, 3, 7, 8, 1)
tup.count(3)
2
tup.index(7)
3
list(reversed(tup))
[1, 8, 7, 3, 2, 3]
sorted(tup)
[1, 2, 3, 3, 7, 8]

# 存储方式的差异
# 为了减小每次增加 / 删减操作时空间分配的开销，Python 每次分配空间时都会额外多分配一些，这样的机制（over-allocating）保证了其操作的高效性：增加 / 删除的时间复杂度均为 O(1)。
l = [1, 2, 3]
print(f"size = {l.__sizeof__()}")
tup = (1, 2, 3)
print(tup.__sizeof__())



