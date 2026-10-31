class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(self,other_obj):
        self.student_list.append(other_obj)
class Student:
    def __init__(self,student_id,name,department):
        self._student_id = student_id
        self._name = name
        self._department = department
        self.__is_enrolled = False
    def enroll_student(self):
        if self.__is_enrolled:
            print("Trying to enroll a student who is already enrolled.")
        else :
            self.__is_enrolled = True
            print(f"Student {self._student_id} has been enrolled")
    def drop_student(self):
        if not self.__is_enrolled:
            print("Trying to drop a student who is not enrolled.")
        else :
            self.__is_enrolled = False
            print(f"Student {self._student_id} has been dropped")
    def view_student_info(self):
        print(f'ID: {self._student_id}, Name: {self._name},Department: {self._department} ,Enrolled: {self.__is_enrolled}')

st_database = StudentDatabase()
a = Student('C151',"Ayan Rahman Khan","CSE")
b = Student('C286',"Zayn Malik Chowdhury","CSE")
c = Student('E360',"Hamza Tariq Ahmed","EEE")
st_database.add_student(a)
st_database.add_student(b)
st_database.add_student(c)

while True:
    print("\n--- student Management Menu ---\n1. View All Students\n2. Enroll Student\n3. Drop Student\n4. Exit")
    choice = int(input("Enter your choice (1 - 4): "))

    if choice == 1 :
        for i in st_database.student_list:
            i.view_student_info()
    elif choice == 2 :
        flag = True
        st_id = str(input("Enter student ID to Enroll: "))
        for i in st_database.student_list:
            if(i._student_id == st_id):
                i.enroll_student()
                flag = False
                break
        if flag : print("Invalid student ID when enrolling or dropping a student.")
    elif choice == 3 :
        flag = True
        st_id = str(input("Enter student ID to Enroll: "))
        for i in st_database.student_list:
            if(i._student_id == st_id):
                i.drop_student()
                flag = False
                break
        if flag : print("Invalid student ID when enrolling or dropping a student.")
        
    elif choice == 4 :
        break