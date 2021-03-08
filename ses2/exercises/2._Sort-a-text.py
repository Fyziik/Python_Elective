def sort_a_text(str):
    tmpList = list(str)
    index = 0
    for char in tmpList:
        if char in "aeiouAEIOU":
            tmpList.pop(index)
        index = index + 1
    
    return sorted(tmpList)


print(sort_a_text("Dette er en test"))