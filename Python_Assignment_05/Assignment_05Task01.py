def result(n):
    student = {'Rohan': 90, 'Siddhant': 85, 'Alice': 78, 'Hardik': 84, 'Sharvari': 72, 'John': 77}
    if n in student:
        print(n + "'s marks: ", student[n])
    else:
        print("Student not found.")
    return n

name = str(input("Enter the Students name: "))
n = name.capitalize()
res = result(n)
