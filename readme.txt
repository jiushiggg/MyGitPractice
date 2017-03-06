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
