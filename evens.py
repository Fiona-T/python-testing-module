def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            # if list not empty, then need to check number of even no.s
            evens = 0
        # if number in list is even, add it to evens
        for n in numbers:
            if n % 2 == 0:
                evens += 1
        # using evens as Truthy/Falsy - true if greater than 0, false if 0
        if evens:
            # this returns true if evens is an even number, false if not
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens(5))
