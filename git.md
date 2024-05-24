- https://git-scm.com/docs
- Example: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

- Flow
    - Working DIR -- Staging Area -- Local Repo -- Remote Repo
- Git- Distributed Version Control open source.
- Github - Platform for hosting and coloborating on GIT repos.
- Local - With in the a member of a team/employee side.
- remote - Common repository that all team members exchange/perform opertions.
- **SETUP/Configure tooling**
    - `git config --global user.name "[name]"`
        - git config --global user.name "email4prasanth"
    - `git config --global email.name "[email]"`
        - git config --global user.email "email4prasanth@gmail.com"
    - `git config --golbal list`
- **Create repositories**
    - `git init` - turns existing directory into a git repository
    - `git clone [url]` - Download the existing repository available on github.
        - git clone https://github.com/kubernetes/kubernetes/tree/master/pkg/controller/podautoscaler
        - It is recommned to clone by creating an empty folder.
- **BRANCH & MERG**
    - Any commit you make will be made on current branch
    - `git branch` - list of branches.
    - `git branch [branch-name]` - create new branch 
        - git branch prasanthmarri.
    - `git checkout [branch-name]`
        - git checkout yamunakutti.
    - `git merge [branch]` - merge specfied branch with current branch.
    - Example:
        git branch 
        git branch -b prasanthbranch (will create `iss53` branch and checkou to that branch.)
        git commit -a -m 'created new branch'
        git checkout master
        git merge prasanthbranch
- **INSPECT & COMPARE**
    - `git log` - show commit history for current active branch.
    - `git log branchB..bracnchA` - shows commit on branchA that are not in branchB.
    - `git diff branchB...branchA` - show difference on branchA that are not in branchB.
    - `git log --flow [file]` - shows version history for file and also rename history.
    - `git show [commit]` - shows metadata of the given commit.
- **TRACKING PATH CHANGES**
    - `git rm [file]`
    - `git mv  [existing-path] [new-path]` 
    - `git log --stat -M` - show all commit logs with indication of any path that moved.
- **Synchronize changes/Updates**
    - `git fetch` - Download files from remote repo to local repo
    - `git merge` - combines remote branch to local branch
    - `git pull` - fetch+merge, Download files from remote repot to working dir
    - `git push [alias] [branch]` - Upload files from local repo to remote repo
    - 
- **REWRITE HISTORY**
    - `git rebase [branch]` - apply any commits of current branch to ahead of specific one
        - https://www.youtube.com/watch?v=0chZFIZLR_0
    - `git reset --hard [commit]` - clear stagging area, rewrite from specific commit
- **TEMPORARY COMMITS**
    - `git stash` - save modified and stage
    - `git stash list`- list of staged files
    - `git stash pop` - write working from top of stack
    - `git stash drop` - discard the changes form top of stack

</h1> FQA </h1>

What's the Difference Between Merge and Rebase?