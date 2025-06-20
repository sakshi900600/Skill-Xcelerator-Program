# Keep withdrawing ₹100 until balance is zero

balance = 500

while balance != 0:
    balance -= 100
    print(f"Withdrew ₹100, Balance: ₹{balance}")


# output: 
# Withdrew ₹100, Balance: ₹400
# Withdrew ₹100, Balance: ₹300
# Withdrew ₹100, Balance: ₹200
# Withdrew ₹100, Balance: ₹100
# Withdrew ₹100, Balance: ₹0