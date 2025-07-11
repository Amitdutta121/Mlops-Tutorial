class employee:

    __user_count = 0

    def __init__(self):
        employee.__user_count += 1
        self.id = employee.__user_count
        self.salary = 50000
        self.designation = "SWE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

    def get_number_of_users(self):
        print("Total users: ", self.__user_count)





sam = employee()
print(sam.id)
sam1 = employee()
print(sam1.id)
sam2 = employee()
print(sam2.id)


sam2.get_number_of_users()