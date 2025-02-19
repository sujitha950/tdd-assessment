def add_numbers(numbers):
    if not numbers:
        return 0
        nums = [int(n) for n in numbers.split(',')]
    return sum(nums)
    

def test_add():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,5") == 6
    print("Added comma seperated numbers are passed")

test_add()
