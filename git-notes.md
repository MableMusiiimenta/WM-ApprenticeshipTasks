# what a branch is;

A branch is a secluded space where a developer can make changes or create new features without interfering with what's already in the codebase unless merged

# what a commit represents;

A commit represents documented additions or changes that are ready to be pushed and added to a workspace

# the difference between the working directory, staging area and a commit;

A working directory is where one is free to create, add, delete and edit code appropriately, a staging area is where different parts of the project are brought together ready for production and a commit refers to changes that are ready to be pushed/added to the code base

# your understanding of git fetch versus git pull;

git fetch refers to getting the changes from the remote repo that are different from your local code but without automatically merging them into your local workspace while git pull gets the remote changes and automatically merges them to the local ones

# what caused your merge conflict and how you resolved it;

The first branch had the word 'soccer' and the new branch used 'football'. So I commited the changes on the new branch and checked out the old branch, then noted the difference, with git diff and ran git merge to keep the changes from the new branch

# what you would normally check before pushing work or opening a pull request.

I would first make sure the code is running well locally with no errors, then solve merge conflicts if any then proceed to push