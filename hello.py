num=int(input("請輸入一個大於1的正整數:"))
print("=== 輸出如下 ===")

list2=[]

for i in range(2,num+1):

    for j in range(2, i):
        if (i % j) == 0:

            break
    else:

        if str(i) == str(i)[::-1]:
            list2.append(i)

count= sum(list2)
#print(list2)除錯用

for i in range(len(list2)):
    if (len(list2) == 1):
        break

    for j in range(0,i+1):
        print( "%-4d" % list2[0],end="")

        if(len(list2)!=1):
            del list2[0]
        else:
            break
    print()

print(count)
