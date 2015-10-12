# !bin/bash
gitcomments() {
    FILE="/usr/tmp/$USER-gitcomments.txt"
    if [ -n "$1" ]
    then
        python ~/gitcomments/gitcomments.py $1 $FILE && vim "+copen | cfile $FILE"
    else
        python ~/gitcomments/gitcomments.py $(git rev-parse --abbrev-ref HEAD) $FILE && vim "+copen | cfile $FILE"
    fi
}
alias vimgc='vim "+copen | cfile /usr/tmp/'$USER'-gitcomments.txt"'
