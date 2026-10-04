def calculate_bill(cart):
  subtotal = 0
  for product, details in cart.items():
    line_total = details["price"] * details["quantity"]
    subtotal += line_total
    print(f"{product} x {details['quantity']} = {line_total} ", end='')

  if subtotal >= 300000:
    discount = int(subtotal * 0.10)
  else:
    discount = 0

  total = subtotal - discount
  print(''+f"Subtotal: {subtotal} ", end='')
  print(f"Discount: {discount} ", end='')
  print(f"Total: {total}")

cart = {
  "Pen": {"price": 5000, "quantity": 10},
  "Notebook": {"price": 12000, "quantity": 5},
  "Bag": {"price": 250000, "quantity": 1},
}
calculate_bill(cart)