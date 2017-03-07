 1906  cd mygit
 1907  git congig --global user.name "ggg"
 1908  git config --global user.name "ggg"
 1909  git config --global user.email "23980383322@qq.com"
 1910  git config user.name
 1911  git config user.email
 1912  git init							//this directory is initiated  as a repository
 1913  ll								//this commit will display a .git directory
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
 [jiushi@mygit]$cat 2.py				//M is no` color	
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

