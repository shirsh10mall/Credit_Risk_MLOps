# Repository Setup & Configuration

1. git init
   Initializes a new Git repository in the current directory.

2. git clone <url>
   Clones an existing repository from a remote server.

3. git config --global user.name "Name"
   Sets your name in global Git configuration.

4. git config --global user.email "[email@example.com](mailto:email@example.com)"
   Sets your email in global Git configuration.

5. git config --list
   Lists all Git configurations for the current environment.

---

# Basic Workflow

6. git status
    Shows the status of files in the working directory and staging area.

7. git add <file>
   Stages a specific file for the next commit.

8. git add .
   Stages all modified and new files in the current directory.

9. git commit -m "message"
   Commits staged changes with a descriptive message.

10. git log
    Displays a list of previous commits with details.

11. git diff
    Shows changes between working directory and staged files.

12. git diff --staged
    Shows changes between staged files and the last commit.

13. git reset <file>
    Unstages a file while keeping its changes.

14. git reset --hard
    Resets working directory and index to the last commit. (Destructive)

15. git rm <file>
    Removes a file from the working directory and stages the deletion.

---

# Branching & Merging

16. git branch
    Lists all local branches in the repository.

17. git branch <branch-name>
    Creates a new branch.

18. git checkout <branch-name>
    Switches to another branch.

19. git checkout -b <branch-name>
    Creates and checks out a new branch.

20. git merge <branch>
    Merges a specified branch into the current branch.

21. git branch -d <branch>
    Deletes a branch (only if it's already merged).

22. git stash
    Temporarily saves changes that are not ready to be committed.

23. git stash pop
    Restores the most recently stashed changes.

---

# Remote Repositories

24. git remote -v
    Shows the URLs of the remote connections.

25. git remote add origin <url>
    Adds a new remote repository.

26. git fetch
    Downloads new data from a remote repository without merging.

27. git pull
    Fetches from and merges with the remote branch.

28. git push
    Pushes your local commits to the remote repository.

29. git push -u origin <branch>
    Pushes a branch to the remote and sets it to track the remote branch.

30. git clone --recurse-submodules <url>
    Clones a repository including all its submodules.

---