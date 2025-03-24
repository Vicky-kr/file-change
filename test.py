from git import Repo

# Path to your Git repository
repo_path = "/home/runner/work/file-change/file-change"

# Initialize the repository
repo = Repo(repo_path)

# Ensure the repository is not bare
if not repo.bare:
    try:
        # Get the current commit (HEAD)
        head_commit = repo.head.commit
        print(head_commit)
        # Get the parent commit (HEAD~1)
        parent_commit = head_commit.parents[0]  # HEAD~1
        print(parent_commit)
        # Get the diff between HEAD and HEAD~1
        diff = head_commit.diff(parent_commit)

        # Print the names of files that have changed
        print("Files changed between HEAD and HEAD~1:")
        for diff_item in diff:
            print(diff_item.a_path)  # File path
    except Exceptio as e:
        print(e)
        print("No parent commit (HEAD~1) available. This might be the first commit.")
else:
    print("The repository is bare.")
