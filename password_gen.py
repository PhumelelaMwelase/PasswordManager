# Password Generator Project
from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class GeneratePassword:

    def __init__(self):
        self.password = ""
        self.password_list = []
        self.password_letters = []
        self.password_numbers = []
        self.password_symbols = []

    def generate_password(self):
        self.password_letters = [choice(letters) for _ in range(randint(8, 10))]
        self.password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        self.password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        self.password_list = self.password_letters + self.password_numbers + self.password_symbols
        shuffle(self.password_list)

        self.password = "".join(self.password_list)

        return self.password
