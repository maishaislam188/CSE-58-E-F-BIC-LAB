def frequent_words_with_mismatch(text, k, d):
    
    patterns = {}
    max_cnt = 0
    
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        
        count = 0
        
        for j in range(len(text) - k + 1):
            substring = text[j:j+k]
            
            diff = 0
            for x in range(k):
                if pattern[x] != substring[x]:
                    diff += 1
                    
            if diff <= d:
                count += 1
                
        patterns[pattern] = count
        
        if count > max_cnt:
            max_cnt = count
            
    for pattern in patterns:
        if patterns[pattern] == max_cnt:
            print(pattern, end=" ")
            
text = input("Enter DNA String: ")
k = int(input("Enter k: "))
d = int(input("Enter d: "))

frequent_words_with_mismatch(text, k, d)                                    
        
        
