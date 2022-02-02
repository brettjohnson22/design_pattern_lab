from overtime_payment import OvertimePayment
from regular_payment import RegularPayment

class Employee:
    def __init__(self, pay_rate):
        self.payment_strategy = None
        self.pay_rate = pay_rate
        self.weekly_hours = 0
        self.account_balance = 0

    def record_weekly_hours(self, hours):
        self.weekly_hours = hours

    def determine_strategy(self):
        if self.weekly_hours > 40:
            self.payment_strategy = OvertimePayment(self.pay_rate)
        else:
            self.payment_strategy = RegularPayment(self.pay_rate)

    def calculate_payment(self):
        self.determine_strategy()
        weekly_payment = self.payment_strategy.run_strategy(self.weekly_hours)
        self.account_balance += weekly_payment
        return weekly_payment




