## 定义
my_set = {1,2,3}

## 追加
my_set.add(4)

## 批量追加
my_set.update([5,6,7])

## 删除
my_set.remove(2)

## pop
my_set.pop()

## 清空
my_set.clear()

## list -> set
my_list = [1,2,3,4,5]
my_set = set(my_list)

## 合并(并集)
my_set1 = {1,2,3}
my_set2 = {3,4,5}
my_set1.union(my_set2)

## 交集
my_set1.intersection(my_set2)

## 差集
my_set1.difference(my_set2)

## 子集
my_set1.issubset(my_set2)
