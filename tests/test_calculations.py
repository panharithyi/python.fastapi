from app.calculations import add,subtract,multiply,divide,BankAccount,InsufficientFunds
import pytest

#initialize bank account with balance zero
@pytest.fixture
def zero_bank_account():
    print('creating empty bank account')
    return BankAccount()

#initialize bank account with 50 bucks
@pytest.fixture
def bank_account():
    return BankAccount(50)

#illustrate pytest parametrize
@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2 , expected):
    print('test add function')
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(2,5) == 10

def test_divide():
    assert divide(4,2) == 2

def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(40)
    assert bank_account.balance == 90

def test_collect_interest(bank_account):

    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize('deposited, withdraw, expected', [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transactions(zero_bank_account,deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)

    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)