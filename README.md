# Git_Assignment_HeroVired

File contains solutions to the Git-based assignment for Hero Vired,
which is covering version control workflows using Git & GitHub,
feature branching, bug fixes, Git LFS, and stash management with Mini Python projects.
Here is list of questions and their solutions

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
- 
 **Repository-Flow**
Create a Development Branch and Add Provided Code
Switch to the dev branch:
git checkout -b dev
Add the provided source code, commit, and push.

Merge with Main and Release Version 1
Merge dev into main:
git checkout main
git merge dev
Create a v1.0 release on GitHub.
Add one or more batchmates as collaborators.

**Implement Square Root Feature**
Create a new feature branch:
git checkout -b feature/sqrt
Uncomment and implement the square_root() function in calculator.py.
Commit the changes in feature/sqrt.

Bug Fixation
Switch to the dev branch:
git checkout dev
Modify the divide() function to prevent division by zero.
Commit the fix and push:

git add .
git commit -m "Fix division by zero bug"
git push origin dev
Create a pull request to merge dev → main.

---

**Feature Addition and Release Version 2**
Switch to feature/sqrt branch:
git checkout feature/sqrt
Merge the updated dev branch into it and resolve any conflicts:
git merge dev
Create a pull request from feature/sqrt to dev.
Once merged, update main with dev and create a v2.0 release.

---

**Handling Large Files with Git LFS**
Create a branch for lfs
Create and switch to a new branch:
git checkout -b lfs
Install and Set Up Git LFS
Download Git LFS

After installing, configure LFS:

git lfs install
git lfs track "*.bin"
git add .gitattributes
git commit -m "Configure Git LFS for .bin files"

Add and commit a file over 200MB:

git add large_file.bin
git commit -m "Add large .bin file"
git push origin lfs
Merge lfs into main once complete.

---

 **Geometry Calculator with Git Stash operation without commit**
Create a Main Feature Branch
Create and switch to the main feature branch:
git checkout -b geometry-calculator
Create Feature Branches

git checkout -b feature/circle-area
git checkout geometry-calculator
git checkout -b feature/rectangle-area
Use Git Stash
Stash incomplete changes:

git stash save "message to save temp changes"
Retrieve them later:

git stash apply 1 or git stash apply 0 based on the number of stash
Commit and Push Features
Commit and push each feature:

git add .
git commit -m "Add rectangle/circle area feature"
git push origin <branch-name>
Create pull requests to dev.
Merge into main upon approval.

---
Screenshot of the Output:
LFS tracking header after cloning
![git lfs](https://github.com/user-attachments/assets/3013265b-6692-472b-93cf-c505394fb895)

---

CalculatorPlus.py
![image](https://github.com/user-attachments/assets/34af2737-0d6a-4bd6-9b2e-27c738974e14)

---
Final Git Stash operation in main after merging both circle and rectangle
![image](https://github.com/user-attachments/assets/dcabe0fa-5914-4f7f-ae9c-caaf4a16efbc)

---
circle branch: git stash 
![image](https://github.com/user-attachments/assets/1a9c6076-de54-4464-8875-09765ee1ba80)

---
rectangle branch: git stash
![image](https://github.com/user-attachments/assets/bf09e1b0-e3e1-4e17-9cb4-41bd35cff8b0)

---
Author: Rahul Sharma
