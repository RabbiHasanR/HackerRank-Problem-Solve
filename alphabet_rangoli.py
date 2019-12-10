import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    # your code goes here
    for i in srange(size):
        print('-'.join([alpha[size-j-1] for j in srange(i+1)]).center(4*(size-1)+1,'-'))

def srange(N):
    return list(range(N))+list(range(N-2,-1,-1))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)