#두번 째 시도
#순차적 접근 https://m31phy.tistory.com/130
#나열 후 삭제
def solution(intervals):

    inter_l = len(intervals)
    va = []

    for a in range(inter_l): #간격이 거꾸로 나오면 되돌림

        if intervals[a][0] < intervals[a][1]:
            for b in range(intervals[a][0],intervals[a][1]+1):
                va.append(b)

        else:
            for b in range(intervals[a][1],intervals[a][0]+1):
                va.append(b)
    print(va)
    #중복 숫자 제거
    va = list(set(va)) #중복 제거
    va.sort() #정렬

    print(va[-1:])

    #없는 수 찾기
    #마지막 수 + 1
    d = va[len(va)-1]
    print(d)
    mn = None
    mx = None
    print(len(va))

    data = []
    sub = []
    p = len(va)-1 #va[] 안에 넣으면 오류 발생
    for i in range(va[0],va[p]+1):

        print("진입",i)

        if i in va: #찾는게 있으면
            if mn == None: #미니에 뭐 없으면
                print("최소값등록")
                mn = i
                sub.append(i)
            else:
                continue

            print(va.index(i))

            #continue
        else: # 찾는게 없는데
            if mn != None: #미니 체워져 있으면
                sub.append(i-1)
                mn = None
                mx = None
                data.append(sub)
                sub = []
                print(data)
            else: #mn 없는데 또 없다 나오면
                continue
            print("없다")
    else:
        sub.append(va[p])
        data.append(sub)

    return data