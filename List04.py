def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    numbers.pop(i)
    return i
i=int(input())
print(main([1,2,3,4,5,6,7,8,9],i))