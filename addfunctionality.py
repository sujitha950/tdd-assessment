def add_numbers(numbers):
    if not numbers:
        return 0
    return int(numbers)

def test_add():
    assert add("") == 0
    assert add("1") == 1
    print("Basic strings and single numbers are passed")

test_add()
