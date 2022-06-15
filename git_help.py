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
