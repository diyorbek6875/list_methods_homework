def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    fruits.insert(i,x)

    return fruits
i=int(input())
x=(input())
print(main([1,2,3,4,5],x,i))