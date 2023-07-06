# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 
# 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때,
# 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
from collections import deque
def solution(priorities, location):
    answer = 0
    count = 0
    max_list = priorities.copy()
    max_list.sort()
    priorities = deque(priorities)

    while max_list:
        first = priorities.popleft()
        max_val = max_list.pop()
        if location<0:
            location+=len(priorities)+1
        print(location, priorities, max_list, first, max_val)   
        if first == max_val and location==0:
            count += 1
            print("목표끝")
            return count
        elif first == max_val and location!=0:
            print("다른거 pop")
            count += 1
            location-=1
        elif first<max_val:
            print("rotate")
            location-=1
            priorities.append(first)
            max_list.append(max_val)

    return count

priorities= [1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities,location))