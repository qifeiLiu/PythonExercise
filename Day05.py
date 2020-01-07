#题目：输入三个整数 x,y,z, 请把 这三个数由小到大排列

List_Sort = []
num = int(input("请输入第一个整数:"))
List_Sort.append(num)
num = int(input("请输入第二个整数:"))
List_Sort.append(num)
num = int(input("请输入第三个整数:"))
List_Sort.append(num)
List_Sort.sort()
print(List_Sort)