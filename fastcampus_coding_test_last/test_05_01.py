'''
친구들로부터 천재 프로그래머로 불리는 프로도는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다. 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

가사 단어 제한사항

words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드 제한사항

queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
검색 키워드는 중복될 수도 있습니다.
각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.
'''

#find, index 근데 find가 더 좋아보인다 find 에는 벨류 에러가 없다
#https://hashcode.co.kr/questions/1149/%EB%AC%B8%EC%9E%90%EC%97%B4%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EB%AC%B8%EC%9E%90%EA%B0%80-%EB%AA%87%EB%B2%88%EC%A7%B8-%EC%9D%B8%EB%8D%B1%EC%8A%A4%EC%97%90%EC%84%9C-%EB%82%98%ED%83%80%EB%82%98%EB%8A%94%EC%A7%80-%EC%95%8C%EC%95%84%EB%82%B4%EB%8A%94-%ED%95%A8%EC%88%98

def solution(words, queries):

    answer = [0 for x in range(len(queries))]
    #queries 에 맞는 조건을 가진 word 가 몃개 인지 찾는거임

    #queries가 고정임? 이건 방식에 따라 다름 아무튼
    #answer 부분은
    for i in range(len(queries)):

        print("-------------------------------------")
        for j in range(len(words)):
        #검사 갯수가 이상해서 (누락 있어서 ) 반복문 보니까 [i] 붙어있었음 ㅋ
            print(queries[i],words[j])
            #조건 맞출 놈이 전치사를 확인해야 하는지 접미사를 확인해야하는 지 확인
            if queries[i][0] == '?':
                print("전치사 검사")

                print(queries[i].count("?"))
                a = queries[i].count("?")
                print(queries[i][a:])
                #이러면 첫글자부터 몃개 있는지 확인 가능


                if queries[i][a:] == words[j][a:] and len(queries[i]) == len(words[j]):
                    print("통과")
                    answer[i] += 1
                else:
                    print("X")




            elif queries[i][-1] == '?':


                print("접미사 검사")


                print(queries[i].index("?"))
                a = queries[i].index("?")
                print(queries[i][:a])

                if queries[i][:a] == words[j][:a] and len(queries[i]) == len(words[j]):
                    print("통과")
                    answer[i] += 1
                else:
                    print("X")



    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?","??test"]
print(solution(words, queries))

#solution(words, queries)

result = [3, 2, 4, 1, 0]
