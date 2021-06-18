#내가 푼 것
def solution(n, k):

    a = list(map(lambda x : x , range(1,n+1)))
    #더 짧은 코드
    # visited = [0 for _ in range(N)]
    #a = [x for x in range(1, int(num) + 1)]
    c = perm(a)
    return c[k-1]
#나는 다른 사람 코드 써서 펙토리얼 구현한 것에서 원하는 값만 찾아서 리턴함

def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result


print(solution(3, 3))
print(solution(4, 9))