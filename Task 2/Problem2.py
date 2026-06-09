text = input()

k = int(input())

mx = 0

ans = []

for i in range(len(text) - k + 1):
    ptr = text[i:i+k]
    cnt = 0
    for j in range(len(text) - k + 1):
        flag = 0
        for t in range(k):
            if text [j+t] != ptr[t]:
                flag = 1
                
        if flag == 0:
            cnt += 1
            
    if cnt > mx:
         mx = cnt
         ans = [ptr]    
    elif cnt == mx and ptr not in ans:
         ans.append(ptr)                   

for x in ans:
    print(x, end=" ")
