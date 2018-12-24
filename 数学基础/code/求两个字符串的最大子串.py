def get_substring(str1,str2):
    max_sub = ""
    n = len(str1)
    for i in range(n,0,-1):
        print(i,"-----")
        for j in range(0,n-i+1):
            max_sub = str1[j:j+i]
            print(max_sub)
            if max_sub in str2:
                return max_sub
            print(j,j + i)
    return max_sub
str1 = "abcdex"
str2 = "mnabcyz"
print(get_substring(str1,str2)) # "abc"

