# gitcomments
Retrieve GitHub pull request review comments and populate a vim quickfix list.

### Setup    
Clone this repository(probably into your home directory):   
    `cd ~ && git clone git@github.com:JRonhovde/gitcomments.git`

Add the bash script source to your `.bash_profile` or `.bashrc`:    
    `source ~/gitcomments/gitcomments.sh`    

Follow the directions in `gitcomments.json.example` to set up your Authentication info.    

Once setup is complete, just use the command `gitcomments <branchname>` (excluding a branch name will cause gitcomments to use the current branch) while in a git repository. If the branch is associated with a Pull Request which has valid review comments, those comments will be retrieved and stored in a file in vim quickfix format. Vim will then launch with the list loaded. Navigate each item using `:cn` and `:cp`.
