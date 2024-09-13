# Task Overview - Terminal_Chaos
In this task, I combined codes from different parts to unlock a repository and explore its contents. The process involves several key steps:

## 1.Combining Codes :
- **Gathering Codes:** I Collected codes from each part of the task.
- **Decoding Combined Code:** Decode the combined code to reveal a link to the        GodSuite repository.

 ## 2.Cloning the Repository :
**Clone Repository:**

```bash
git clone <link of the url>
```
This command downloads the repository from the provided link to my local system, this allowed me to access its contents.

## 3.Exploring the Repository :
Once I cloned, I explored the repository using Git commands:
### - Check Branches:
```bash
git branch
```
Lists all branches in the repository and highlights the current branch.
### - Switch Branches:
```bash
git checkout <branch name>
```
It Switches to a specified branch, allowing you to view and work on different versions of the code.
### - grep :
```bash
grep -rl "holy"
grep -rl "good"
```
the grep -rl command is used to search recursively through directories for files containing a specific word or pattern, and it only outputs the names of those files. In your task, you used it to find all files containing the words "holy" and "good" to identify relevant files for further processing.

## 4.File Navigation and Manipulation :
To navigate and manipulate files, I used the following commands:
### - View Directory Structure:
```bash
tree
```
Displays the directory and file structure in a hierarchical format, This helped me a lot to understand the organization of files.
### - Display File Content:
```bash
cat <filename>
```
Shows the content of a file, which is useful for reading and analyzing file contents.

## EXPLANATION :
At first in part 1,started using **tree** command which was far more better than **find** in my point of view for this part 1.So first I located the file path where the *parchment.txt* was there,used the **cat** command to see what's inside there and found out the first code.  
In part 2,took a lot of time for understanding and executing it as the brewed spell was wrong and also don't know what to do further.after sometime only i discovered the actual secret behind it . here the **git branch** and **git checkout <filename>** helped me a lot.also i seeked the help of the task admin as i had a confusion in brewed spell.so i used the spell to defeat the Kharnokand got the code from him also a amulet.  
In part 3, i unlocked the chests easily by running python for each chest also switched between the branches dark realm 1,2 to unlock the chests.the secret code for opening the chest is the amulet code which i got from defeating Kharnok.  
In part 4 , i decoded the 4 codes and got a url of the next part the godsuite.  
In part 5, actually it  was too easy for me as i have explored many commands and understood the logic behind it.Here first i located the path  to clone the repository used **git clone <url>** for cloning.Used an important code:  ```git log --oneline``` which will display a list of commits with their respective messages(its more like dispaying the branch names).Also used ```git checkout <commit-hash>```as this command switches our working directory to the state of the project at a specific commit.dentified by the <commit-hash>.(like checkout branch..).finally found out the code at the 4th commit-hash and decoded it.After that i clone the repo which i had decoded using that i easily runned the victory.py file using the command ```python victory.py --run``` and claimed the winnning token.



