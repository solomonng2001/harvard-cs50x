#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Greeting user and asking name
    string name = get_string("What's your name? ");
    
    //Addressing user with user's name
    printf("hello, %s\n", name);
}