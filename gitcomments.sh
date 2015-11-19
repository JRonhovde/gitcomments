# !bin/bash
gitcomments() {
    FILE="/usr/tmp/$USER-gitcomments.txt"
    if [ -n "$1" ]
    then
        python ~/gitcomments/gitcomments.py $1 $FILE $(git config --get remote.origin.url) && vim "+copen | cfile $FILE"
    else
        python ~/gitcomments/gitcomments.py $(git rev-parse --abbrev-ref HEAD) $FILE $(git config --get remote.origin.url) && vim "+copen | cfile $FILE"
    fi
}
_gitcomments() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    BRANCHES="$(git branch | tr -d '\n')" 
    COMPREPLY=( $(compgen -W "$BRANCHES" -- $cur ) )
    return 0
}
complete -F _gitcomments gitcomments
alias vimgc='vim "+copen | cfile /usr/tmp/'$USER'-gitcomments.txt"'
