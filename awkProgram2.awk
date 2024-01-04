{ if ($1 ~ /^[qwertasdfgbzxcv]?([yuiiophjklnm][qwertasdfgzxcbv])+$/ || /^[yuiiophjklnm]?([qwerbtasdfgzxcv][yuiiophjklnm])+$/)  print length($1), $1}
