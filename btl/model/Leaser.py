import datetime
import btl.model.Users as users
import btl.utility as utility
class Leaser:
    def __init__(self, id, name, user, borrowDate, returnDate):
        self.id = id
        self.name = name
        self.user = user
        self.borrowDate = borrowDate
        self.returnDate = returnDate
    @staticmethod
    def createLease():
        print("_____________________TAO PHIEU MUON___________________________")
        leaseID=utility.autoID(8)
        print(f"ID: {leaseID}")
        borrowDate = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"Ngay tao: {borrowDate}")
        returnDate = input("Ngay tra sach: ")
        print("\n______________________________________________________________\nTHONG TIN NGUOI MUON:")
        userModel = users.User
        while True:
            isNewUser = input("Lan dau muon (y, n): ")
            if isNewUser not in ['y', 'n']:
                print("Lua chon khong dung")
                continue
            if isNewUser == "y":
                auto_id = utility.autoID(6)
                print(f"User ID: {auto_id}")
                name = input("Enter user name: ")
                phone = input("Enter user phone: ")
                address = input("Enter user address: ")
                userModel = users.User(auto_id, name, phone, address)
                break
            else:
                print("Tim kiem khach hang: ")
                userModel = users.User.find_user_in_list()

                if userModel is not None:
                    break
                else:
                    print("Khong tim thay nguoi dung.")

        print("\n______________________________________________________________\nTHEM SACH MUON:")
        count =0
        while True:
            count= count+1
            iscontinue=input("Co tiep tuc khong (y,n): ")
            if iscontinue  not in ['y', 'n']:
                print("Lua chon khong dung")
                continue
            if iscontinue == 'y':

                print("")
            else:
                print("Dung them!.")
                break

Leaser.createLease()