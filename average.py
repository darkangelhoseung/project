# 숫자 리스트의 평균을 계산하는 함수


def average(numbers):
    if not numbers:
        raise ValueError("평균을 계산하려면 숫자가 하나 이상 필요합니다.")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average([10, 20, 30]))
