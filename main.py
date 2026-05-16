

context = {
    "products" :[
        {
            'name': 'Product 1',
            'price': 10.99,
        },
        {
            'name': 'Product 2',
            'price': 19.99,
        },
    ]
}

for p in context['products']:
    print(p['name'], p['price'])


class Product:
    name = ""
    price = 0.0

p = Product()
p.name = "Product 1"
p.price = 10.99

print (p.name, p.price)