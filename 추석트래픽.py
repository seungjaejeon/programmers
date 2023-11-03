def solution(lines):
    l = []
    for i, val in enumerate(lines):
        sec = 0
        temp = 0
        for j, val2 in enumerate(list(val[11:].split(":"))):
            if j==0:
                sec += int(val2)*60*60
            elif j==1:
                sec += int(val2)*60
            elif j==2:
                sec_list = list(val2.replace('s','').split(" "))
                sec += float(sec_list[0])
                temp = sec
                sec -= float(sec_list[1])
                sec += 0.001
                l.append((round(sec,3),round(temp,3)))
    answer = 0
    
    for i, val in enumerate(l):
        count = 0
        start = val[1]
        end = round(val[1]+0.999,3)
        print(f"{val[0], val[1]}")
        print(start, end)
        for j, val2 in enumerate(l):
            if start<=val2[0]<=end or start<=val2[1]<=end or (val2[0]<=start and val2[1]>=end):
                count += 1
        if answer<count:
            answer = count
        
    return answer