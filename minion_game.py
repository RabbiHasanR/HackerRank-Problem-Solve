def minion_game(string):
    # your code goes here
    vowel='AEIOU'
    stuart=0
    kevin=0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin+=(len(string)-i)
        else:
            stuart+=(len(string)-i)
    if kevin>stuart:
        print('Kevin {}'.format(kevin))
    elif stuart>kevin:
        print('Stuart {}'.format(stuart))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)