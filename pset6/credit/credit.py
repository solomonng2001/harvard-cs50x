from cs50 import get_int


def main():

    # Get number from user
    number = get_positive_int("Number: ")

    # Initialise variables for convenient use later
    digit_count = count_digits(number)
    digit12 = first_2_digits(number)

    # Check if luhn algorithm test result is true, else print invalid
    if luhn_algorithm(number):

        # Checking various characteristics of american express, mastercard and visa
        if digit_count == 15 and (digit12 == 34 or digit12 == 37):
            print("AMEX")
            return
        if digit_count == 16 and digit12 >= 51 and digit12 <= 55:
            print("MASTERCARD")
            return
        if (digit_count == 13 or digit_count == 16) and int(digit12 / 10) == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


# Luhn's Algorithm
def luhn_algorithm(number):

    # Initialise to zero
    non_multiplied_sum = 0
    multiplied_sum = 0

    while True:
        # Summing all odd-placed digits
        non_multiplied_sum += int(number) % 10
        number /= 10
        if number < 1:
            break

        # Summing all even-placed or every other digit, but first checking if multiplied digit is single or double digit
        multiplied_digit = (int(number) % 10) * 2
        number /= 10
        if multiplied_digit < 10:
            multiplied_sum += multiplied_digit
        else:
            multiplied_sum += multiplied_digit % 10
            multiplied_sum += 1
        if number < 1:
            break

    # Checking if last digit of sum is 0 and return true or false
    return (multiplied_sum + non_multiplied_sum) % 10 == 0


# Return number of digits in number
def count_digits(number):
    i = 0
    while number >= 1:
        number /= 10
        i += 1
    return i


# Return first 2 digits in number
def first_2_digits(number):
    n = int(number / 10**(count_digits(number) - 2))
    return n


# Ensure input is positive integer
def get_positive_int(prompt):
    while True:
        n = get_int(prompt)
        if n > 0:
            return n
            break


if __name__ == "__main__":
    main()