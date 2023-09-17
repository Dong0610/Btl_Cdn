import json
import btl.utility as utility


class User:
    userList = []
    userFile = "user.json"

    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    @staticmethod
    def enter_user():
        print("Enter the number of users: ")
        num_users = int(input())

        for _ in range(num_users):
            auto_id = utility.autoID(6)
            print(f"User ID: {auto_id}")
            name = input("Enter user name: ")
            phone = input("Enter user phone: ")
            address = input("Enter user address: ")
            user = User(auto_id, name, phone, address)
            User.userList.append(user)

        while True:
            save_choice = input("Do you want to save the data (y/n)?: ").lower()
            if save_choice not in ['y', 'n']:
                continue
            if save_choice == 'y':
                User.save_users(User.userFile, User.userList)
                print("Data saved successfully!")
                break
            elif save_choice == 'n':
                print("Data not saved.")
                break

    @staticmethod
    def print_user(user):
        print(f"   {user.id.ljust(10)}{user.name.ljust(30)}{user.phone.ljust(15)}{user.address.ljust(50)}")

    @staticmethod
    def print_header():
        print(f"   {'ID'.ljust(10)}{'Name'.ljust(30)}{'Phone'.ljust(15)}{'Address'.ljust(50)}")

    @staticmethod
    def delete_user_by_id(user_id):
        users_list = User.load_users(User.userFile)
        deleted_user = None
        for user in users_list:
            if user.id == user_id:
                deleted_user = user
                users_list.remove(user)
                break

        if deleted_user:
            User.save_users(User.userFile, users_list, True)
            print(f"User with ID {deleted_user.id} has been deleted.")
        else:
            print(f"User with ID {user_id} not found.")

    @staticmethod
    def find_user(user_list):
        while True:
            print("Search by:")
            print("0: Exit.\n1: ID.\n2: Name.\n3: Phone.\n4: Address.")
            search_option = int(input("Enter your choice: "))

            if search_option == 0:
                break
            if search_option not in [1, 2, 3, 4]:
                print("Invalid choice.")
                continue

            search_term = input("Enter the search term: ")
            result_list = []

            for user in user_list:
                if search_option == 1 and user.id == search_term:
                    result_list.append(user)
                elif search_option == 2 and user.name == search_term:
                    result_list.append(user)
                elif search_option == 3 and user.phone == search_term:
                    result_list.append(user)
                elif search_option == 4 and user.address == search_term:
                    result_list.append(user)

            if len(result_list) != 0:
                User.print_header()
                for result in result_list:
                    User.print_user(result)
            else:
                print("No matching results found.")

    @staticmethod
    def find_user_in_list():
        user_list = User.load_users(User.userFile)
        userFind = User
        print(f"{len(user_list)}")
        while True:
            print("Search by:")
            print("0: Exit.\n1: ID.\n2: Name.\n3: Phone.\n4: Address.")
            search_option = int(input("Enter your choice: "))
            if search_option == 0:
                break
            if search_option not in [1, 2, 3, 4]:
                print("Invalid choice.")
                continue
            search_term = input("Enter the search term: ")
            result_list = []
            for user in user_list:
                if search_option == 1 and user.id == search_term:
                    result_list.append(user)
                elif search_option == 2 and user.name == search_term:
                    result_list.append(user)
                elif search_option == 3 and user.phone == search_term:
                    result_list.append(user)
                elif search_option == 4 and user.address == search_term:
                    result_list.append(user)

            if len(result_list) != 0:
                userFind = result_list[0]
            else:
                print("No matching results found.")
            break
        return userFind


    @staticmethod
    def sort_user(user_list, sort_key):
        while True:
            print("Sort by:")
            print("0: Exit.\n1: ID.\n2: Name.\n3: Phone.\n4: Address.")
            sort_option = int(input("Enter your choice: "))

            if sort_option == 0:
                break
            if sort_option not in [1, 2, 3, 4]:
                print("Invalid choice.")
                continue

            if sort_option == 1:
                sorted_list = sorted(user_list, key=lambda x: x.id)
            elif sort_option == 2:
                sorted_list = sorted(user_list, key=lambda x: x.name)
            elif sort_option == 3:
                sorted_list = sorted(user_list, key=lambda x: x.phone)
            elif sort_option == 4:
                sorted_list = sorted(user_list, key=lambda x: x.address)

            User.print_header()
            for result in sorted_list:
                User.print_user(result)


    @staticmethod
    def load_users(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                users_list = [User(user['id'], user['name'], user['phone'], user['address']) for user in data]
                return users_list
        except FileNotFoundError:
            return []


    @staticmethod
    def save_users(filename, users, overwrite=False):
        if overwrite:
            existing_data = [{'id': user.id, 'name': user.name, 'phone': user.phone, 'address': user.address}
                             for user in users]
        else:
            try:
                with open(filename, 'r') as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = []
            existing_data.extend([{'id': user.id, 'name': user.name, 'phone': user.phone, 'address': user.address}
                                  for user in users])
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)


def Usermenu():
    while True:
        print("\nUser Menu:")
        print("1. Enter Users")
        print("2. Print Users")
        print("3. Find User")
        print("4. Sort Users")
        print("5. Save Users")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            User.enter_user()
        elif choice == '2':
            user_data = User.load_users(User.userFile)
            User.print_header()
            for user in user_data:
                User.print_user(user)
        elif choice == '3':
            User.find_user(User.userList)
        elif choice == '4':
            User.sort_user(User.userList, "Name")
        elif choice == '5':
            User.save_users(User.userFile, User.userList)
            print("Users saved to file.")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Usermenu()
