# A simple ATM controller

## How To Clone
This project can be cloned by entering
```
git clone https://github.com/YunOh21/simple_atm.git
```
into your terminal.

This project is written and tested in Python 3.8.3.

## How To Run
```
python3 controller.py
```
Then, follow the instructions displayed on the prompt.

- You could make a new card or use an old card.
- This system doesn't have a database, so the card's information is always the same. (The system could be enhanced by integrating an h2 database or similar.)
  - If you made a new card, the balance is 0.
  - If you used an old card, the balance is 999999999.
  - You may check or edit these values in ```class_card.py.```
- You could select savings/chequing account.
  - You could see balance of both accounts.
  - If you chose savings account, you could only 'deposit'.
  - If you chose chequing account, you could 'deposit' or 'withdraw'.

## How To Test
```
python3 test_controller.py
```
- This file has 23 test cases for functions in ```controller.py```
- Those test cases are written with ```unittest``` module in Python3.
- You may modify some parameters in the test cases to experiment with values different from those already written.