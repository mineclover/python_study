# 과제1번 코드란

#여러시도를 했었음, 기록은 사라짐
#일단 , 있는 걸 그대로 썼을 떄 , 또는 c = d , e = c 같이 한 요소의 값을 여러 번 하는 것을 할 때
#리버스가 제대로 안되는 문제가 있었음 , 주소를 통한 참조 복사에 대한 증명? 그런 느낌이였음

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