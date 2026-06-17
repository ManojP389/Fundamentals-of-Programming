n = int(input())
arr =[]
for i in range(n):
        arr.append(int(input()))
freq ={}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
a =[]
for key,value in freq.items():
        a.append(key)
    # for i in range(n):
    #     for j in range(n-i-1):
    #         if a[j] > a[j+1]:
    #             temp = a[j]
    #             a[j] = a[j+1]
    #             a[j+1] = temp
a.sort()
print(a)
print(a[-2])