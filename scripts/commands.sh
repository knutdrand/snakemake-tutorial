awk '{t+=($3-$2)*$4;n+=($3-$2)}END{print t/n}' 
