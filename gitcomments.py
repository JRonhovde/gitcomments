#!/usr/bin/python

import urllib2
import json
import sys
import os
import re
import pprint
import subprocess
import inspect


parentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
with open(parentDir+'/gitcomments.json') as data_file:
    data = json.load(data_file)

username = data['username']
token = data['token']

getRepo = ['git', 'config', '--get', 'remote.origin.url']
getRepoProcess = subprocess.Popen(getRepo, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
repoURL, err = getRepoProcess.communicate()
repoObj = re.match(r'(https\:\/\/github\.com\/|git\@github\.com\:)([^\/]*)\/([^.]*)',str(repoURL))
try:
    repoOwner = repoObj.group(2)
    repoName = repoObj.group(3)
except:
    sys.exit('Could not retrieve repository information, make sure you are in a git repository.')

branchname = sys.argv[1]
filename = sys.argv[2]

getPR = 'curl --user '+username+':'+token+' https://api.github.com/repos/'+repoOwner+'/'+repoName+'/pulls?head='+repoOwner+':'+branchname
process1 = subprocess.Popen(getPR.split(), stdout=subprocess.PIPE)
try:
    pullRequestJSON = process1.communicate()[0]
    pullRequestList = json.loads(pullRequestJSON)[0]
    url = pullRequestList['review_comments_url']
except:
    sys.exit('Invalid branch. Check that your branch is spelled correctly.')

getComments = 'curl --user '+username+':'+token+' '+url+'?per_page=100'
process2 = subprocess.Popen(getComments.split(), stdout=subprocess.PIPE)
try:
    commentJSON = process2.communicate()[0]
except:
    sys.exit('No result from GitHub API. Check to make sure your branch, "'+branchname+'" is attached to a Pull Request on GitHub.')

commentList = json.loads(commentJSON)
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

