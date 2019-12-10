def reverseArray(a):
    reverse_list=list(reversed(a))
    return reverse_list

if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
