class Account:
    name = ''
    pwd = ''
    money = 0

    def __init__(self, name, pwd):  # 생성자
        self.name = name
        self.pwd = pwd
        self.money = 1000

    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        if self.money < money:
            return
        else:
            self.money -= money

    def query(self):
        print(self.name, "님 현재 잔액은 ", self.money, "입니다.")


class bankmanager:
    accounts = []
    loginA = None
    money = 0

    def __init__(self):
        bankmanager.accounts = []

    def displaymainmenu(self):
        print("1.로그인")
        print("2.회원가입")
        print("3.종료")
        return int(input("check: "))

    def join(self):
        name = input("name: ")
        pwd = input("pwd: ")
        bankmanager.accounts.append(Account(name, pwd))

    def login(self):
        name = input("name: ")
        pwd = input("pwd: ")
        for a in bankmanager.accounts:
            if a.name == name and a.pwd == pwd:
                bankmanager.loginA = a
                return True
        return False

    def displaysubmenu(self):
        print("1.입금")
        print("2.출금")
        print("3.조회")
        print("4.로그아웃")
        return int(input("check: "))

    def deposit(self):
        self.money += int(input("money: "))
        bankmanager.loginA.deposit(self.money)

    def withdraw(self):
        a = int(input("money: "))
        if self.money >= a:
            self.money -= a
            bankmanager.loginA.withdraw(self.money)
        else:
            print("잔액이 부족합니다.")

    def query(self):
        print("현재 잔액은 ", self.money, "입니다.")