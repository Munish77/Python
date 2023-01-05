Firstly, a new repository called Python had been created in Git on the student's Windows workstation. The student's Python exercises from week 2 to 5 had been saved in this repository (refer to image below).

![image](https://user-images.githubusercontent.com/120669555/210595749-9a5ca4b6-8654-43f8-9012-66b942f6a13b.png)

Next, the student had pushed the Python repository to GitHub (refer to image below).

![Python_folder_pushed_to_git_repo](https://user-images.githubusercontent.com/120669555/210598862-2788b2d0-a47c-430e-9caf-c794101b1875.PNG)

The student then created two branches in the Python repository. The branches were called as main and feature (refer to image below). The student had used the git checkout command to navigate between the branches created by git branch. Checking out a branch basically updates the files in the working directory to match the version stored in that branch and it tells Git to record all new commits on that branch. It is a way to select which line of development is being workied on. Having a dedicated branch for each new feature is a big shift from a traditional SVN workflow. It makes it easy to try new experiments without the fear of destroying existing functionality and it makes it possible to work on many unrelated features at the same time. In addition, branches also facilitate several collaborative workflows. The git checkout command can sometimes be confused with git clone. The difference between the two commands is that clone works to fetch code from a remote repository alternatively checkout works to switch between versions of code already on the local system.

![Feature_branch_created_and_merged_with_main_branch](https://user-images.githubusercontent.com/120669555/210680332-e1cbb1b1-caae-4c96-87a5-1e99d659144e.PNG)

Changes had been made in the feature branch and then merged into the main branch and pushed.

![Feature_branch_updated](https://user-images.githubusercontent.com/120669555/210680420-c26f7464-3a17-4083-84a8-9dbcee72ae3f.PNG)

Merge conflicts happen quite oftenly. Merge conflicts happen when the user merges branches that have competing commits and Git needs the users help to decide which changes to incorporate in the final merge. Git can often resolve differences between branches and merge them automatically. Usually, the changes are on different lines or even in different files which makes the merge simple for computers to understand. However, sometimes there are competing changes that Git can not resolve without the user's help. Often, merge conflicts happen when people make different changes to the same line of the same file or when one person edits a file and another person deletes the same file. The user must resolve all merge conflicts before the user can merge a pull request on GitHub. If the user has a merge conflict between the compare branch and base branch in the pull request, the user can view a list of the files with conflicting changes above the Merge pull request button. The Merge pull request button is deactivated until the user has resolved all conflicts between the compare branch and base branch.

