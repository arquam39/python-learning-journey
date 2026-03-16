# bank account

class account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,amount):
        self.amount = self.balance - amount
        print(f"you have debited {amount} and your current balance is {self.amount}")

    def cradit(self,amount2):
        self.amount2 = self.balance + amount2
        print(f"you have debited {amount2} and your current balance is {self.amount2}")


pay1 = account(50000,"abcdr")
pay2 = account(70000,"gghcdr")

pay2.debit(500)
pay1.cradit(199)


# student result check

class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def average(self):
        sum = 0
        for i in range (len(self.mark)):
            sum += self.mark[i]
        avg = sum/3
        print(f"{self.name} has obtained {avg} %")

s1 = student("Ali",[91,78,88])
s2 = student("Atika",[67,89,90])

student.average(s1)
student.average(s2)

# also

class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def average(self):
        sum = self.mark1 + self.mark2 + self.mark3
        avg = sum/3
        print(avg)

s1 = student("Ali",90,78,80)
s2 = student("Atika",67,89,90)

student.average(s1)
student.average(s2)
