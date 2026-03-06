from quick_calc.calculator import Calculator


class QuickCalcApp:
    def __init__(self):
        self.calculator = Calculator()
        self.current = None
        self.operator = None
        self.display = "0"

    def input_number(self, value):
        self.display = str(value)

    def choose_operator(self, operator):
        self.current = float(self.display)
        self.operator = operator

    def calculate(self, next_value):
        next_value = float(next_value)

        if self.operator == "+":
            result = self.calculator.add(self.current, next_value)
        elif self.operator == "-":
            result = self.calculator.subtract(self.current, next_value)
        elif self.operator == "*":
            result = self.calculator.multiply(self.current, next_value)
        elif self.operator == "/":
            result = self.calculator.divide(self.current, next_value)
        else:
            raise ValueError("Invalid operator.")

        if result == int(result):
            self.display = str(int(result))
        else:
            self.display = str(result)

        return self.display

    def clear(self):
        self.current = None
        self.operator = None
        self.display = "0"
        self.calculator.clear()
        return self.display


if __name__ == "__main__":
    app = QuickCalcApp()
    print("Quick-Calc CLI")
    print("Enter: number operator number")
    print("Example: 5 + 3")
    user_input = input("> ").split()

    if len(user_input) == 3:
        a, op, b = user_input
        app.input_number(a)
        app.choose_operator(op)
        print("Result:", app.calculate(b))
    else:
        print("Invalid input.")