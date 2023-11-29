def replace_sec(h, m, s):
    re = h*3600 + m*60 + s
    return re
def replace_angle(sec):
    h = int(sec/3600)
    m = int((sec%3600)/60)
    s = (sec%3600)%60
    sec_angle = s*6 % 360
    min_angle = ((m*6) + (s/10)) % 360
    hour_angle = ((h*30) + (m/2) + (s/120)) % 360
    return (hour_angle, min_angle, sec_angle)

def solution(h1, m1, s1, h2, m2, s2):
    f = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    answer = -1
    count = 0
    past_h, past_m, past_s = replace_angle(replace_sec(h1,m1,s1))
    for i in range(replace_sec(h1, m1, s1), replace_sec(h2, m2, s2)+1):
        for j in f:
            h, m, s = replace_angle((i+j))
            h, m, s = round(h,1),round(m,1),round(s,1)
            if s < past_s:
                past_s -= 360
            if past_s < h <= s:
                count += 1
            if past_s < m <= s:
                count += 1
            if (past_s < h <= s and past_s < m <= s):
                count -= 1
            # 시침과 분침 초침이 모두 겹치는 경우 
            # 11시 59분 59초에서 12시 0분 0초로 넘어가는 경우 체크
            past_h = h
            past_m = m
            past_s = s

    return count
