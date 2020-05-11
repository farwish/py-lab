##
# list-merge.py
#
# 合并、去重、存在检测
##

a = ['a', 'b', 'c', 1]
b = ['c', 'd', 'e', 2]


# item 合并不去重

c = a + b
print(c)	# ['a', 'b', 'c', 1, 'c', 'd', 'e', 2]

a.extend(b)
print(a)	# ['a', 'b', 'c', 1, 'c', 'd', 'e', 2]

# a[len(a):len(a)] = b
# print(a)


# item 合并去重

d = list(set(a + b)) 	# [1, 2, 'c', 'b', 'e', 'd', 'a']
print(d)


# exists 检测

if 'a' in a:
    print("'a' is in a") 	# 'a' is in a

if 1 in a:
    print("1 is in a") 		# 1 is in a

if '1' in a:
    print("'1' is in a")
else:
    print("'1' is not in a") 	# '1' is not in a
