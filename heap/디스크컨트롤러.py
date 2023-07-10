# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
# 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.
# 예를들어

# - 0ms 시점에 3ms가 소요되는 A작업 요청
# - 1ms 시점에 9ms가 소요되는 B작업 요청
# - 2ms 시점에 6ms가 소요되는 C작업 요청
# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때,
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 
# return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)
import heapq
def solution(jobs):
    answer = 0
    start = [jobs[i][0] for i in range(len(jobs))]
    time = [jobs[i][1] for i in range(len(jobs))]
    heapq.heapify(time)
    while time:
        heapq.heappop(time)
    return answer
jobs =[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))