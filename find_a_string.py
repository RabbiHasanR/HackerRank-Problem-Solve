def count_substring(string, sub_string):
    count=0
    result=[]
    list_sub_string=list(sub_string)
    for i in range(len(string)):
        result.append(string[i])
        if len(result)==len(list_sub_string):
            string_result = ''.join(result)
            if string_result == sub_string:
                count += 1
                result.pop(0)
            else:
                result.pop(0)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)