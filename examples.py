examples = [
    {
        "id": "is_even",
        "spec": "Write a function that returns True if a number is even, False otherwise.",
        "solution": "def is_even(x): return x % 2 == 0",
        "test_code": """
            def test_is_even():
                assert is_even(2) == True
                assert is_even(3) == False
                assert is_even(0) == True
        """
    },
    {
        "id": "factorial",
        "spec": "Implement a recursive function that returns the factorial of a non-negative integer.",
        "solution": "def factorial(n): return 1 if n == 0 else n * factorial(n - 1)",
        "test_code": """
            def test_factorial():
                assert factorial(0) == 1
                assert factorial(5) == 120
                assert factorial(3) == 6
        """
    },
    # Add more examples here...
]
