def add_numbers(numbers):
    if not numbers:
        return 0
        end = numbers.find('\n')
        # removing delimiters
        delimiter = numbers[2:end]
        numbers = numbers[end + 1:]
        numbers = numbers.replace(delimiter, ',')
        numbers = numbers.replace('\n', ',')
        negative_nums = [n for n in nums if n < 0]
    if negative_nums:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negative_nums))}")
        nums = [int(n) for n in numbers.split(',')]
    return sum(nums)
    

def test_add():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,5") == 6
    assert add("1\n2,3") == 6
    assert add("//;\n1;2") == 3
    assert add("//|\n1|2|3") == 6
    try:
        print(add("1,-2")) 
       
    except ValueError as e:
        print(e)
    print("Handled delimiter logic here")

test_add()
