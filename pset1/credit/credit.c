#include <cs50.h>
#include <stdio.h>

long GetPositiveInt(void);
int DigitCount(long j);
bool LuhnAlgorithm(long number);
int Digit1(long number);
int Digit12(long number);

int main(void)
{
    //Prompt to get positive integer
    long number = GetPositiveInt();

    //Count number of digits
    int digit_count = DigitCount(number);

    //Validating against LuhnAlgorithm
    bool valid = LuhnAlgorithm(number);

    //Obtaining first digit
    int digit1 = Digit1(number);

    //obtaining first 2 digits
    int digit12 = Digit12(number);

    //Categorising invalids and various cards
    if (valid == true)
    {
        if (digit_count == 15 && (digit12 == 34 || digit12 == 37))
        {
            printf("AMEX\n");
        }
        else if (digit_count == 16 && (digit12 >= 51 && digit12 <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if (digit1 == 4 && (digit_count == 13 || digit_count == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

}

//Abstraction: Prompt to get positive integers
long GetPositiveInt(void)
{
    long n;
    do
    {
        n = get_long("Number: ");
    }
    while (n < 1);
    return n;
}

//Abstraction: Count number of digits
int DigitCount(long j)
{
    int n = 0;
    for (long i = j; i >= 1; i /= 10)
    {
        n++;
    }
    return n;
}

//Abstraction: Validation Using Luhn's Algorithm
bool LuhnAlgorithm(long number)
{
    int non_multiplied_sum = 0;
    int multiplied_sum = 0;
    int n = 0;
    for (long i = number; i >= 1; i /= 10)
    {
        int digit = i % 10;
        //Case when digit is not to be mulitplied
        if (n % 2 == 0)
        {
            non_multiplied_sum += digit;
        }
        //Case when digit is to be multiplied by 2
        else
        {
            int multiplied2 = digit * 2;
            //Cases when digit to be multiplied by 2 may be double or single digit or 0
            switch (DigitCount(multiplied2))
            {
                case 2:
                    multiplied_sum += multiplied2 % 10 + (multiplied2 / 10) % 10;
                    break;
                case 1:
                case 0:
                    multiplied_sum += multiplied2;
            }
        }
        n++;
    }
    //To Check if last digit of the sum is indeed 0
    if ((non_multiplied_sum + multiplied_sum) % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//Abstraction: Obtaining first digit
int Digit1(long number)
{
    int n;
    for (long i = number; i >= 1; i /= 10)
    {
        n = i % 10;
    }
    return n;
}

//Abstraction: Obtaining first 2 digits
int Digit12(long number)
{
    int n;
    for (long i = number; i >= 10; i /= 10)
    {
        n = i % 100;
    }
    return n;
}