class Labrary:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        
    def remove_book(self, title, quantity):
        if title in self.books:
            if self.books[title] > quantity:
                self.books[title] -= quantity
            else:
                del self.books[title]               
        else:
            print("no book was fond")

    def view_book(self):
        print(self.books)


    def get_total_books(self):
        total = sum(self.books.values())
        print(f'Total books available: {total}')

new_labrary=Labrary()

new_labrary.add_book("hello",2)

new_labrary.view_book()

new_labrary.remove_book("hello",1)

new_labrary.view_book()

new_labrary.get_total_books()

new_labrary.add_book("azad",50)
new_labrary.view_book()







    

    

    