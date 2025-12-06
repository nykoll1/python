class BaseCalculator:   
    def calculate(self, a, b):
        return "Base class cannot calculate"

class Calculator(BaseCalculator): 
    def calculate(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "Error: division by zero"
            return a / b
        else:
            return "Invalid operation"
        
#ისტორიის ფაილში შენახვა 
def save_history(history):
    with open("history.txt", "w", encoding="utf-8") as file:
        for item in history:
            file.write(item + "\n")

#ფაილის წაშლა
def delete_history():
    try:
        open("history.txt", "r")  
        with open("history.txt", "w") as f:
            pass
        print("History deleted!")
    except FileNotFoundError:
        print("No history file found!")


def run_calculator():
    calc = Calculator()
    history = []

    print("მარტივი კალკულატორი ")

    while True:
        a = int(input("შეიყვანეთ პირველი რიცხვი: "))
        b = int(input("შეიყვანეთ მეორე რიცხვი: "))
        op = input("Choose operation (+, -, *, /): ")

        result = calc.calculate(a, b, op)
        print("Result:", result)

        history.append(f"{a} {op} {b} = {result}")

        again = input("გსურთ გააგრძელოთ? (კი/არა): ")
        if again.lower() != "კი":
            break

    save_history(history)
    print("History saved to history.txt")


def main_menu():
    while True:
        print("\n= MENU =")
        print("1. კალკულატორის დაწყება")
        print("2. ისტორიის წაშლა")
        print("3. გასვლა")

        choice = input("აირჩიე: ")

        if choice == "1":
            run_calculator()
        elif choice == "2":
            delete_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("ხელახლა სცადეთ")

main_menu()