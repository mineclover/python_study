def solution(N, number):
    sets = [{}, {N}]

    if N == number:
        return 1

    for i in range(2, 9):
        current_set = {int(str(N) * i)}
        for j in range(1, i // 2 + 1):
            for val_j in sets[j]:
                for val_k in sets[i - j]:
                    current_set.add(val_j + val_k)
                    current_set.add(val_j - val_k)
                    current_set.add(val_k - val_j)
                    current_set.add(val_j * val_k)
                    if val_k != 0:
                        current_set.add(val_j // val_k)
                    if val_j != 0:
                        current_set.add(val_k // val_j)

                    if number in current_set:
                        return i
        sets.append(current_set)
    return -1