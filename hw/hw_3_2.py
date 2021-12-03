def func(l1, l2):
    i = 0
    j = 0
    sorted_lst = []
    while i != len(l1) and j != len(l2):
        if l1[i] > l2[j]:
            sorted_lst.append(l2[j])
            j+=1
        else:
            sorted_lst.append(l1[i])
            i+=1
    if i == len(l1):
        while j != len(l2):
            sorted_lst.append(l2[j])
            j +=1
    if j == len(l2):
        while i != len(l1):
            sorted_lst.append(l1[i])
            i +=1
    return sorted_lst