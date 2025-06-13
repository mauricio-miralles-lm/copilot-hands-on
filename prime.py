def is_prime(n):
    """Check if a number is prime."""
    # Handle special cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check only values of form 6k±1 up to sqrt(n)
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# create a function to do 5 unit tests of the code above
def test_is_prime():
    """Run unit tests for the is_prime function."""
    assert is_prime(2) == True, "Test case 1 failed"
    assert is_prime(3) == True, "Test case 2 failed"
    assert is_prime(4) == False, "Test case 3 failed"
    assert is_prime(29) == True, "Test case 4 failed"
    assert is_prime(100) == False, "Test case 5 failed"
    
    print("All test cases passed!")
