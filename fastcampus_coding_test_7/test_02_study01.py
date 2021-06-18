#https://gomguard.tistory.com/138


intervals = [[1,3],[2,6],[8,10],[15,18],[21,10]]
#연속성 체크 어케함

#일단 내부 정렬
inter_l = len(intervals)
va = [[] for i in range(inter_l)] # 내부를 0으로 선언 응용 *( list = [0 for i in range(n)] )

for i in range(inter_l):

    if intervals[i][0] > intervals[i][1]:
        va[i].append(intervals[i][1])
        va[i].append(intervals[i][0])
    else:
        va[i].append(intervals[i][0])
        va[i].append(intervals[i][1])


print(intervals)
print(va)

#병합 대상인지 구분 후

while inter_l > 0:
    




#병합 방식 선택




for a in range(10,20+1):
    print(a)

def solution(intervals):
    return []

#비교 대상 b의 합이 원본 a의 합보다 1 이상 작으면,

# 2, 3 = 5 / 1 , 5 = 6 / 5 < 6   ,