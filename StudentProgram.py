import StudentClass as sc


StudentID = 1001
Name = 'John'
dob = '10/11/2001'
classification = 'junior'


student1 = sc.Student(StudentID, Name, dob, classification)


student1.calc_age()
student1.calc_reg()

print(f'Student age is {student1.get_age()}')

print(f'Student can register between {student1.get_regDate()}')
