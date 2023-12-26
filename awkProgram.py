import subprocess
import sys

def longesterAlternating(my_dictionary):

    # Get number of lines in the dictionary, and print it out
    subprocess.run(["awk", 'END {print "Number of words in the file:", NR}', "/../../usr/share/dictd/" + my_dictionary + ".index"])


def main():
    for line in sys.stdin:
        longesterAlternating(line.rstrip())
        break

if __name__ == "__main__":
    main()
