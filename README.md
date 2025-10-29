# homeworks

This repository contains Python homework files from the user's attachments. Files included are the `davaleba_*.py` scripts located in the project root.

What's here:
- `davaleba_1.py` through `davaleba_10.py` — small Python homework scripts.

How to create a remote GitHub repository and push this local repo

Option A — create repo on GitHub website (manual):
1. Go to https://github.com and sign in.
2. Click "New" to create a new repository. Give it a name (for example `homeworks`) and choose Public or Private.
3. Do NOT initialize with a README (we already have one). Create the repo.
4. In your repository page you'll see instructions. Run the following in your local repo folder (cmd.exe):

```cmd
cd /d "c:\Users\UGRELA\Desktop\step it\homeworks"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPO>.git
git push -u origin main
```

Option B — using GitHub CLI (`gh`) (requires `gh` and that you're logged in):

```cmd
cd /d "c:\Users\UGRELA\Desktop\step it\homeworks"
# create a public repo and push current directory, replace <REPO> with your repo name or omit to use current folder name
gh repo create <USERNAME>/<REPO> --public --source=. --remote=origin --push
```

If you'd like, I can run `gh repo create` for you here — that requires that `gh` is installed and you're already authenticated on this machine. Otherwise, tell me your desired GitHub repo name and whether you want it Public or Private and I will give exact commands to run.
