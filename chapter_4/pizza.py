pizzas = ['pepperoni', 'americano', 'dodo']
friends_pizzas = pizzas[:]

pizzas.append('hawaiian')
friends_pizzas.append('italian')

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nmy friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
