import random

class NumberEncryptor:
    def __init__(self):
        self.result = None

    def encrypt(self, num):
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            self.result = num + random.randint(1, 100)
        elif operation == '-':
            self.result = num - random.randint(1, 100)
        elif operation == '*':
            self.result = num * random.randint(1, 100)
        elif operation == '/':
            self.result = num / random.randint(1, 100)
        return self

    def __repr__(self):
        if self.result is None:
            return "No result available. Please encrypt a number first."
        else:
            return f"Encrypted Result: {self.result}"

encryptor = NumberEncryptor()
encrypted_result = encryptor.encrypt(5)
print(encrypted_result)
