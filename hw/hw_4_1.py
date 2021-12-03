
purchase = []
key = input()
key = key.split(' ')
read = True
key_len = [ len(s) for s in key ]
max_len = max(key_len)
min_len = min(key_len)
# print(key, 'cute' in key)
while(read):
    
    line = input()
    if line == 'end':
        break
    
    i = 0
    while(i < len(line)-min_len+1):
        # print(i)
        for j in range(max_len, min_len-1, -1):
            
            if i + j > len(line) :
                continue
            # print(i)
            # print(line[i:i + j])
            if line[i:i + j] in key:
                line = line[:i] + '「' + line[i:i+j] + '」' + line[i+j:]
                i = i + j + 1
                break
        i += 1
    print(line)
