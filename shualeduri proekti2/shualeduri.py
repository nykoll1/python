import json


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class BookManager:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    self.books.append(Book(item["title"], item["author"], item["year"]))
        except:
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump([b.__dict__ for b in self.books], file, indent=4)

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))
        self.save_books()

    def show_all(self):
        if not self.books:
            print("სია ცარიელია.")
            return
        for b in self.books:
            print(f"{b.title} | {b.author} | {b.year}")

    def search_by_title(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                print(f"ნაპოვნია: {b.title} - {b.author} ({b.year})")
                return
        print("ასეთი წიგნი ვერ მოიძებნა.")
        

def main():
    manager = BookManager()

    while True:
        print("\n BOOK MANAGER")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სათაურით")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპერაცია: ")

        if choice == "1":
            title = input("სათაური: ")
            author = input("ავტორი: ")
            year = input("წელი: ")

            if not year.isdigit():
                print("გთხოვთ შეიყვანოთ რიცხვი.")
                continue

            manager.add_book(title, author, int(year))
            print("წიგნი დამატებულია!")

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            t = input("მიუთითეთ სათაური: ")
            manager.search_by_title(t)

        elif choice == "4":
            print("გამოსვლა...")
            break

        else:
            print("არასწორი არჩევანი!")
            

main()