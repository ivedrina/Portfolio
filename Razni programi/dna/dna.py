'''A program that identifies to whom a sequence of DNA belongs

Run your program as:
 python dna.py databases/small.csv sequences/1.txt --> output Bob.
 python dna.py databases/small.csv sequences/2.txt--> output No match
 python dna.py databases/small.csv sequences/3.txt--> output No match
 python dna.py databases/large.csv sequences/5.txt--> output Lavender
 python dna.py databases/large.csv sequences/6.txt--> output Luna
 python dna.py databases/large.csv sequences/7.txt--> output Ron'''   


import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    rows = []
    with open(sys.argv[1], mode='r')as file:
        csvFile = csv.reader(file)
        fields = next(csvFile)
        a = fields
        for line in csvFile:
            rows.append(line)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], mode='r')as f:
        txtFile = f.read()

    # Find longest match of each STR in DNA sequence

    ina = []
    for i in range(1, len(a)):
        s = longest_match(txtFile, a[i])
        ina.append(str(s))

    # Check database for matching profiles
    for j in range(len(rows)):
        if rows[j][1:len(a)] == ina:
            print(rows[j][0])
            return
    print('No match\n')

    return

 
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)
        # print(longest_run)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

