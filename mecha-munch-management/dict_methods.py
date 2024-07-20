add_item = lambda current_cart, items_to_add: {
    i: ([0, current_cart.get(i)][not not current_cart.get(i)] + items_to_add.count(i))
    for i in {*items_to_add} | {*current_cart}
}

read_notes = lambda notes: add_item(dict.fromkeys({*notes}, 0), notes)
update_recipes = lambda ideas, recipe_updates: ideas | dict(recipe_updates)
sort_entries = lambda cart: {it: cart[it] for it in sorted(cart.keys())}
send_to_store = lambda cart, aisle_mapping: sorted(
    {item: [cart[item]] + aisle_mapping[item] for item in cart}.items(),
    key=lambda x: x[0],
    reverse=True,
)


def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        store_inventory[item][0] = store_inventory[item][0] - fulfillment_cart[item][0]
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = "Out of Stock"
    return store_inventory
