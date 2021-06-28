# 과제 2번 코드란

#리스트 대조 후 리스트에 없는 이름 반환
#동명이인도 걸러냄, 그러면 .. 그냥 갯수 세게 해서 리턴 할 때 반환하게 해
#어짜피 자료 제한 사항이 통과자 = 참여자 -1 임

#pop으로 하려했는데 안됨
#participant.index(completion[a]) 로 하려했는데 길이 제한 걸려서 0으로 바꿈
#문자열로 반환하기 위해서

def solution(participant, completion):

    for a in range(len(completion)):

        #print(participant.index(completion[0]))
        del(participant[participant.index(completion[0])])
        del(completion[0])

    return participant[0]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
