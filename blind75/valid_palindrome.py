import logging

# configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ValidPalindrome:
    def valid_palindrome(self, input_string: str) -> bool:
        logging.debug(f"checking if {input_string} is a palindrome")
        if input_string == " ":
            return input_string
        
        cleansed_string = "".join([c for c in input_string if c.isalnum()]).lower()
        reversed_string = "".join(reversed(cleansed_string))

        logging.debug(f"result is {cleansed_string == reversed_string}")
        return cleansed_string == reversed_string

def main():
    vp = ValidPalindrome()
    # input_string = "race a car"
    input_string = "A man, a plan, a canal: Panama"
    print(vp.valid_palindrome(input_string))

if __name__ == "__main__":
    main()