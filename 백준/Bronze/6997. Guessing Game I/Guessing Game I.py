def calculate_feedback(secret, guess):

    secret = list(f"{int(secret):04d}")

    guess = list(f"{int(guess):04d}")

    circles = 0

    squares = 0

    # 이미 매칭된 위치를 표시

    secret_used = [False] * 4

    guess_used = [False] * 4

    # 1단계: 정확한 위치의 숫자 일치 (circle)

    for i in range(4):

        if secret[i] == guess[i]:

            circles += 1

            secret_used[i] = True

            guess_used[i] = True

    # 2단계: 다른 위치의 숫자 일치 (square)

    for i in range(4):

        if not guess_used[i]:

            for j in range(4):

                if not secret_used[j] and guess[i] == secret[j]:

                    squares += 1

                    secret_used[j] = True

                    break

    return circles, squares

def main():

    T = int(input())

    for _ in range(T):

        secret_str, guess_str = input().split()

        circles, squares = calculate_feedback(secret_str, guess_str)

        print(f"For secret = {int(secret_str):04d} and guess = {int(guess_str):04d}, {circles} circles and {squares} squares will light up.")

if __name__ == "__main__":

    main()