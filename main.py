def compareStrings(str1, str2):
    a = len(str1)
    b = len(str2)
    #length not equal then one to one not possible
    if a != b:
        return False

    current =[]
    for i in range(len(str1)):
        current.append((str1[i], str2[i]))

        #checking for same strings in string 1 as they should not be mapped to different items
        #one to one matching

    for i in range(len(str1)-1):
        for j in range(len(str1) - 1):
            if current[i][0] == current[j+1][0]:
                if current[i][1] != current[j+1][1]:
                    return False
    return True

#get argument from the console
a = sys.argv[1]
b = sys.argv[2]
result = compareStrings(a, b)
print(result)
