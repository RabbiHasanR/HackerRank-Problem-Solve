# if __name__ == '__main__':
    # n = int(input())
    # # integer_list = map(int, input().split())
    # # print()
    # input_line=input()
    # input_list=input_line.split()
    # for i in range(n):
    #     input_list[i]=int(input_list[i])
    # #print(input_list)
    # t=tuple(input_list)
    # print(hash(3))

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print(hash(tuple(integer_list)))

# numbers = input().strip().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# T = tuple(numbers)
# print(hash(T))


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))