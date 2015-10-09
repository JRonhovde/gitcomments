#!/usr/bin/python

import urllib2
import json
import sys
import os
import re

thisDir = os.getcwd()

with open('/home/jronhovde/gitcomments/gitcomments.json') as data_file:
    data = json.load(data_file)

# if re.search(r'ss$',thisDir):
    # repo = 'sycamoreschool'
# elif re.search(r'sc$',thisDir):
    # repo = 'sycamorecampus'

# username = 'JRonhovde'
# token = 'd00ebb9687f47f3017219290f2791d8875dcf5ba'
# owner = 'sycamoreeducation'

# branchname = sys.argv[1]
# filename = sys.argv[2]

# getPR = 'curl --user '+username+':'+token+' https://api.github.com/repos/'+owner+'/'+repo+'/pulls?head='+owner+':'+branchname
# import subprocess
# process1 = subprocess.Popen(getPR.split(), stdout=subprocess.PIPE)
# try:
    # pullRequestJSON = process1.communicate()[0]
    # pullRequestList = json.loads(pullRequestJSON)[0]
    # url = pullRequestList['review_comments_url']
# except:
    # sys.exit('Invalid branch. Check that your branch is spelled correctly.')

# getComments = 'curl --user '+username+':'+token+' '+url+'?per_page=100'
# process2 = subprocess.Popen(getComments.split(), stdout=subprocess.PIPE)
# try:
    # commentJSON = process2.communicate()[0]
# except:
    # sys.exit('No result from GitHub API. Check to make sure your branch, "'+branchname+'" is attached to a Pull Request on GitHub.')

# commentList = json.loads(commentJSON)
# myfile = open(filename, 'w+')
# myList = []
# for comment in commentList:
    # if str(comment['position']) == 'None':
        # continue

    # path = comment['path']
    # locationObj = re.match(r'@@ -\d+,\d+ \+(\d+)',comment['diff_hunk'])
    # newLineObj = re.findall(r"\n[+ ]", comment['diff_hunk'])
    # offset = len(newLineObj)
    # location = int(locationObj.group(1)) + int(offset) -1
    
    # body = comment['body']
    # try:
        # duplicate = myList.index(location) >= 0
    # except:
        # duplicate = 'false'
        # pass
    # if duplicate == 'false':
        # myList.append(location)
        # quickfix = str(path) + ':' + str(location) + ':' + str(body) + '\n'
        # myfile.write(quickfix)

# os.system('git checkout '+branchname)

