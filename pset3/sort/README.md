[Lab 3: Sort](https://cs50.harvard.edu/x/2021/labs/3/#lab-3-sort)
=================================================================

Analyze three sorting programs to determine which algorithms they use.

[Background](https://cs50.harvard.edu/x/2021/labs/3/#background)
----------------------------------------------------------------

Recall from lecture that we saw a few algorithms for sorting a sequence of numbers: selection sort, bubble sort, and merge sort.

-   Selection sort iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
-   Bubble sort compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
-   Merge sort recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.

[Getting Started](https://cs50.harvard.edu/x/2021/labs/3/#getting-started)
--------------------------------------------------------------------------

1.  Log into [ide.cs50.io](https://ide.cs50.io/) using your GitHub account.
2.  In your terminal window, run `wget https://cdn.cs50.net/2020/fall/labs/3/lab3.zip` to download a Zip file of the lab distribution code.
3.  In your terminal window, run `unzip lab3.zip` to unzip (i.e., decompress) that Zip file.
4.  In your terminal window, run `cd lab3` to change directories into your `lab3`directory.

[Instructions](https://cs50.harvard.edu/x/2021/labs/3/#instructions)
--------------------------------------------------------------------

Provided to you are three already-compiled C programs, `sort1`, `sort2`, and `sort3`. Each of these programs implements a different sorting algorithm: selection sort, bubble sort, or merge sort (though not necessarily in that order!). Your task is to determine which sorting algorithm is used by each file.

-   `sort1`, `sort2`, and `sort3` are binary files, so you won't be able to view the C source code for each. To assess which sort implements which algorithm, run the sorts on different lists of values.
-   Multiple `.txt` files are provided to you. These files contain `n` lines of values, either reversed, shuffled, or sorted.
    -   For example, `reversed10000.txt` contains 10000 lines of numbers that are reversed from `10000`, while `random100000.txt` contains 100000 lines of numbers that are in random order.
-   To run the sorts on the text files, in the terminal, run `./[program_name] [text_file.txt]`.
    -   For example, to sort `reversed10000.txt` with `sort1`, run `./sort1 reversed10000.txt`.
-   You may find it helpful to time your sorts. To do so, run `time ./[sort_file] [text_file.txt]`.
    -   For example, you could run `time ./sort1 reversed10000.txt` to run `sort1` on 10,000 reversed numbers. At the end of your terminal's output, you can look at the `real` time to see how much time actually elapsed while running the program.
-   Record your answers in `answers.txt`, along with an explanation for each program, by filling in the blanks marked `TODO`.[Specification](https://cs50.harvard.edu/x/2021/psets/2/substitution/#specification)
------------------------------------------------------------------------------------

Design and implement a program, `substitution`, that encrypts messages using a substitution cipher.

-   Implement your program in a file called `substitution.c` in a directory called `substitution`.
-   Your program must accept a single command-line argument, the key to use for the substitution. The key itself should be case-insensitive, so whether any character in the key is uppercase or lowercase should not affect the behavior of your program.
-   If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` (which tends to signify an error) immediately.
-   If the key is invalid (as by not containing 26 characters, containing any character that is not an alphabetic character, or not containing each letter exactly once), your program should print an error message of your choice (with `printf`) and return from `main` a value of `1` immediately.
-   Your program must output `plaintext:` (without a newline) and then prompt the user for a `string` of plaintext (using `get_string`).
-   Your program must output `ciphertext:` (without a newline) followed by the plaintext's corresponding ciphertext, with each alphabetical character in the plaintext substituted for the corresponding character in the ciphertext; non-alphabetical characters should be outputted unchanged.
-   Your program must preserve case: capitalized letters must remain capitalized letters; lowercase letters must remain lowercase letters.
-   After outputting ciphertext, you should print a newline. Your program should then exit by returning `0` from `main`.

<sub>*Assignment description taken from https://cs50.harvard.edu/x/2021/*</sub>
