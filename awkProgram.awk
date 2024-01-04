BEGIN {
	pattern1 = "^([qwertasdfgzxcvb]([yuiophjklnm][qwertasdfgzxcvb])+[yuiophjklnm]?)$";
	pattern2 = "^([yuiophjklnm]([qwertasdfgzxcvb][yuiophjklnm])+[qwertasdfgzxcvb]?)$";
}

{
        if (length($1) > longest && ($1 ~ pattern1 || $1 ~ pattern2)){
	    longest = length($1);
            longestWord = $1;
        }
}

END {
    print "Longest alternating word:", longestWord;
}
