 1906  cd mygit
 1907  git congig --global user.name "ggg"
 1908  git config --global user.name "ggg"
 1909  git config --global user.email "23980383322@qq.com"
 1910  git config user.name
 1911  git config user.email
 1912  git init							//this directory is initiated  as a repository
 1913  ll								//this command will show  .git directory
 1914  touch test.py					//create a file
 1916  git status						//display file status 
 1917  git add test.py					//add a file in git 
 1918  git status


//forget commit a file, but don't add commit number 
 1993  vi 2.py							//creat a file in mygit
 1996  git log --oneline				//show the commit log
 1998  git add 2.py						//add a file in git
 1999  git commit --amend --no-edit		//commit, --amend:Put this commit in previous commit. --no-edit:Don't change the message.
 2000  git log --oneline				//show the commit log.there is no new commit, but change the commit ID


//reset
 [jiushi@mygit]$cat 2.py
 print '2.py'
 [jiushi@mygit]$vi 2.py
 [jiushi@mygit]$cat 2.py
 print '2.py'
 print '2.1.py'
 [jiushi@mygit]$git add 2.py
 [jiushi@mygit]$git status -s
 M  2.py								//M is green color
 [jiushi@mygit]$git reset 2.py			
 Unstaged changes after reset:
 M	2.py			
 [jiushi@mygit]$cat 2.py				//M is no color	
 print '2.py'
 print '2.1.py'
 [jiushi@mygit]$git status -s			
  M 2.py								//M is red color
 
 [jiushi@mygit]$git add 2.py
 [jiushi@mygit]$git commit -m "change2"
 [master ce09a22] change2
 [jiushi@mygit]$git log --oneline
 ce09a22 change2
 9528d99 o
 3b75d59 change 1
 
 [jiushi@mygit]$git reset --hard 9528d99
 HEAD is now at 9528d99 o
 [jiushi@mygit]$git log --oneline
 9528d99 o
 3b75d59 change 1

 [jiushi@mygit]$git reflog
 9528d99 HEAD@{0}: reset: moving to HEAD@{3}
 ce09a22 HEAD@{1}: reset: moving to ce09a22
 9528d99 HEAD@{2}: reset: moving to 9528d99
 ce09a22 HEAD@{3}: commit: change2
 9528d99 HEAD@{4}: commit (amend): o
 23909ee HEAD@{5}: commit (amend): o
 d7bec16 HEAD@{6}: commit: o
 3b75d59 HEAD@{7}: commit (initial): change 1
 [jiushi@mygit]$git reset --hard HEAD@{2}
 HEAD is now at ce09a22 change2
 
 [jiushi@mygit]$git log --oneline
 ce09a22 change2
 9528d99 o
 3b75d59 change 1


 //checkout
[jiushi@mygit]$git log --oneline
4216ccf change2
9528d99 o
3b75d59 change 1
[jiushi@mygit]$git checkout 9528d99 -- readme.txt	//Only readme.txt is back to 9528d99 

//branch
[jiushi@mygit]$git log --oneline --graph
* 4216ccf change2
* 9528d99 o
* 3b75d59 change 1
[jiushi@mygit]$git branch dev						//Create a branch
[jiushi@mygit]$git branch							//Display branch
  dev
  * master
[jiushi@mygit]$git checkout dev						//goto dev branc
Switched to branch 'dev'
[jiushi@mygit]$git branch							//already in dev branch
* dev
  master
[jiushi@mygit]$git branch -d dev					//failed
error: Cannot delete the branch 'dev' which you are currently on.

[jiushi@mygit]$git checkout master					//goto master 
Switched to branch 'master'
[jiushi@mygit]$git branch -d dev					//delete dev branch
Deleted branch dev (was 4216ccf).
[jiushi@mygit]$git checkout -b dev					//Create a dev and goto dev branch
[jiushi@mygit]$git branch
* dev
  master

[jiushi@mygit]$git commit -am "change 3 in dev"		//equal to add ,then commit -m.this command
													//only can use in exist file in git,not to new file
[dev c5a87f1] change 3 in dev
 2 files changed, 9 insertions(+), 1 deletion(-)
[jiushi@mygit]$git log --oneline --graph
* c5a87f1 change 3 in dev
* 4216ccf change2
* 9528d99 o
* 3b75d59 change 1

//merge
[jiushi@mygit]$git checkout master					//back to master
Switched to branch 'master'
[jiushi@mygit]$git merge -m "keep merge info" dev	//default message
Updating 4216ccf..832e7df
Fast-forward (no commit created; -m option ignored)
 2.py       |  1 +
 readme.txt | 48 ++++++++++++++++++++++++++++++++++++++-
 2 files changed, 48 insertions(+), 1 deletion(-)
[jiushi@mygit]$git log --oneline --graph			//no message
* 832e7df change 3 in dev
* 4216ccf change2
* 9528d99 o
* 3b75d59 change 1
[jiushi@mygit]$git branch
  dev
* master

//I make conflict
[jiushi@mygit]$git checkout dev
Switched to branch 'dev'
[jiushi@mygit]$git commit -am "add merge" --amend 
[dev 5319740] add merge
2 files changed, 63 insertions(+), 1 deletion(-)
[jiushi@mygit]$git log --oneline
5319740 add merge
4216ccf change2
9528d99 o
3b75d59 change 1




//merge conflict
[jiushi@mygit]$git merge --no-ff -m "keep merge info" dev	//no fast forward
Auto-merging readme.txt
CONFLICT (content): Merge conflict in readme.txt
Automatic merge failed; fix conflicts and then commit the result.
[jiushi@mygit]$git commit -am "solve conflict"
[master 785ebc6] solve conflict
[jiushi@mygit]$git log --oneline --graph
*   785ebc6 solve conflict
|\  
| * 5319740 add merge
* | 832e7df change 3 in dev
|/  
* 4216ccf change2
* 9528d99 o
* 3b75d59 change 1


//stash
[jiushi@mygit]$vi 2.py				//add "print 'stash"
[jiushi@mygit]$cat 2.py
print '2.py'
print '2.1.py'
print '2.branch.py'
print 'stash'
[jiushi@mygit]$git log --oneline
6ff6229 add merge
785ebc6 solve conflict
5319740 add merge
832e7df change 3 in dev
4216ccf change2
9528d99 o
3b75d59 change 1

[jiushi@mygit]$git stash
Saved working directory and index state WIP on master: 6ff6229 add merge
HEAD is now at 6ff6229 add merge
ushi@mygit]$cat 2.py
print '2.py'
print '2.1.py'
print '2.branch.py'
[jiushi@mygit]$git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
	modified:   2.py

//github
[jiushi@mygit]$git remote add origin https://github.com/longfeigao/test1.git
fatal: remote origin already exists.
[jiushi@mygit]$git remote rm origin
[jiushi@mygit]$git remote add origin https://github.com/longfeigao/test1.git
[jiushi@mygit]$git push -u origin master
Username for 'https://github.com': longfeigao
Password for 'https://longfeigao@github.com': 


