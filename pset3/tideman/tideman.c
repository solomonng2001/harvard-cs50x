#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates & number of candidates
string candidates[MAX];
int candidate_count;

//2D array of pairs & number of pairs
pair pairs[MAX * (MAX - 1) / 2];
int pair_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool cycle(int start, int edge, int non_edge);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);
        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        for (int j = 0, m = candidate_count - i - 1; j < m; j++)
        {
            preferences[ranks[i]][ranks[i + j + 1]] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0, n = candidate_count - 1; i < n; i++)
    {
        for (int j = 0, m = candidate_count - 1 - i; j < m; j++)
        {
            if (preferences[i][i + 1 + j] > preferences[i + j + 1][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = i + j + 1;
                pair_count++;
            }
            else if (preferences[i + j + 1][i] > preferences[i][i + j + 1])
            {
                pairs[pair_count].winner = i + j + 1;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int swap_count;
    do
    {
        swap_count = 0;
        for (int i = 0, n = pair_count - 1; i < n; i++)
        {
            //Use of Bubble Sort to check if neighbouring pair has greater strength of victory
            if (preferences[pairs[i + 1].winner][pairs[i + 1].loser] > preferences[pairs[i].winner][pairs[i].loser])
            {
                pair swap;
                swap = pairs[i];
                pairs[i] = pairs[i + 1];
                pairs[i + 1] = swap;
                swap_count++;
            }
        }
    }
    while (swap_count != 0);
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0, n = pair_count; i < n; i++)
    {
        if (!cycle(pairs[i].winner, pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

//Checking if cycle exists
bool cycle(int start, int edge, int non_edge)
{
    //Base case: recursively prior loser is current winner (function has looped through 1 complete cycle)
    if (non_edge == start)
    {
        return true;
    }
    //Recursively checking if current loser is also a winner to another candidate
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        if (locked[non_edge][i])
        {
            if (cycle(start, non_edge, i))
            {
                return true;
            }
        }
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        int true_count = 0;
        for (int j = 0, m = candidate_count; j < m; j++)
        {
            if (locked[j][i])
            {
                true_count++;
            }
        }
        //Winner or source must not be a loser to any other candidate
        if (true_count == 0)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
    return;
}