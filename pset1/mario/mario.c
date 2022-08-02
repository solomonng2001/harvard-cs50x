#include <cs50.h>
#include <stdio.h>

int get_valid_height(void);
void space(int n);
void hashtag(int n);

int main(void)
{
    //Prompt for valid height
    int height = get_valid_height();
    
    //Print spaces and hashtags until required height
    for (int i = 0; i < height; i++)
    {
        space(height - i - 1);
        hashtag(i + 1);
        space(2);
        hashtag(i + 1);
        printf("\n");
    }
}

//Abstraction: Prompt for valid height from 1 to 8
int get_valid_height(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

//Abstraction: Print n number of blank spaces
void space(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

//Abrstraction: Print n number of #
void hashtag(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}