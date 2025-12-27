from student import student_details

def test_student_details():
    expected_output = (
        "student usn: 01fe24bca320\n"
        "student name: rutika\n"
        "student division: E\n"
        "age: 20"
    )

    result = student_details("01fe24bca320", "rutika", "E", 20)
    assert result == expected_output
