user_carts = {}

def add_to_cart(user_id, item):
    user_carts.setdefault(user_id, []).append(item)

def view_cart(user_id):
    return user_carts.get(user_id, [])

def clear_cart(user_id):
    user_carts.pop(user_id, None)
