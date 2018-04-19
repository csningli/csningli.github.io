
if [ $# -lt 2 ]; then
	echo "Wrong number of arguments."
	echo "Example:  $ ./complete.sh index-body.html index.html"
else 
	echo "<html>" > $2 
	cat head.html $1 footer.html >> $2
	echo "</html>" >> $2 
fi

