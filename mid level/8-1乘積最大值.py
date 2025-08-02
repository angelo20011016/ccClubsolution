#對數字排序
c = input()
d = c.split(" ")
d = [int(i) for i in d]
null_list = []
for x in range(len(d)-1):
    null_list.append(d[x]*d[x+1])
print(max(null_list))


    


# print(sorted(c))
# #可能情況 都是正的 
# print(c[-1]*c[-2])
# #有正有負 -3 1 4 7 =28 -7 -4 -3 1

# #都是負的

