def main(fruits,x):
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """
    fruits.append(x)
    return fruits
x=input()
fruits=[1,2,3,4,5,6]
print(main(fruits,x))