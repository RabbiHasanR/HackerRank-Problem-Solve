def min_window(strArr):
    string=strArr[0]
    pat=strArr[1]
    print(string)
    print(pat)
    curent=[0]*52
    expected=[0]*52
    for char in pat:
        expected[ord(char)-ord('a')]+=1
    i,count,start,min_width,min_start=0,0,0,float('inf'),0

    while i<len(string):
        curent[ord(string[i])-ord('a')]+=1
        if curent[ord(string[i])-ord('a')]<=expected[ord(string[i])-ord('a')]:
            count+=1
        if count==len(pat):
            while expected[ord(string[start])-ord('a')]==0 or curent[ord(string[start])-ord('a')]>expected[ord(string[start])-ord('a')]:
                curent[ord(string[i])-ord('a')]-=1
                start+=1
            if min_width>i-start+1:
                min_width=i-start+1
                min_start=start
        i+=1
    if min_width==float('inf'):
        return ''
    return string[min_start:min_start+min_width]


a=["aaffhkksemckelloe", "fhea"]
print(min_window(a))