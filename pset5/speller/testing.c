// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 100000;

// Hash table
node *table[N];

// Number of words in dictionary
unsigned int word_count = 0;

//Function Prototype
bool find(node *trav, const char *word);
void destroy(node *trav);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Recursively find word from hash table by traversing
    return find(table[hash(word)], word);
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Make copy of word to convert to lower case later
    char word_copy[LENGTH + 1];
    strcpy(word_copy, word);

    // Source: http://www.cse.yorku.ca/~oz/hash.html
    // Original credits to  Daniel J. Bernstein
    unsigned long hash = 5381;
    int c;
    int i = 0;
    while ((c = tolower(word_copy[i++])))
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //Variables
    char word[LENGTH + 1];

    // Open to read dictionary file
    FILE *dictionary_ptr = fopen(dictionary, "r");
    if (dictionary_ptr == NULL)
    {
        return false;
    }

    // Copy every string from dictionary file to unique location in hash table
    while (fscanf(dictionary_ptr, "%s", word) != EOF)
    {
        // Create new node containing copied word from dictionary file
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);

        // Insertion of node into unique location in hash table
        unsigned int hash_value = hash(word);
        n->next = table[hash_value];
        table[hash_value] = n;

        // Keep count of number of words in dictionary for size function later
        word_count++;
    }

    // Close dictionary file and free memory
    fclose(dictionary_ptr);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // For every element in hash table
    for (int i = 0, n = N; i < n; i++)
    {
        //Traverse down each chain and delete nodes until trav reaches NULL
        node *trav = table[i];
        while (trav != NULL)
        {
            node *tmp = trav->next;
            free(trav);
            trav = tmp;
        }

        //Check that trav has traversed to last chain and emptied last chain
        if (i == n - 1 && trav == NULL)
        {
            return true;
        }
    }
    return false;
}

// Abstraction: recursively search for word in hash table
bool find(node *trav, const char *word)
{
    if (trav == NULL)
    {
        return false;
    }
    else if (strcasecmp(trav->word, word) == 0)
    {
        return true;
    }
    else
    {
        return find(trav->next, word);
    }
}