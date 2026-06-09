str = input()

ptr = input()

cnt = 0

for i in range(len(str)):
    flag = 0
    for j in range(len(ptr)):
         if i + j < len(str):
             if str[i+j] != ptr[j]:
                 flag = 1
                 
         if i + j > len(str):
             flag = 1        
                 
    if flag == 0:
        cnt += 1
 
        
print(cnt)
