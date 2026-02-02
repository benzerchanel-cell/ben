#6810470069
#นายณัฐกัณฑ์ บูรณบุณย์

price_input = float(input("Enter normal price: "))
discount_input = float(input("Enter percent discount: "))

print(f"Normal price: {price_input:.2f}")

print(f"Percent discount: {discount_input:.2f}%")

sales_price = price_input * (100 - discount_input) / 100

print(f"Discounted price: {sales_price:.2f}\n")