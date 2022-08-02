#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int letter(string text);
int word(string text);
int sentence(string text);

int main(void)
{
    //Prompt to obtain text from user
    string text = get_string("Text: ");

    //Count number of letters in text
    int letter_count = letter(text);

    //Count number of words in text
    int word_count = word(text);

    //Count number of sentences in text
    int sentence_count = sentence(text);

    //Calculating Coleman-Liau index
    float L = (float)letter_count / word_count * 100;
    float S = (float)sentence_count / word_count * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    
    //Printing response according to various grades
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index < 16)
    {
        printf("Grade %i\n", (int)round(index));
    }
    else
    {
        printf("Grade 16+\n");
    }
}

//Abstraction: Count number of letters in text
int letter(string text)
{
    int letter_count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (islower(text[i]) || isupper(text[i]))
        {
            letter_count++;
        }
    }
    return letter_count;
}

//Abstraction: Count number of words in text
int word(string text)
{
    int space_count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            space_count++;
        }
    }
    return space_count + 1;
}

//Abstraction: Count number of sentences in text
int sentence(string text)
{
    int sentence_count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        switch (text[i])
        {
            case '.':
            case '?':
            case '!':
                sentence_count++;
        }
    }
    return sentence_count;
}