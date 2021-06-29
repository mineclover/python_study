# 과제 5번 코드란
def solution(words, queries):
    answer = [0 for x in range(len(queries))]

    for i in range(len(queries)):
        for j in range(len(words)):
            if queries[i][0] == '?':
                a = queries[i].count("?")
                if queries[i][a:] == words[j][a:] and len(queries[i]) == len(words[j]):
                    answer[i] += 1
                else:
                    pass

            elif queries[i][-1] == '?':
                a = queries[i].index("?")
                if queries[i][:a] == words[j][:a] and len(queries[i]) == len(words[j]):
                    answer[i] += 1
                else:
                  pass

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
