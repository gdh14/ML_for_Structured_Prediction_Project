# configure user and email

git config --global user.name "yy1203"
git config --global user.email "yangyu2@andrew.cmu.edu"
# check branch
git branch 

# switch branch
git checkout $branchname

# create new branch and switch to new branch
git checkout -b $branchname

# load data from remote branch
git pull origin master


# check the status of git?
git status

# check commit log
git log

# add
git add -A
git add file_name

# commit
git commit -m "content"

# upload to remote
git push 

