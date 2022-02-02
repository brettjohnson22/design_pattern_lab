from payment import Payment

class OvertimePayment(Payment):
    def __init__(self, hourly_rate):
        super().__init__(hourly_rate)

    def run_strategy(self, hours):
        regular_wages = self.hourly_rate * 40
        overtime_hours = hours - 40
        overtime_rate = self.hourly_rate * 1.5
        overtime_wages = overtime_rate * overtime_hours
        return regular_wages + overtime_wages



