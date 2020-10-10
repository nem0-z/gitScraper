# gitScraper

Easy interactive script that converts a commit history page on github to a bash file *commit.sh* filled with the entries like this:

 #commitMessage

 git cherry-pick/revert commitSHA

You can decide whether you want to pick or revert following commits and also you can tell the script up until which point in the commit history you want to pick/revert commits.

Simply clone the repository using:

git clone https://github.com/nem0-z/gitScraper

and execute the script with the following command:

python3 gitScraper.py
