
def minwindow(strArr):
    string=strArr[0]
    pattern=strArr[1]

    length1=len(string)
    length2=len(pattern)

    if length1<length2:
        return ''

    hash_pattern=[0]*256
    hash_string=[0]*256

    for x in range(0,length2):
        hash_pattern[ord(pattern[x])]+=1

    start,start_index,min_len=0,-1,float('inf')

    counter=0
    for b in range(0,length1):
        hash_string[ord(string[b])]+=1

        if hash_pattern[ord(string[b])] !=0 and hash_string[ord(string[b])] <=hash_pattern[ord(string[b])]:
            counter+=1
        if counter==length2:

            while hash_string[ord(string[start])]>hash_pattern[ord(string[start])] or hash_pattern[ord(string[start])]==0:
                if hash_string[ord(string[start])] > hash_pattern[ord(string[start])]:
                    hash_string[ord(string[start])]-=1
                start+=1
            length_win=b-start+1
            if min_len>length_win:
                min_len=length_win
                start_index=start
    if start_index==-1:
        return ''

    return  string[start_index:start_index+min_len]


a=["aaffhkksemckelloe", "fhea"]
print(minwindow(a))