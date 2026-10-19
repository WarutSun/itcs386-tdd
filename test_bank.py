import pytest
from bank import BankAccount, InsufficientFunds


@pytest.fixture
def account():
    return BankAccount("alice", balance=100)


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100


def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100