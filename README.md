# Git_Assignment_HeroVired

Feature branching, pull-requests and releases (`CalculatorPlus.py`)  
* Bug-fixing and CI-ready code organisation  
* Working with large files through **Git LFS**  
* Parallel feature development with **stash** & branch juggling (`GeoCalculator.py`)


**Q1: CalculatorPlus**

- Created `dev` branch, added initial Calculator code.
- Implemented `square_root()` in `feature/sqrt` branch.
- Fixed divide bug (added zero division check).
- Merged features to `dev`, tested, then merged to `main`.
- Released **v1** (basic + sqrt), **v2** (with bug fix).
- Collaborated with classmate for code review.

---

**Q2: Git LFS**

- Created `lfs` branch.
- Installed & configured Git LFS.
- Uploaded a file >200MB.
- Verified file download on another machine after cloning.

---

**Q3: GeometryCalculator**

- Created `geometry-calculator` branch.
- Used `git stash` to switch between:
  - `feature/circle-area`
  - `feature/rectangle-area`
- Completed both features, created PRs, merged after review.

Workflow Steps
1️. CalculatorPlus Implementation
      Create a GitHub repository named git_assignment_HeroVired and clone it locally by git clone.
      Create a Dev Branch and add the provided code
      Switch to the dev branch.
      Merge with Main and Release Version 1
      Added batchmates as collaborators

2. Implement Square Root Feature
        Create a new branch feature/sqrt and implement the square root function.
        Uncomment and implement the square_root function in calculator.py.
        Commit your changes in the local branch feature/sqrt.
        Bug Fixation
        Switch to the dev branch.
        Modify the divide function to prevent division by zero.
        Implement the fix in the dev branch and merge it.
        Create a pull request to push the changes to the main branch from dev.
        Feature Addition and Release Version 2
        Switch to the feature/sqrt branch.
        Merge the updated changes from dev branch to feature/sqrt branch and fix the conflicts if any.
        Create a pull request to push the changes to the feature/sqrt branch from dev.
        Merge dev into main and create a version 2 of the release.

   Handling Large Files with Git LFS
        Create a Branch for Git LFS and checkout to a new branch lfs:
        git checkout -b lfs
        Install and Set Up Git LFS
        Download and install the Git LFS CLI.
        URL: https://github.com/git-lfs/git-lfs/releases/download/v3.6.1/git-lfs-windows-v3.6.1.exe

   Once downloaded and installed, intialize using Git LFS install then
        git lfs track "*.bin"
        git add .gitattributes
        Add and commit a file over 200MB.
        Implement, commit, and push all the changes or requirements into the current branch.
        #Steps to complete the lfs
        git add .
        git commit -m "Add .bin file"
        git push origin lfs
        Merge into main once you are done.

3.Geometry Calculator with Git Stash and implementing the stashing without commit

       Create a main feature branch geometry-calculator
       Checkout to the geometry-calculator branch.
       Create Feature Branches from the main feature branch "geometry-calculator" like
       feature/circle-area and feature/rectangle-area 

Use Git Stash
       Before switching branches, stash incomplete changes:
       git stash save "message like circle changes"
Retrieve the stashed changes when resuming work:
       git stash apply 1 or 0  based on saved stash sequence and message

Commit and Push Features
       Implement, commit, and push both features and create pull requests for dev.
       Merge into main upon approval.


Author: Rahul Sharma
