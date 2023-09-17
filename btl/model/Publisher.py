import json
import string
import random
import btl.utility as utility

class Publisher:
    publishList = []
    publishFile = "publish.json"

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    @staticmethod
    def enter_publish():
        print("Nhap so luong: ")
        sum = int(input())  # Convert the input to an integer
        count = 0
        for _ in range(sum):
            auto_id =utility.autoID(6)
            count = count + 1
            print(f"Publist:{count} ")
            print("ID: " + auto_id)
            print("Nhap ten: ", end="")
            name = input()
            print("Nhap dia chi: ", end="")
            address = input()
            publisher = Publisher(auto_id, name, address)
            Publisher.publishList.append(publisher)
        while True:
            print("Co luu lai danh sach da nhap khong (y/n)?: ", end="")
            tt = input()
            if tt not in ['y', 'n']:
                continue
            if tt == 'y':
                Publisher.save_publishers(Publisher.publishFile, Publisher.publishList)
                print("Luu file thanh cong!")
                break
            elif tt == 'n':
                print("Du lieu chua duoc luu")
                break

    @staticmethod
    def delete_publisher_by_id(publisher_id):
        # Load the list of publishers from the file
        publishers_list = Publisher.load_publishers(Publisher.publishFile)

        # Find the publisher with the specified ID and remove it
        deleted_publisher = None
        for publisher in publishers_list:
            if publisher.id == publisher_id:
                deleted_publisher = publisher
                publishers_list.remove(publisher)
                break

        if deleted_publisher:
            # Save the updated list back to the file
            Publisher.save_publishers(Publisher.publishFile, publishers_list,True)
            print(f"Publisher with ID {deleted_publisher.id} has been deleted.")
        else:
            print(f"Publisher with ID {publisher_id} not found.")

    @staticmethod
    def print_publisher(publish):
        print(f"   {publish.id.ljust(10)}{publish.name.ljust(30)}{publish.address.ljust(50)}")

    @staticmethod
    def print_header():
        print(f"   {'ID'.ljust(10)}{'Name'.ljust(30)}{'Address'.ljust(50)}")

    @staticmethod
    def find_publish(listPublish):
        while True:
            print("Tim kiem theo:")
            print("0: Dung lai.\n1: ID.\n2: Name.\n3: Address.\nNhap lua chon:", end="")
            luachon = int(input())

            if luachon == 0:
                break
            if luachon not in [1, 2, 3]:
                print("Lua chon khong hop le.")
                continue
            search_term = input("Nhap thong tin tim kiem: ", end="")
            listResult = []
            for data in listPublish:
                if luachon == 1 and data.id == search_term:
                    listResult.append(data)
                elif luachon == 2 and data.name == search_term:
                    listResult.append(data)
                elif luachon == 3 and data.address == search_term:
                    listResult.append(data)

            if len(listResult) != 0:
                Publisher.print_header()
                for result in listResult:
                    Publisher.print_publisher(result)
            else:
                print("Khong tim thay ket qua.")

    @staticmethod
    def sort_publish(listPublish, sort_key):
        while True:
            print("Sap xep theo:")
            print("0: Dung lai.\n1: ID.\n2: Name.\n3: Address.\nNhap lua chon: ", end="")
            luachon = int(input())
            if luachon == 0:
                break
            if luachon not in [1, 2, 3]:
                print("Lua chon khong hop le.")
                continue

            if luachon == 1:
                sorted_list = sorted(listPublish, key=lambda x: x.id)
            elif luachon == 2:
                sorted_list = sorted(listPublish, key=lambda x: x.name)
            elif luachon == 3:
                sorted_list = sorted(listPublish, key=lambda x: x.address)

            Publisher.print_header()
            for result in sorted_list:
                Publisher.print_publisher(result)

    @staticmethod
    def load_publishers(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                publishers_list = [Publisher(publisher['id'], publisher['name'], publisher['address']) for publisher in
                                   data]
                return publishers_list
        except FileNotFoundError:
            return []

    @staticmethod
    def save_publishers(filename, publishers, overwrite=False):
        if overwrite:
            existing_data = [{'id': publisher.id, 'name': publisher.name, 'address': publisher.address}
                             for publisher in publishers]
        else:
            try:
                with open(filename, 'r') as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = []
            existing_data.extend([{'id': publisher.id, 'name': publisher.name, 'address': publisher.address}
                                  for publisher in publishers])
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

    @staticmethod
    def editPublisher():
        listPublish = Publisher.load_publishers(Publisher.publishFile)
        while True:
            Publisher.print_header()
            for data in listPublish:
                Publisher.print_publisher(data)
            print("1: Tiep tuc\n0: Dung lai.\nNhap lua chon: ", end="")
            lc = int(input())
            if lc not in [0, 1]:
                print("Lua chon khong hop le.\n")
                continue
            if lc == 1:
                print("\nNhap id: ", end="")
                edit_id = input()
                found = False
                for publisher in listPublish:
                    if publisher.id == edit_id:
                        print("Nhap thong tin moi:")
                        new_name = input("Nhap ten moi: ")
                        new_address = input("Nhap dia chi moi: ")
                        publisher.name = new_name
                        publisher.address = new_address
                        found = True
                        break

                if found:
                    Publisher.save_publishers(Publisher.publishFile, listPublish)
                    print("Da cap nhat thong tin.")
                else:
                    print("Khong tim thay Publisher co ID nhu vay.")
            else:
                print("Dung sua thong tin.")
                break


def Publishmenu():
    while True:
        print("\nMenu:")
        print("1. Enter Publishers")
        print("2. Print Publishers")
        print("3. Find Publisher")
        print("4. Sort Publishers")
        print("5. Edit Publisher")
        print("6. Save Publishers")
        print("5. Delete Publisher")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Publisher.enter_publish()
        elif choice == '2':
            listData = Publisher.load_publishers(Publisher.publishFile)
            Publisher.print_header()
            for data in listData:
                Publisher.print_publisher(data)
        elif choice == '3':
            Publisher.find_publish(Publisher.publishList)
        elif choice == '4':
            Publisher.sort_publish(Publisher.publishList, "Name")
        elif choice == '5':
            Publisher.editPublisher()
        elif choice == '6':
            Publisher.save_publishers(Publisher.publishFile, Publisher.publishList)
            print("Publishers saved to file.")
        elif choice == '7':
            publisher_id = input("Enter the ID of the publisher to delete: ")
            Publisher.delete_publisher_by_id(publisher_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")








if __name__ == "__main__":
    Publishmenu()
