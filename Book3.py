'''.Q.3)Book Class
Create a Book class with title, author, and price.
Add a method to apply discount (e.g., 20%).
'''
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self):
        discount = self.price * 0.20
        self.price -= discount
        return discount
book = Book("The Alchemist", "Paulo Coelho", 500)

print("Title:", book.title)
print("Author:", book.author)
print("Original Price:", book.price)

discount = book.apply_discount()
print("Discount Applied:", discount)
print("Discounted Price(book Price):", book.price)
