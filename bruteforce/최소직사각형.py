def solution(sizes):
    answer = 0
    garo_arr = []
    sero_arr = []
    for i in range(len(sizes)):
        garo_arr.append(max(sizes[i]))
        sero_arr.append(min(sizes[i]))
    garo = max(garo_arr)
    sero = max(sero_arr)
    answer = garo * sero
    return answer