def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("不能除以零")
    return x / y

def power(x, y):
    return x ** y

def calculator():
    print("简单计算器")
    print("=" * 30)
    print("选择操作:")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 乘方 (**)")
    print("0. 退出")
    print("=" * 30)
    
    while True:
        try:
            choice = input("\n请输入操作编号 (0-5): ")
            
            if choice == '0':
                print("感谢使用计算器，再见！")
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print("无效的选择，请重新输入！")
                continue
            
            num1 = float(input("输入第一个数字: "))
            num2 = float(input("输入第二个数字: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            elif choice == '5':
                result = power(num1, num2)
                print(f"\n{num1} ** {num2} = {result}")
            
        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    calculator()