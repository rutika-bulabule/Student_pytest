def student_details(usn, name, division, age):
    result = (
        f"student usn: {usn}\n"
        f"student name: {name}\n"
        f"division: {division}\n"
        f"age: {age}"
    )
    return result


if __name__ == "__main__":
    
    usn = "01fe24bca320"
    name = "rutika"
    division = "E"
    age = 20

    print(student_details(usn, name, division, age))