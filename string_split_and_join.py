def split_and_join(line):
    # write your code here
    split_string=line.split(" ")
    result='-'.join(split_string)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)