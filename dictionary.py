
def die():
    return 'Wasted'

switcher = {
    0:'zero',
    1:'One',
    2:die
}

print(switcher[int(input('enter index: ')) ])


