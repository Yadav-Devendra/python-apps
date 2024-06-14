import re

def is_palindrome(input_value):
    """
    Check if the input (string or numeric) is a palindrome.
    
    Args:
    input_value (str or int or float): The input value to check for palindrome properties.
    
    Returns:
    bool: True if the input is a palindrome, False otherwise.
    """
    # Convert the input to string regardless of whether it's a string or a number.
    input_string = str(input_value)
    
    # Normalize the string: remove non-alphanumeric characters and convert to lower case.
    normalized_string = re.sub(r'[\W_]', '', input_string.lower())
    
    # Check if the normalized string is equal to its reverse.
    return normalized_string == normalized_string[::-1]

def main():
    try:
        # Taking input from the user
        user_input = input("Enter a string or a number to check if it is a palindrome: ")
        
        # Try to convert to a float if possible. This will check for numeric input including integers and floats.
        try:
            # Convert user input to a float if it's a numeric value
            converted_input = float(user_input)
            # If the input is an integer value (like '5' or '22'), convert it to int to remove decimal zeros.
            if converted_input.is_integer():
                converted_input = int(converted_input)
        except ValueError:
            # If there is a ValueError, then the input is not a number, keep it as a string.
            converted_input = user_input
        
        # Check if the input is valid (at least one alphanumeric character)
        if not converted_input and converted_input != 0:
            raise ValueError("The input must contain at least one alphanumeric character.")
        
        # Check if the input is a palindrome
        if is_palindrome(converted_input):
            print(f"The input '{user_input}' is a palindrome.")
        else:
            print(f"The input '{user_input}' is not a palindrome.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()