#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool Alphabetical(int length, string array);
bool NoRepetition(int length, string array);

int main(int argc, string argv[])
{
    //Case when number of command line arguments is not 1
    if (argc != 2)
    {
        printf("Usage: ./Substitution Key\n");
        return 1;
    }
    //Case when number of command line arguments is 1
    else
    {
        //Calculate number of characters in key
        int length = strlen(argv[1]);
        
        //Case when key does not contain 26 characters
        if (length != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        //Case when key does not contain only alphabets
        else if (Alphabetical(length, argv[1]) == false)
        {
            printf("Key must be alphabetical.\n");
            return 1;
        }
        //Case when key contains repeated characters
        else if (NoRepetition(length, argv[1]) == false)
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
        else
        {
            //Encryption of input using key
            string input = get_string("plaintext: ");
            char output[strlen(input)];
            for (int i = 0, n = strlen(input); i < n; i++)
            {
                //Converting lowercase back to lowercase
                if (islower(input[i]))
                {
                    output[i] = tolower(argv[1][input[i] - 97]);
                }
                //Converting uppercase back to uppercase
                else if (isupper(input[i]))
                {
                    output[i] = toupper(argv[1][input[i] - 65]);
                }
                //Preservingg non-alphabetical characters unchanged
                else
                {
                    output[i] = input[i];
                }
            }
            output[strlen(input)] = '\0';
            
            //Printing encrypted message
            printf("ciphertext: %s\n", output);
            return 0;
        }
    }
}

//Abstraction: Check if all characters in string is alphabetical
bool Alphabetical(int length, string array)
{
    int alphabet = 0;
    for (int i = 0; i < length ; i++)
    {
        if (isalpha(array[i]))
        {
            alphabet++;
        }
    }
    if (alphabet == length)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//Abstraction: Checking for repeated characters
bool NoRepetition(int length, string array)
{
    int repeat = 0;
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            //Since repetition may involve uppercase and lowercase of same alphabet
            if (array [i] == tolower(array [j]) || array [i] == toupper(array [j]))
            {
                repeat++;
            }
        }
    }
    if (repeat == length)
    {
        return true;
    }
    else
    {
        return false;
    }
}