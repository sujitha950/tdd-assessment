def add_numbers(numbers):
    if not numbers:
        return 0
        numbers = numbers.replace('\n', ',')
        nums = [int(n) for n in numbers.split(',')]
    return sum(nums)
    

def test_add():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,5") == 6
    assert add("1\n2,3") == 6
    print("Handled new line logic here")

test_add()
