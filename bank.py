import json
import uuid
from pathlib import Path

class Bank:

    database = "data.json"

    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, "r") as file:
                return json.load(file)
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def create_account(cls, name, age, email, pin):

        data = cls.load_data()

        account_no = str(uuid.uuid4())[:8]

        user = {
            "account_no": account_no,
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "balance": 0
        }

        data.append(user)
        cls.save_data(data)

        return account_no

    @classmethod
    def authenticate(cls, account_no, pin):

        data = cls.load_data()

        for user in data:
            if user["account_no"] == account_no and user["pin"] == pin:
                return user

        return None

    @classmethod
    def deposit(cls, account_no, amount):

        data = cls.load_data()

        for user in data:
            if user["account_no"] == account_no:
                user["balance"] += amount

        cls.save_data(data)

    @classmethod
    def withdraw(cls, account_no, amount):

        data = cls.load_data()

        for user in data:
            if user["account_no"] == account_no:

                if user["balance"] >= amount:
                    user["balance"] -= amount
                    cls.save_data(data)
                    return True

        return False