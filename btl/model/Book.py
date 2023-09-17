import json
import btl.utility as utility

class Book:
    bookList = []
    bookFile = "books.json"

    def __init__(self, id, name, publishId, price, count, status):
        self.id = id
        self.name = name
        self.publishId = publishId
        self.price = price
        self.count = count
        self.status = status

    @staticmethod
    def enter_book():
        print("Enter the number of books: ")
        num_books = int(input())
        for _ in range(num_books):
            auto_id = utility.autoID(6)
            print(f"Book ID: {auto_id}")
            name = input("Enter book name: ")
            publish_id = input("Enter publisher ID: ")
            price = float(input("Enter book price: "))
            count = int(input("Enter book count: "))
            status = input("Enter book status: ")

            book = Book(auto_id, name, publish_id, price, count, status)
            Book.bookList.append(book)

        while True:
            save_choice = input("Do you want to save the data (y/n)?: ").lower()
            if save_choice not in ['y', 'n']:
                continue
            if save_choice == 'y':
                Book.save_books(Book.bookFile, Book.bookList)
                print("Data saved successfully!")
                break
            elif save_choice == 'n':
                print("Data not saved.")
                break

    @staticmethod
    def print_book(book):
        print(
            f"   {book.id.ljust(10)}{book.name.ljust(30)}{book.publishId.ljust(10)}{str(book.price).ljust(15)}{str(book.count).ljust(10)}{book.status.ljust(20)}")

    @staticmethod
    def print_header():
        print(
            f"   {'ID'.ljust(10)}{'Name'.ljust(30)}{'Publisher ID'.ljust(10)}{'Price'.ljust(15)}{'Count'.ljust(10)}{'Status'.ljust(20)}")

    @staticmethod
    def find_book(book_list):
        while True:
            print("Search by:")
            print("0: Exit.\n1: ID.\n2: Name.\n3: Publisher ID.\n4: Price.\n5: Count.\n6: Status.")
            search_option = int(input("Enter your choice: "))

            if search_option == 0:
                break
            if search_option not in [1, 2, 3, 4, 5, 6]:
                print("Invalid choice.")
                continue

            search_term = input("Enter the search term: ")
            result_list = []

            for book in book_list:
                if search_option == 1 and book.id == search_term:
                    result_list.append(book)
                elif search_option == 2 and book.name == search_term:
                    result_list.append(book)
                elif search_option == 3 and book.publishId == search_term:
                    result_list.append(book)
                elif search_option == 4 and str(book.price) == search_term:
                    result_list.append(book)
                elif search_option == 5 and str(book.count) == search_term:
                    result_list.append(book)
                elif search_option == 6 and book.status == search_term:
                    result_list.append(book)

            if len(result_list) != 0:
                Book.print_header()
                for result in result_list:
                    Book.print_book(result)
            else:
                print("No matching results found.")

    @staticmethod
    def sort_book(book_list, sort_key):
        while True:
            print("Sort by:")
            print("0: Exit.\n1: ID.\n2: Name.\n3: Publisher ID.\n4: Price.\n5: Count.\n6: Status.")
            sort_option = int(input("Enter your choice: "))

            if sort_option == 0:
                break
            if sort_option not in [1, 2, 3, 4, 5, 6]:
                print("Invalid choice.")
                continue

            if sort_option == 1:
                sorted_list = sorted(book_list, key=lambda x: x.id)
            elif sort_option == 2:
                sorted_list = sorted(book_list, key=lambda x: x.name)
            elif sort_option == 3:
                sorted_list = sorted(book_list, key=lambda x: x.publishId)
            elif sort_option == 4:
                sorted_list = sorted(book_list, key=lambda x: x.price)
            elif sort_option == 5:
                sorted_list = sorted(book_list, key=lambda x: x.count)
            elif sort_option == 6:
                sorted_list = sorted(book_list, key=lambda x: x.status)

            Book.print_header()
            for result in sorted_list:
                Book.print_book(result)

    @staticmethod
    def load_books(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                books_list = [
                    Book(book['id'], book['name'], book['publishId'], book['price'], book['count'], book['status']) for
                    book in data]
                return books_list
        except FileNotFoundError:
            return []


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'publishId': self.publishId,
            'price': self.price,
            'count': self.count,
            'status': self.status
        }

    @staticmethod
    def save_books(filename, books, overwrite=False):
        try:
            if overwrite:
                existing_data = [book.to_dict() for book in books]
            else:
                try:
                    with open(filename, 'r') as file:
                        existing_data = json.load(file)
                except FileNotFoundError:
                    existing_data = []
                if not isinstance(existing_data, list):
                    existing_data = []

                existing_data.extend([book.to_dict() for book in books])

            with open(filename, 'w') as file:
                json.dump(existing_data, file, indent=4)

            print(f'Saved {len(books)} books to {filename}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')
def Bookmenu():
    while True:
        print("\nBook Menu:")
        print("1. Enter Books")
        print("2. Print Books")
        print("3. Find Book")
        print("4. Sort Books")
        print("5. Save Books")
        print("6. Delete Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Book.enter_book()
        elif choice == '2':
            book_data = Book.load_books(Book.bookFile)
            Book.print_header()
            for book in book_data:
                Book.print_book(book)
        elif choice == '3':
            Book.find_book(Book.bookList)
        elif choice == '4':
            Book.sort_book(Book.bookList, "Name")
        elif choice == '5':
            Book.save_books(Book.bookFile, Book.bookList)
            print("Books saved to file.")
        elif choice == '6':
            book_id = input("Enter the ID of the book to delete: ")
            Book.delete_book_by_id(book_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Bookmenu()
