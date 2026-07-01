def fibonacci_sequence(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

if __name__ == "__main__":
    try:
        n = int(input("몇 개의 피보나치 수를 출력할까요? "))
    except ValueError:
        print("정수를 입력하세요.")
    else:
        print(fibonacci_sequence(n))
