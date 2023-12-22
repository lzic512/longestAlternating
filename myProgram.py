from english_words import get_english_words_set
import sys

# Finds the longest word that is defined as sequential letters alteranting sides of the keyboard
def longesterAlternating():
    if len(sys.argv) != 2:
        return
    my_dictionary = sys.argv[1]
    # Get words from a specified dictionary
    english_words_set = getWordList(my_dictionary)
    # I sort it so that I always get the same answer
    my_set = sorted(english_words_set)
    # Checks the side we previously were on, we start by making the checker apply to both left and right
    # I denote right as 0 and left as 1, 2 is denoted as the start of a word
    side_checker = 2
    # Stores the longest alterating word
    longest = ""
    # This is how I define a word as on the "left" side of the keyboard
    left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', 'Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V', 'B']
    # This is how I define a word as on the "right" side of the keyboard
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', 'Y', 'U', 'I', 'O', 'P', 'H', 'J', 'K', 'L', 'N', 'M']
    # Go through each word in the set
    for curr_word in my_set:
        # If the length of the word is less than the length of the longest so far, just skip it
        if len(curr_word) < len(longest):
            continue
        # Where we will build each word, to check its length against itself, to see if we have reached the end of the word
        temp = ""
        # Go through each letter of each word
        for curr_letter in curr_word:
            # If the current letter is on the left side of the keyboard
            if curr_letter in left:
                # If the previous letter was on the right, or it is the beginning of the word we change sideChecker to left, and add to temp
                if side_checker == 0 or side_checker == 2:
                    temp = temp + curr_letter
                    side_checker = 1
                # Otherwise (if sideChecker is 1) we change sideCheker to 2, to signal that we are restarting our word, and reset temp
                else:
                    side_checker = 2
                    temp = "" 
                    break
                # If the length of temp is equal to the length of the current word, we are done building the word, so we then replace it as the longest
                # We are essentially comparing the built word to the completed word itself, to see if we have made it though the entire word
                if len(temp) == len(curr_word):
                    longest = temp
            elif curr_letter in right:
                # If the previous letter was on the left, or it is the beginning of the word we change sideChecker to right, and add to temp
                if side_checker == 1 or side_checker == 2:
                    temp = temp + curr_letter
                    side_checker = 0
                else:
                    # Otherwise (if sideChecker is 0) we change sideCheker to 2, to signal that we are restarting our word, and reset temp
                    side_checker = 2
                    temp = "" 
                    break
                # If the length of temp is equal to the length of the current word, we are done building the word, so we then replace it as the longest
                # We are essentially comparing the built word to the completed word itself, to see if we have made it though the entire word
                if len(temp) == len(curr_word):
                    longest = temp
    # Just return the longest word
    return longest

def getWordList(dictionary):
    word_list = []
    f = open("/../../usr/share/dictd/" + dictionary + ".index")
    for x in f:
        if x != "":
            line = x.split()
            if line[0].isalpha():
                word_list.append(line[0])
    return word_list

def main():
    print("Longest alternating word in this dictionary: " + longesterAlternating())

if __name__ == "__main__":
    main()
