- https://git-scm.com/docs
- Example: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

- Flow
    - Working DIR -- Staging Area -- Local Repo -- Remote Repo
- Git- Distributed Version Control open source.
- Github - Platform for hosting and coloborating on GIT repos.
- Local - With in the a member of a team/employee side.
- remote - Common repository that all team members exchange/perform opertions.
- **SETUP/Configure tooling**
    - git config --global user.name "[name]"
        - git config --global user.name "email4prasanth"
    - git config --global email.name "[email]"
        - git config --global user.email "email4prasanth@gmail.com"
    - git config --golbal list
- **Create repositories**
    - git init - turns existing directory into a git repository
    - git clone [url] - Download the existing repository available on github.
        - git clone https://github.com/kubernetes/kubernetes/tree/master/pkg/controller/podautoscaler
        - It is recommned to clone by creating an empty folder.
- **BRANCH & MERG**
    - Any commit you make will be made on current branch
    - git branch - list of branches.
    - git branch [branch-name] - create new branch 
        - git branch prasanthmarri.
    - git checkout [branch-name]
        - git checkout yamunakutti.
    - git merge [branch] - merge specfied branch with current branch.
    - Example:
        git branch 
        git branch -b prasanthbranch (will create `iss53` branch and checkou to that branch.)
        git commit -a -m 'created new branch'
        git checkout master
        git merge prasanthbranch
- **INSPECT & COMPARE**
    - git log - show commit history for current active branch.
    - git log branchB..bracnchA - shows commit on branchA that are not in branchB.
    - git diff branchB...branchA - show difference on branchA that are not in branchB.
    - git log --flow [file] - shows version history for file and also rename history.
- **TRACKING PATH CHANGES**
    - git rm [file]
    - git mv  [existing-path] [new-path] 
    - git log --stat -M - show all commit logs with indication of any path that moved.
