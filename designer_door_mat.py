def getVals():
    height, width = map(int, input().split())
    assert height % 2 == 1  # make sure the numbers are odd
    assert width == height * 3  # make sure the width is 3 times the height
    return height, width


def designMat(design, message):
    h, w = getVals()

    # Top
    pattern = [i for i in range(1, h, 2)]
    for i in pattern:
        yield '{}'.format(str(design * i)).center(w, '-')

    # Middle
    yield '{}'.format(message).center(w, '-')

    # Bottom
    pattern = list(reversed(pattern))
    for i in pattern:
        yield '{}'.format(str(design * i)).center(w, '-')


for line in designMat('.|.', 'WELCOME'):
    print(line)