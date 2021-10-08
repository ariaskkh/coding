def solution(numbers):
    numbers = list(map(str, numbers))
    # 특정 조건으로 리스트 정렬할 때 key = lambda x : 사용하기
    # 여기선 x * 3을 알아내는 게 포인트. 어렵다.
    numbers.sort(key=lambda x : x * 3, reverse = True)
    print(numbers)
    answer = ''.join(numbers)
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))