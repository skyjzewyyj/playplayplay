import random

def guess_number():
    target = random.randint(1, 100)  # 随机生成 1~100 的整数
    attempts = 0
    print("我想了一个 1 到 100 之间的数字，你猜猜看！")

    while True:
        try:
            guess = int(input("请输入你的猜测："))
        except ValueError:
            print("请输入一个整数！")
            continue

        attempts += 1

        if guess < target:
            print("太小了！")
        elif guess > target:
            print("太大了！")
        else:
            print(f"恭喜你，猜对了！你一共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    guess_number()