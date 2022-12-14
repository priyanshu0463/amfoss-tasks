
 task-02

## Commands used during the task:

cloning the repo

```git clone https://github.com/gauthamk02/TerminalHunt.git```

creating solution directory

```mkdir solution```

changing directory to solution

```cd solution```

multiplying smallest perfect number by 44

```echo $((6*44))```

creating part1.txt

```touch part1.txt```

using nano to input the part 1 solution into part1.txt

```nano part1.txt```

to see the contents of part1.txt

```cat part1.txt```

going back a directory

```cd ..```

copying 06/1.txt to solution/

```cp 06/1.txt solution/```

renaming the file by moving the file to the same destination but changing the destination filename

```mv 1.txt part2.txt```

copying 10/1.txt to solution/

```cp 10/1.txt solution/```

renaming 1.txt to part3.txt

```mv 1.txt part3.txt```

using git status to know the current state of the repo

```git status```

staging all the files

```git add ./```

commiting all the changes

```git commit -m "completed till step 6"```

listing all the branches

```git branch -a```

using git checkout to checkout the asia branch

```git checkout origin/asia```

trying to find athens.txt

```find . -name athens.txt```

going back to main branch

```git checkout main```

marging asia branch with main

```git merge origin/asia```

copying NewFolder/Greek-Empire/athens.txt to solution/

```cp NewFolder/Greek-Empire/athens.txt solution/```

renaming athens.txt to part4.txt

```mv athens.txt part4.txt```

using cat command to merge all the text files into one password.txt

```cat *.txt > password.txt```

deleting all the other txt files

```rm part{1,2,3,4}.txt```

to get the contents of password.txt

```cat password.txt```

staging and committing the changes

```git add secret-scrollss.png```

```git commit -m "screenshot"```

```git add SOLUTION.md```

```git commit -m "solutions of task-02"```

pushing to the remote repository

```git push```


