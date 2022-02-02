from payment import Payment

class RegularPayment(Payment):
    def __init__(self, hourly_rate):
        super().__init__(hourly_rate)

    def run_strategy(self, hours):
        return hours * self.hourly_rate