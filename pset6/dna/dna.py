from sys import argv, exit
import csv

# Copy of database (list of dictionaries)
data_list = []

# Overall count of STRs in DNA sequence
str_dict = {
    "AGATC": 0,
    "TTTTTTCT": 0,
    "AATG": 0,
    "TCTAG": 0,
    "GATA": 0,
    "TATC": 0,
    "GAAA": 0,
    "TCTG": 0
}


def main():

    # Ensure correct usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Read database into memory as list of dictionaries
    with open(argv[1], "r") as data_file:
        data_reader = csv.DictReader(data_file)
        for individual in data_reader:
            data_list.append(individual)

        # Read all STR combinations into memory as list including header "name"
        str_list = data_reader.fieldnames
        del str_list[0]

    # Read DNA sequence into memory as string
    with open(argv[2], "r") as sequence_file:
        sequence = sequence_file.read()

    # Update overall counts of STRs in STR dictionary
    for i in str_list:
        str_dict[i] = count_str(sequence, i)

    # Check if all STR counts in DNA sequence matches database
    for individual in data_list:
        matches = 0
        for i in str_list:
            if str_dict[i] == int(individual[i]):
                matches += 1
        
        # Print name if matches
        if matches == len(str_list):
            print(individual["name"])
            exit(0)
    
    # Else print no match
    print("No match")


# Count maximum successive number of particular STR in given DNA sequence
def count_str(sequence, str_sequence):
    max_str_count = 0
    
    # Iterating through other starting points
    for j in range(len(str_sequence)):
        successive_str_count = 0
        
        # Iterating by block of STR length
        for i in range(j, len(sequence) - ((len(sequence) - j) % len(str_sequence)) - len(str_sequence) + 2, len(str_sequence)):
            if sequence[i:i + len(str_sequence)] != str_sequence:
                successive_str_count = 0
            else:
                successive_str_count += 1
                
                # Updating maximum STR count
                if max_str_count < successive_str_count:
                    max_str_count = successive_str_count
                    
    # Output of function to be inteeger reflecting maximum STR count
    return max_str_count


if __name__ == "__main__":
    main()