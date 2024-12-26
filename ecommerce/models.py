class Cart:
    """In-memory store for user carts."""
    def __init__(self):
        self.carts = {}

    def add_item(self, user_id, item):
        if user_id not in self.carts:
            self.carts[user_id] = []
        self.carts[user_id].append(item)

    def get_cart(self, user_id):
        return self.carts.get(user_id, [])

    def clear_cart(self, user_id):
        if user_id in self.carts:
            del self.carts[user_id]

class Order:
    """In-memory store for orders."""
    def __init__(self):
        self.orders = []

    def create_order(self, user_id, total_amount, items):
        order = {'user_id': user_id, 'total_amount': total_amount, 'items': items}
        self.orders.append(order)
        return order

class DiscountCode:
    """In-memory store for discount codes."""
    def __init__(self):
        self.codes = {}
    
    def generate_code(self, order_count):
        code = f'DISCOUNT{order_count // 5 + 1}'
        self.codes[code] = False  # Not used yet

    def use_code(self, code):
        if code in self.codes and not self.codes[code]:
            self.codes[code] = True  # Mark as used
            return True
        return False

# Initialize in-memory stores globally.
cart_store = Cart()
order_store = Order()
discount_code_store = DiscountCode()
