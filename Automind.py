

print("===============================================")
print("        Welcome to AutoMind Deal Helper         ")
print(
print("===============================================\n")

# Inventory
print("Here are some available cars:\n")

inventory = {
    "BMW M3": 62900,
    "BMW X5": 58900,
    "Mercedes C300": 41200,
    "Mercedes GLE 350": 58950,
    "Porsche 911": 113000,
    "Porsche Macan": 63900,
    "Toyota Camry": 24500,
    "Toyota Corolla": 19800,
    "Honda Civic": 22500,
    "Nissan Altima": 23900
}

# Display cars with prices
for car, price in inventory.items():
    print(f" - {car}: ${price:,}")

# User picks a car
print("\n-----------------------------------------------")
car_choice = input("Type the EXACT name of the car you're interested in: ")
print("-----------------------------------------------\n")

if car_choice not in inventory:
    print("Sorry, that car is not in our inventory.")
    exit()

base_price = inventory[car_choice]

# Show base price
print(f"You selected: {car_choice}")
print(f"Base Price: ${base_price:,.2f}")

# Tax & fees
SALES_TAX_RATE = 0.07
DEALER_FEE = 699

tax_amount = base_price * SALES_TAX_RATE
otd_price = base_price + tax_amount + DEALER_FEE

print("\n--- Price Breakdown ---")
print(f"Sales Tax (7%): ${tax_amount:,.2f}")
print(f"Dealer Fee:      ${DEALER_FEE:,.2f}")
print(f"Out-the-Door Price: ${otd_price:,.2f}\n")

# Ask payment type
payment_type = input("Are you paying Cash or Finance? (cash/finance): ").lower()

if payment_type == "cash":
    print("\n-----------------------------------------------")
    print(f"Your total cash price is: ${otd_price:,.2f}")
    print("Thank you for using AutoMind!")
    print("-----------------------------------------------")
    exit()

# Finance section
if payment_type == "finance":
    print("\n--- Finance Calculator ---")
    down_payment = float(input("Enter your down payment amount ($): "))
    apr = float(input("Enter your interest rate (APR %): "))
    term = int(input("Enter loan term (months): "))

    amount_financed = max(0, otd_price - down_payment)

    # Monthly payment formula
    r = (apr / 100) / 12

    if r == 0:
        monthly = amount_financed / term
    else:
        monthly = amount_financed * r / (1 - (1 + r) ** (-term))

    print("\n-----------------------------------------------")
    print("           Finance Summary")
    print("-----------------------------------------------")
    print(f"Vehicle:           {car_choice}")
    print(f"Out-the-Door Price: ${otd_price:,.2f}")
    print(f"Down Payment:       ${down_payment:,.2f}")
    print(f"Amount Financed:    ${amount_financed:,.2f}")
    print(f"APR:                {apr}%")
    print(f"Term:               {term} months")
    print(f"Monthly Payment:    ${monthly:,.2f}")
    print("-----------------------------------------------")
    print("        Thank you for using AutoMind!")
    print("-----------------------------------------------")

else:
    print("Invalid input. Please type 'cash' or 'finance'.")
