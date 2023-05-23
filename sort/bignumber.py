def solution(numbers):
    # 1. Convert any number to string
    numbers = list(map(str, numbers))

    # 2. Sort by comparing x+y to y+x
    # numbers의 원소의 조건이 0부터 1000이하이므로 각 원소의 길이를 4배한 후 앞에 4자리만 비교하여 정렬하면 우선순위가 명확히 나온다.
    # 따라서 아래와 같이 람다를 이용하여 정렬하였다.
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. Concatenate the sorted numbers and return
    answer = ''.join(numbers)

    # Exception handling to return "0" instead of "000" when there are multiple 0's
    if answer[0] == '0':
        return '0'
    else:
        return answer


# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

