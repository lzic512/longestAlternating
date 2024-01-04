BEGIN {
	pattern1 = "^([qwertasdfgzxcvb]([yuiophjklnm][qwertasdfgzxcvb])+[yuiophjklnm]?)$";
	pattern2 = "^([yuiophjklnm]([qwertasdfgzxcvb][yuiophjklnm])+[qwertasdfgzxcvb]?)$";
}

{
        if (length($1) > longest && ($1 ~ pattern1 || $1 ~ pattern2)){
		print length($1), " ", $1
        }
}

