BEGIN {
    left = "qwertasdfgzxcvb";
    right = "yuiophjklnm";
    longest_word = "";
    max_length = 0; 
}

{
    for (word_num = 1; word_num <= NF; word_num++) {
        word = $1;
        side = ""; 
        alternating = 1;

        for (i = 1; i <= length(word); i++) {
            char = substr(word, i, 1);

            if (index(left, char) > 0) {
                if (side == "left") {
                    alternating = 0;
                    break;
                }
                side = "left";
            } else if (index(right, char) > 0) {
                if (side == "right") {
                    alternating = 0;
                    break;
                }
                side = "right";
            } else {
                # Non-letter character
                alternating = 0;
                break;
            }
        }

        if (alternating && length(word) > max_length) {
            longest_word = word;
            max_length = length(word);
        }
    }
}

END {
    if (max_length > 0) {
        print "Longest alternating word: " longest_word;
    } else {
        print "No alternating words found.";
    }
}
