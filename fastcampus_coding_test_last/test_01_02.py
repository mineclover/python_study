# 과제1번 코드란

def solution(s):
    d = str(s)
    d = ''.join(list(reversed(d)))

    if s == d:
        return ''

    data = list(s)
    ln = len(data)
    ln2 = ln // 2

    a = s[:ln2]
    c = data[-ln2:]
    c.reverse()
    c = ''.join(c)

    if a == c:
        print("True")
        return ''
    else:
        c = data[:ln2]
        d = data[:ln2]
        c.reverse()
        d = d + c
        d = ''.join(d)
        return d


s = 'abcdcba'
print(solution(s))

s = 'bannana'
print(solution(s))

s = 'wabe'
print(solution(s))