def get_user_numbers():
    numbers = []
    num = input("请输入一个数字 (输入'完成'结束输入)：")
    while num != "完成":
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("无效的输入，请重新输入一个数字。")
        num = input("请输入一个数字 (输入'完成'结束输入)：")
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    print("欢迎使用平均值计算器！")
    user_numbers = get_user_numbers()
    average = calculate_average(user_numbers)
    print("平均值为:", average)

if __name__ == "__main__":
    main()
