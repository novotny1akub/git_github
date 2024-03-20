# https://naucse.python.cz/course/pyladies/git/basics/
# https://nceas.github.io/oss-lessons/version-control/1-git-basics.html

## short
# !git init
# !git add file_name_goes_here.py
# !git commit -m "My commit"
# !git remote add origin https://github.com/novotny1akub/git_github.git (zkopírováno z repa na githubu)
# !git push -u origin master

## dalsi commandy
# !git add $(ls -r)
# !git add .
# !git add *
# !git commit -a -m "Change titles and styling on homepage"
# !git show <commitHash>:/path/to/file --> ./my_file.py
# !git status
# !git show --> ukazuje log předchozího commitu
# !git diff --> změny mezi dvěma commity nebo mezi commitem a stávající verzí repozitáře a commitem
# !git log --> vypíše všechny revize od té nejnovější až po úplný začátek projektu.

## uplne na zacatku
# !git config --global user.name "Jakub Novotny"
# !git config --global user.email "my_email_goes_here@example.com"
# !git config --global --list
# !git config --global --replace-all user.name "Jakub Novotny"


### https://www.youtube.com/playlist?list=PLdHg5T0SNpN1dJt6gv9DGSqk5sBjmG3XI
## making commits
# git status # if i want to see, for example, what files are not in the staging area
# git add file_name # to add to the staging area, if you change a file and want to commit it, you need to stage it again!
# git add . # to add all unstaged files
# git commit -m "first commit"
# git log # to see all commits i made, press q to exit
# git log --oneline
# git commit --amend -m "changed commit message"
# git commit --amend -m "New commit message" <commit-id>
## checkout commits (going back in time)
# git checkout <commit-hash> # to see how things looked in the past
## revert commits (undoing things)
# git revert <commit-hash> # creates a new commit that undoes the changes made by a previous commit
## merging commits into one - (git rebase and squashing)
# git rebase -i HEAD~5 # interactively changing posledních 5 commitů, p (beru, jak je), r (beru, ale měním message), s (consolidating more commits into one larger commit.), d (completely remove)




