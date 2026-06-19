import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exeception occuerd as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountgenrate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name" : input("Tell your name : -"),
            "age" : int(input("Tell your age :- ")),
            "email" : input("Tell your email :- "),
            "pin" : input("Tell your  4 pin :- "),
            "accountNo." : Bank.__accountgenrate(),
            "balance" : 0
        }

        if info['age']<18 or len(str(info['pin'])) != 4:
            print("you are not eligible for creating an account")
        else:
            print("account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            Bank.data.append(info)
            Bank.__update()
    def depositmoney(self):
        account = input("Tell your account number :- ")
        pin = input("Tell your 4 pin :- ")
        userdata = [i for i in Bank.data if i['accountNo.'] == account and i['pin'] == pin]
        if not userdata:
            print("account number or pin is incorrect")
        else:
            ammount = int(input("Tell the amount you want to deposit :- "))
            if ammount > 100000 or ammount < 0:
                print("you can't deposit more than 100000 or you can't deposit negative amount")
            else:
                userdata[0]['balance'] += ammount
                Bank.__update()
                print(f"your account has been credited with {ammount} and your current balance is {userdata[0]['balance']}")

    def withdrawmoney(self):
        account = input("Tell your account number :- ")
        pin = input("Tell your 4 pin :- ")
        userdata = [i for i in Bank.data if i['accountNo.'] == account and i['pin'] == pin]
        if not userdata:
            print("account number or pin is incorrect")
        else:
            ammount = int(input("Tell the amount you want to withdraw :- "))
            if ammount > 100000 or ammount > userdata[0]['balance'] or ammount < 0:
                print("you can't withdraw more than 100000 or your balance is low or you can't withdraw negative amount")
            else:
                userdata[0]['balance'] -= ammount
                Bank.__update()
                print(f"your account has been debited with {ammount} and your current balance is {userdata[0]['balance']}")
    def showdetails(self):
        account = input("Tell your account number :- ")
        pin = input("Tell your 4 pin :- ")
        userdata = [i for i in Bank.data if i['accountNo.'] == account and i['pin'] == pin]
        if not userdata:
            print("account number or pin is incorrect")
        else:
            print("your account details are :- ")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
    def updatedetails(self):
        account = input("Tell your account number :- ")
        pin = input("Tell your 4 pin :- ")
        userdata = [i for i in Bank.data if i['accountNo.'] == account and i['pin'] == pin]
        if not userdata:
            print("account number or pin is incorrect")
        else:
            print("you cannot update the age , account number and balance")
            print("fill the details you want to update or leave it blank if you don't want to update it")
            newdata = {
                "name" : input("Tell your name : -"),
                "email" : input("Tell your email :- "),
                "pin" : input("Tell your new pin :- ")
            }
            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']
            if newdata['email'] == "":
                newdata['email'] = userdata[0]['email']
            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']
            newdata["accountNo."] = userdata[0]['accountNo.']
            newdata["balance"] = userdata[0]['balance']
            newdata["age"] = userdata[0]['age']
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            
            userdata[0].update(newdata)
            Bank.__update()
            print("your details have been updated successfully")

    def deleteaccount(self):
        account = input("Tell your account number :- ")
        pin = input("Tell your 4 pin :- ")
        userdata = [i for i in Bank.data if i['accountNo.'] == account and i['pin'] == pin]
        if not userdata:
            print("account number or pin is incorrect")
        else:
            check = input("are you sure you want to delete your account (y/n) :- ")
            if check.lower() != 'y':
                print("your account has not been deleted")
                return
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("your account has been deleted successfully")

user = Bank()
print("press 1 for creating an account")
print("press 2 for deposit money")
print("press 3 for withdraw money")
print("press 4 for information")
print("press 5 for updating the information")
print("press 6 for deleting account")

check = int(input("tell your respones :- "))

if check == 1:
    user.Createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.deleteaccount()