from abc import ABC, abstractmethod


class State(ABC):
    def display_and_wait_for_input(self):
        # display screen
        # Block on input from user
        self.perform_action(...)

    @abstractmethod
    def perform_action(self, kwargs):
        pass


class Atm:
    def __init__(self, total_cash_balance):
        self.total_cash_balance = total_cash_balance
        self.state = DefaultState

    def start(self, **kwargs):
        self.state = self.state.perform_action(kwargs)
        self.state.display_and_wait_for_input()


class DefaultState(State):
    def perform_action(self, kwargs):
        # assuming this will be called on card insert
        return CardInserted

class FailState(State):
    def display_and_wait_for_input(self):
        # display failure
    def perform_action(self, kwargs):
        # display failure


class CardInserted(State):
    def validate_card(self):
    def perform_action(self, kwargs):
        if kwargs["card-type"] == "valid":
            return CardPin
        else:
            return DefaultState

class CardPin(State):
    @staticmethod
    def validate(user, pin):
        pass

    def perform_action(self, kwargs):
        if self.validate(kwargs["user"], kwargs["pin"]):
            return TransactionOptions
        else:
            return DefaultState

class TransactionOptions(State):
    def perform_action(self, kwargs):
        pass


if __name__ == "__main__":
    atm = Atm()
    atm.start()





