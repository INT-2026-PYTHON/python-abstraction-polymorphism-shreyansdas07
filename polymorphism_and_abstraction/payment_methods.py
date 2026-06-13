"""
## 2. Payment Methods — Duck Typing Polymorphism  *(Medium)*

=================================================
PAYMENT METHODS (DUCK TYPING)
=================================================

Problem Statement:
Build THREE INDEPENDENT classes that do NOT
share a common parent:

   class CreditCard:
       pay(amount)
   class UPI:
       pay(amount)
   class Cash:
       pay(amount)

Even though they have no common base class,
each one has a method named `pay(amount)`.
A single function `checkout(payment_method,
amount)` should work with ALL of them, just by
calling `payment_method.pay(amount)`.

This is DUCK TYPING POLYMORPHISM:
   "If it walks like a duck and quacks like a
    duck, it's a duck."
   If an object has a `pay()` method, the
   function treats it as a payment method.


-------------------------------------------------
Input Example:
methods = [
   CreditCard("Alice", "4111-1111-1111-1111"),
   UPI("bob@upi"),
   Cash("Carol"),
]

for m in methods:
    checkout(m, 500)

Output Example:
[CreditCard] Alice paid 500 via card 4111-1111-1111-1111
[UPI]        bob@upi paid 500
[Cash]       Carol paid 500 in cash

-------------------------------------------------
Explanation:
- `checkout` does not care which CLASS the
  object is, only that the object has a
  `pay()` method.
- This is polymorphism WITHOUT inheritance —
  Python doesn't require a shared base class.
- Adding a new payment method later (e.g.
  PayPal) only requires writing a new class
  with a `pay()` method; `checkout` keeps
  working unchanged.
=================================================

"""
class CreditCard:
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def pay(self, amount):
        print(f"[CreditCard] {self.name} paid {amount} via card {self.card_number}")

class UPI:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"[UPI]        {self.upi_id} paid {amount}")

class Cash:
    def __init__(self, name):
        self.name = name

    def pay(self, amount):
        print(f"[Cash]       {self.name} paid {amount} in cash")

def checkout(payment_method, amount):
    payment_method.pay(amount)

methods = []
while True:
    method_type = input("Enter payment method type (CreditCard, UPI, Cash), or 'done' to finish: ").strip().lower()

    if method_type == 'done':
        break

    try:
        if method_type == 'creditcard':
            name = input("Enter name for CreditCard: ")
            card_number = input("Enter card number for CreditCard: ")
            methods.append(CreditCard(name, card_number))
            print(f"CreditCard for {name} added.\n")
        elif method_type == 'upi':
            upi_id = input("Enter UPI ID: ")
            methods.append(UPI(upi_id))
            print(f"UPI for {upi_id} added.\n")
        elif method_type == 'cash':
            name = input("Enter name for Cash payment: ")
            methods.append(Cash(name))
            print(f"Cash payment for {name} added.\n")
        else:
            print("Invalid payment method type. Please enter 'CreditCard', 'UPI', or 'Cash'.\n")
    except Exception as e:
        print(f"An error occurred while adding method: {e}\n")

if not methods:
    print("No payment methods added. Exiting.\n")
else:
    while True:
        try:
            amount_str = input("Enter the amount to be paid for all methods: ")
            payment_amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    print(f"Processing Payments for amount {payment_amount}")
    for m in methods:
        checkout(m, payment_amount)
