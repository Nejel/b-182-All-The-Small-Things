#https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    result = 'fake'
    kevin = 0
    stuart = 0
    counter = 0

    for i in s:
        if i in ['A', 'E', 'I', 'O', 'U']:
            counter += 1
            kevin += (len(s) - (counter - 1))
        else:
            counter += 1
            stuart += (len(s) - (counter - 1))

    if kevin > stuart:
        result = ('Kevin %s' % kevin)
        print(result)
    elif kevin < stuart:
        result = ('Stuart %s' % stuart)
        print(result)
    else:
        print('Draw')
    return result


if __name__ == '__main__':
    s = input()
    minion_game(s)
