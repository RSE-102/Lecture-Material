# Git Demo

## Recap of Git basics

- Expert level poll on git: ask students to estimate their level.
    - Beginner: I have hardly ever used Git
    - User: pull, commit, push, status, diff
    - Developer: fork, branch, merge, checkout
    - Maintainer: rebase, squash, cherry-pick, bisect
    - Owner: submodules

![git overview picture from py-rse](https://third-bit.com/py-rse/figures/git-cmdline/git-remote.png)

- `git --help`, `git commit --help`
- incomplete statement `git co`

- There is a difference between Git and hosting services ([*forges*](https://en.wikipedia.org/wiki/Forge_(software)))
    - [GitHub](https://github.com/)
    - [GitLab](https://about.gitlab.com/), open-source, hosted e.g. at [IPVS](https://gitlab-sim.informatik.uni-stuttgart.de)
    - [Bitbucket](https://bitbucket.org/product/)
    - [SourceForge](https://sourceforge.net/)
    - many more
    - often, more than just hosting, also DevOps

- Give outlook on remainder of Git part: *How I work with Git*, advanced topics (workflows, rebase), exercise

## How I work with Git

Starting remarks:

- There is not *the one solution* how to do things with Git. I simply show what I typically use.
- Don't use a client if you don't understand the command line `git`

- (1) Look at GitHub
    - [preCICE repository](https://github.com/precice/precice)
    - default branch `develop`
    - branch protection rule for `main` (`Settings` --> `Branches`)
    - fork -> my fork

- (2) Working directory:
    - ZSH shell shows git branches
    - `git remote -v` (I have upstream, myfork, ...)
    - mention difference between ssh and https (also see GitHub)
    - get newest changes `git pull upstream develop`
    - or simply `git pull` (`git branch -vv` to see upstream tracking)
    - `git log` -> I use special format, see `~/.gitconfig`,
    - check log on GitHub
    - explain how hash is computed (complete state + pointer to parent)
    - explain short hash
    - `git checkout -b add-demo-feature`

- (3) First commit
    - `git status` -> always tells you what you can do
    - `vi src/action/Action.hpp` -> add `#include "MagicHeader.hpp"`
    - `git diff`, `git diff src/com/Action.hpp`, `git diff --color-words`
    - `git status`, `git add`, `git status`
    - `git commit` -> "Include MagicHeader in Action.hpp as a demo" (what, not how; include why if possible; imperative mood; no period)
    - `git status`, `git log`, `git show`

- (4) Change or revert things
    - I forgot to add sth: `git reset --soft HEAD~1`, `git status`
    - `git diff`, `git diff HEAD` because already staged
    - `git log`
    - `git commit`
    - actually all that is nonsense: `git reset --hard HEAD~1`

- (5) Create PR
    - create commit again
    - `git push -u myfork add-demo-feature` -> copy link
    - explain PR template
    - explain target branch
    - explain "Allow edits by maintainers"
    - cancel
    - my fork -> branches -> delete

- (6) Check out someone else's work
    - have a look at an existing PR, look at all tabs, show suggestion feature
    - but sometimes we want to really build and try sth out ...
    - `git remote -v`
    - `git remote add alex git@github.com:ajaust/precice.git` if I don't have remote already (or somebody else)
    - `git fetch alex`
    - `git checkout -t alex/[branch-name]`
    - I could now also push to `ajaust`'s remote

## Further reading

### Quick things

- [Video: Git in 15 minutes: basics, branching, no remote](https://www.youtube.com/watch?v=USjZcfj8yxE)
- Chapters [6](https://third-bit.com/py-rse/git-cmdline.html) and [7](https://third-bit.com/py-rse/git-advanced.html) of Research Software Engineering with Python
- [git purr](https://girliemac.com/blog/2017/12/26/git-purr/)

### References

- [Official documentation](http://git-scm.com/doc)
