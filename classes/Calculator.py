class Calculator:

    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number

    def division(self) -> float:
        result = self.first_number / self.second_number
        print(f"\nANSWER : {result}\n")
        return result

    def multiplication(self) -> float:
        result = self.first_number * self.second_number
        print(f"\nANSWER : {result}\n")
        return result

    def addition(self) -> float:
        result = self.first_number + self.second_number
        print(f"\nANSWER : {result}\n")
        return result

    def subtraction(self) -> float:
        result = self.first_number - self.second_number
        print(f"\nANSWER : {result}\n")
        return result