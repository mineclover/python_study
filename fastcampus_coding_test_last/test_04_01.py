#단어가 n개인 순환문에서 keek을 전부 지나가게하는 최소 dist 사용
#dist 로 지나가는 것임

# 과제 6번 코드란

#특정 크기의 원. 에 취약지점.이 있고, 그 취약지점을 검사할 수 있는 최대 길이가 정해진 유닛.들이 있음,
#그런 상황에서 최소 인원 구하기, 지목은 안해도 됨

def solution(n, weak, dist):
    answer = 0
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))