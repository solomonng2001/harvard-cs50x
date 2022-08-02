#include <cs50.h>
#include <stdio.h>

int get_population(void);

int main(void)
{
    //Prompt for start size
    printf("Start ");
    int start = get_population();

    //Prompt for end size
    int end;
    do
    {
        printf("End ");
        end = get_population();
    }
    while (end < start);

    //Calculate number of years until intended population
    int year = 0;
    int population = start;
    while (population < end)
    {
        population = population + (population / 3) - (population / 4);
        year++;
    }

    //Print number of years
    printf("Years: %i\n", year);
}

//Abstraction: Ensure valid population of greater than or equal to 9
int get_population(void)
{
    int n;
    do
    {
        
        n = get_int("size: ");
    }
    while (n < 9);
    return n;
}