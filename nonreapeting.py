s = input().strip()
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
arr=[]
for key,value in freq.items():
    if value == 1:
        arr.append(key)

print(arr[0])