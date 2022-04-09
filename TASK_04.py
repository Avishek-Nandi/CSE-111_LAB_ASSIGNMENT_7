# Solution to Task 4

class Product:
    def __init__(self, id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price

    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+        "Price: "+str(self.__price)


class Book(Product):

    def __init__(self, id, title, price, isbn, publisher):
        self.publisher = publisher
        self.isbn = isbn
        super().__init__(id, title, price)

    def printDetail(self):
        return f"{Book.get_id_title_price(self)}\nISBN: {self.isbn} Publisher: {self.publisher}"


class CD(Product):

    def __init__(self, id, title, price, band, duration, genre ):

        self.genre = genre
        self.duration = duration
        self.band = band
        super().__init__(id, title, price)

    def printDetail(self):
        return f"{Book.get_id_title_price(self)}\nBand: {self.band} Duration: {self.duration} minutes\nGenre: {self.genre}"

if __name__ == "__main__":
    book = Book(1, "The Alchemist", 500, "97806", "HarperCollins")
    print(book.printDetail())
    print("-----------------------")
    cd = CD(2, "Shotto", 300, "Warfaze", 50, "Hard Rock")
    print(cd.printDetail())
