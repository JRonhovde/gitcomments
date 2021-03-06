#!/usr/bin/python
#Version 1.0 - 2015-10-12

import json
import sys
import os
import re
import inspect
import requests


parentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
jsonFile = parentDir+'/gitcomments.json'
if os.path.isfile(jsonFile):
    with open(jsonFile) as data_file:
        try:
            data = json.load(data_file)
        except:
            sys.exit(jsonFile+' is not a valid JSON file')
else:
    sys.exit('Could not find '+jsonFile+', see gitcomments.json.example for instructions')

username = data['username']
token = data['token']

branchname = sys.argv[1]
filename = sys.argv[2]
repo = sys.argv[3]

repoObj = re.match(r'(https\:\/\/github\.com\/|git\@github\.com\:)([^\/]*)\/([^.]*)',str(repo))
try:
    repoOwner = repoObj.group(2)
    repoName = repoObj.group(3)
except:
    sys.exit('Could not retrieve repository information, make sure you are in a git repository.')

getPullRequestURL = "https://api.github.com/repos/"+repoOwner+"/"+repoName+"/pulls?head="+repoOwner+":"+branchname+"&access_token="+token
try:
     prURL = requests.get(getPullRequestURL).json()[0]['review_comments_url']
except:
    sys.exit('Invalid branch. Check that your branch is spelled correctly. Also check that your branch is associated with a pull request on GitHub')

getCommentsURL = prURL+"?per_page=100&access_token="+token
try:
    commentList = requests.get(getCommentsURL).json()
except:
    sys.exit('No result from GitHub API. Check to make sure your branch, "'+branchname+'" is associated with a Pull Request on GitHub.')

if len(commentList) == 0:
    sys.exit("There are no review comments on this pull request")
myfile = open(filename, 'w+')
mySet = set()
for comment in commentList:
    if str(comment['position']) == 'None':
        continue

    path = comment['path']
    locationObj = re.match(r'@@ -\d+,\d+ \+(\d+)',comment['diff_hunk'])
    newLineObj = re.findall(r"\n[+ ]", comment['diff_hunk'])
    offset = len(newLineObj)
    location = int(locationObj.group(1)) + int(offset) -1
    
    body = comment['body']
    if location not in mySet:
        mySet = mySet | {location}
        quickfix = str(path) + ':' + str(location) + ':' + str(body) + '\n'
        myfile.write(quickfix)

os.system('git checkout '+branchname)

