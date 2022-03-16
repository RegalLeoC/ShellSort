def shell_sort(list):
    inter = len(list) // 2
    inter = int(inter)
    while inter > 0:
        i = 0
        j = inter
        while j < len(list):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
            i = i + 1
            j = i + 1
        while i - inter != -1:
            if list[i - inter] > list[i]:
                list[i-inter], list[i] = list[i], list[i-inter]
            i = i - 1
        inter = inter // 2
        inter = int(inter)
    return list

