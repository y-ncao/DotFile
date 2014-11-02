##Common

###Switching to/updating a local branch[¶](#Switching-toupdating-a-local-branch)
```
git checkout local_branch
git pull --rebase
git submodule init
git submodule update
```

###Start new branch from state of current branch.[¶](#Start-new-branch-from-state-of-current-branch)
```
git checkout -b new_branch_name
```

Which is the same as:

```
git branch new_branch_name
git checkout new_branch_name
```

### Basic development of a feature[¶](#Basic-development-of-a-feature)

1. [Switch to/update master branch](#Switching-toupdating-a-local-branch).
2. Create local branch:
```
git checkout -b 1234_my_feature
```
3. Do your development.
4. Commit your changes:
```
git status
git add file.py
git commit -m "Descriptive commit message."
```
5. Push to the git server:
```
git push -u
```

### "Non fast-forward" error when pushing[¶](#Non-fast-forward-error-when-pushing)

This means your commits don't fit directly on top of what's currently on the server.

* Did you just do a rebase? You'll need to do a force push instead to confirm that you are pushing rewritten commits:
```
git push -f
```
* If you didn't just rebase, someone else has pushed commits since you last did a pull. In this case, do a pull to rebase your changes on top of the latest code, then push it again:
```
git pull --rebase
git push
```

### Checking out a remote branch for testing/review/shared development[¶](#Checking-out-a-remote-branch-for-testingreviewshared-development)
1.  Make sure your repository database is up-to-date by [switching to and updating master branch](#Switching-toupdating-a-local-branch).
2.  Checkout as a tracking branch:
```
git checkout -t origin 1234_their_feature
git submodule init
git submodule update
```
3.  If another developer later rebases the branch, you need to [delete and re-checkout the branch](#After-someone-else-rebases-a-shared-branch) to get the latest code.
### Push your latest changes to the remote of your feature branch.[¶](#Push-your-latest-changes-to-the-remote-of-your-feature-branch)
```
git push origin sprint-X-description
```
where _origin_ is properly set to the right Github repo. If you have tracking set up properly, you should be able to simply do
```
git push
```
though if you aren't sure, being explicit is always preferred.

### Merging master into your feature branch for testing[¶](#Merging-master-into-your-feature-branch-for-testing)

Before you open your pull request and have people start testing your work, you will want to merge in the latest changes from master so that any changes since your last merge are included and they are testing the code in a more production-like state.

```
git checkout master
git pull origin master
git checkout your_feature_branch
git merge master
```

### Writing a commit message[¶](#Writing-a-commit-message)

Our commit messages are going to be used to generate a changelog for each release. As such, we need to have a standard for what it should look like and what information we will have in the message.
NOTE: This is only the commit message used when merging into master. You don't have to follow this model for all of your individual commits in your working feature branch.

##Structure

###Subject
The first line of the commit message is known as the subject. It describes the change concisely and helps reviewers to see at a glance what the commit is about.

* Use the imperative mood (e.g., "Make foo do bar" instead of "[This patch] makes foo do bar" or "[I am] changing foo to do bar").
* Being a title (not a sentence in a paragraph) it should not end in a full stop.
* It should be no more than 50 characters (must be less than 80).
* The subject is what is used in the changelog.

###Body
Use the body of the commit message to describe your change in detail.

* Separate the body from the subject with an empty line.
* Give an overview of why you're committing this change.
  * What the commit changes.
  * Any new design choices made.
  * Areas to focus on for recommendations or to verify correct implementation.
  * Any research you might have done.
* Bytes are cheap, so just write!
* Try to make your commit message understandable without external resources (e.g., instead of just giving a URL to a mailing list archive, summarize the relevant points of the discussion).
* Wrap the body of the message at no more than 72 characters.

###Cross-references

* Use the "Issue:" keyword to cross-reference a Jira ticket.

###Example

Separate app log from apache log; fix MPS/logger

Introduce the concept of app_logger which separates the app logging
from the apache error log (old way). Given that some functions are
called under different contexts (i.e. the app directly, job engine,
dcs, etc.), app_logger allows for switching to different log channel
if the current channel is "root" (i.e. the app), which maintains
all job engine logging to end up in the job engine.

Create two separate log files for app logging - one for INFO and
above. One for debug and above.

MPS/factory/logger.py had a bug which prevented the real time
switch of logger level from the logconf.ini file. Fixed bug
to allow for functionality.

Issue: 1234

###Sources
[http://www.mediawiki.org/wiki/Gerrit/Commit_message_guidelines](http://www.mediawiki.org/wiki/Gerrit/Commit_message_guidelines)
[http://www.slideshare.net/TarinGamberini/commit-messages-goodpractices](http://www.slideshare.net/TarinGamberini/commit-messages-goodpractices)
[http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
[http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)
[https://github.com/torvalds/linux/pull/17#issuecomment-5659933](https://github.com/torvalds/linux/pull/17#issuecomment-5659933)
[https://github.com/thoughtbot/guides/tree/master/code-review](https://github.com/thoughtbot/guides/tree/master/code-review)

### Merging your work back into _master_[¶](#Merging-your-work-back-into-master)

After you are done with your feature branch and it has been tested and reviewed by the team, you will want to merge your work back into our master branch.
During the course of your work, you may (should) have made many commits with your progress. We don't necessarily want all of these commits showing up in master branch. When looking at the
log of master branch, it is much cleaner to see just one commit with your feature for easy locating and removal if needed.
At the same time, we don't want to lose important history in your feature branch. See Michael's Notes on History.
To solve this problem, I propose "merge --squash". This will allow a single commit to show in master with all of the work from your feature branch while keeping all the individual commits in your feature branch untouched and unsquashed.
Process:

1. Checkout master
```
git checkout master
```
2. Pull in the latest changes from origin master
```
git pull origin master
```
3. You likely won't have conflicts, but if you do resolve them.
4. Checkout your local feature branch
```
git checkout yourbranch
```
5. Update merge in local master
```
git merge master
```
6. Resolve any conflicts
7. Checkout master again
```
git checkout master
```
8. Merge you feature branch into master with --squash
```
git merge --squash yourbranch
```
9. There should be no conflicts to resolve.
10. Commit your changes into a single commit (they should already be added).
```
git commit -m "Your description of feature"
```
11. Push your changes to master
```
git push origin master
```

Some notes:
For clarity, I use the full push/pull syntax. This is not necessary if you have your branches tracking correctly.
This process will leave your full history in place in your feature branch.
Unfortunately, if you DO need to make a change to your work after moving to master, it may make it slightly more difficult (since all of your other changes are already there).
As personal preference, I try to do all of my work to/from master using the local master branch. You could have pulled the remote changes to master into your local feature branch, instead of checkout out master, pulling them in there, and then doing a merge (though you would still have to pull when back in master anyway). I like this because then you are sure you are keeping your local master as up to date with origin master as any other branch will be and you resolve any conflicts there.

## Rebasing[¶](#Rebasing)

### What is a rebase[¶](#What-is-a-rebase)

According to the man pages (which you should read; man git-rebase), a rebase will "forward-port local commits to the updated upstream head". Basically what this means is that you can change the starting point of your commits. This is most commonly used (including in this document) to replay your work on top of work that was pushed after you started your work. Doing with a pull with rebase means that your changes will be applied on top of the latest changes that were pushed.

### Rebasing isn't always good[¶](#Rebasing-isnt-always-good)

Rebasing may be used to make your life a little easier. However, it can also just as easily make your life harder. Or worse, make one of your co-workers life's harder.  You are rewriting history. This is not always a good thing.
Before rebasing, make sure it is what you want to do. If you have already pushed your changes to a remote branch and especially if you have knowledge that someone already checked them out to their machine, please let them know. Otherwise you may be destroying git history their changes are working on.
Some reading material:
[http://paul.stadig.name/2010/12/thou-shalt-not-lie-git-rebase-ammend.html](http://paul.stadig.name/2010/12/thou-shalt-not-lie-git-rebase-ammend.html)
[http://blog.codesherpas.com/on_the_path/2010/10/git-rebase-in-anger.html](http://blog.codesherpas.com/on_the_path/2010/10/git-rebase-in-anger.html)
[http://alexvollmer.com/posts/2009/01/31/rewriting-history-with-git/](http://alexvollmer.com/posts/2009/01/31/rewriting-history-with-git/)
[http://git-scm.com/docs/git-rebase/1.7.6](http://git-scm.com/docs/git-rebase/1.7.6)
[http://gitready.com/intermediate/2009/01/31/intro-to-rebase.html](http://gitready.com/intermediate/2009/01/31/intro-to-rebase.html)
[http://stackoverflow.com/questions/2302736/trimming-git-checkins-squashing-git-history/](http://stackoverflow.com/questions/2302736/trimming-git-checkins-squashing-git-history/)
[http://stackoverflow.com/questions/2320772/redoing-commit-history-in-git-without-rebase](http://stackoverflow.com/questions/2320772/redoing-commit-history-in-git-without-rebase)
[http://stackoverflow.com/questions/2427238/in-git-what-is-the-difference-between-merge-squash-and-rebase](http://stackoverflow.com/questions/2427238/in-git-what-is-the-difference-between-merge-squash-and-rebase)
[http://stackoverflow.com/questions/5189560/how-can-i-squash-my-last-x-commits-together-using-git](http://stackoverflow.com/questions/5189560/how-can-i-squash-my-last-x-commits-together-using-git)
[http://stackoverflow.com/questions/7275508/is-there-a-way-to-squash-a-number-of-commits-non-interactively](http://stackoverflow.com/questions/7275508/is-there-a-way-to-squash-a-number-of-commits-non-interactively)
Don't do this: [http://viget.com/extend/only-you-can-prevent-git-merge-commits](http://viget.com/extend/only-you-can-prevent-git-merge-commits)

### When to rebase your branch against master[¶](#When-to-rebase-your-branch-against-master)

*   Before setting a ticket to "Ready for Testing".
*   After fixing a bug that a tester found.
*   You need to develop with specific code that was introduced to master.
*   You haven't updated your branch in a while.

### Rebasing against master[¶](#Rebasing-against-master)

Before rebasing, make sure:

*   You are working alone on a feature branch **OR** [you have told other developers to stop working and push their progress](#Rebasing-a-shared-branch-against-master).
*   You have reached a comfortable stopping point with no glaring errors.
*   You are okay with losing your branch's history up until this point (if not, [back up your branch](#Creating-a-backup-of-the-current-branch)).</div>

1. [Switch to/update master branch](#Switching-toupdating-a-local-branch).
2. Switch back to your branch:
```
git checkout 1234_my_feature
git submodule update
```
3. Rebase against master (and [solve conflicts](#Solving-a-rebase-conflict), if any):
```
git rebase master
git submodule init
git submodule update
```
4.  Force push to the git server:
```
git push -f
```

### Squashing to one commit to reduce noise[¶](#Squashing-to-one-commit-to-reduce-noise)
See above warnings about rebasing.
If you want to save your branch's history up to this point, [back it up](#Creating-a-backup-of-the-current-branch) first.

1. Do an interactive rebase against your original branch point:
```
git rebase -i $(git merge-base HEAD master)
```
Your editor will open with a file that looks similar to this:
```
pick 07a34b9 Added file 1.
pick 22ada84 Fixed file 1. Add file 2.
pick e0ed823 Added file 3 finally.
pick 2a5ce20 File 4, fixing other bugs.
```
2. Change the word "pick" to "s" or "squash" for **all but the first commit**, e.g.:
```
pick 07a34b9 Added file 1.
s 22ada84 Fixed file 1. Add file 2.
s e0ed823 Added file 3 finally.
s 2a5ce20 File 4, fixing other bugs.
```
3. Save and exit the editor.
Another editor will open to allow you to edit the squashed commit message:

```
# This is a combination of 4 commits.
# The first commit's message is:
Added file 1.

    # This is the 2nd commit message:

    Fixed file 1. Add file 2.

    # This is the 3rd commit message:

    Added file 3 finally.

    # This is the 4th commit message:

    File 4, fixing other bugs.
```

4.  Edit the commit message to be a summary (instead of a combination of) the commits, e.g.:

```
Added files 1-4, and fixed some bugs.
```
5.  Save and exit the editor.

Here is a [script](https://github.com/Navisite/rndtools/blob/master/tools/squash) that will automate the squashing.
Please don't use it until you understand the process manually (and then when you do please improve it if possible).

## Conflict resolution[¶](#Conflict-resolution)

### Solving a rebase conflict[¶](#Solving-a-rebase-conflict)

1. Check to see what's conflicting:
```
git status
```
2. If there's a submodule conflict, you have to [handle that separately](#Submodule-conflicts-while-rebasing-against-master).
3. Execute your visual diff tool for each conflict:
```
git mergetool
```
  (Alternatively, you may hand-edit the conflicted files. Only worry about files that are "both changed".)
4. Meld shows three files:
   * file.py.LOCAL.XXXXX = new code from master branch
   * file.py = the attempted/half-finished merge of the two
   * file.py.REMOTE.XXXXX = the code from your feature branch
5. Edit only file.py; the other two are temporary.
6. When finished, save and exit Meld.
7. Add the new changes only and continue **(don't commit)**:
```
git add file.py
git rebase --continue
```
If you are stopped more than once or twice to resolve conflicts during a rebase, you should consider [aborting the rebase](#Aborting-a-rebase) and [squashing your commits to one](#Squashing-to-one-commit-to-reduce-conflicts) before trying again.

## Shared development/integration branches[¶](#Shared-developmentintegration-branches)

### Rebasing a shared branch against master[¶](#Rebasing-a-shared-branch-against-master)
1. Tell everyone else to finish and push to the shared branch.
2. Wait until they've all done this.
3. Update your local copy:
```
git checkout 1234_my_feature
git pull --rebase
git submodule init
git submodule update
```
4. Do the rebase and force push.
5. Tell everyone that you're done and that they should delete and re-checkout the branch.

Here is a [script](https://github.com/Navisite/rndtools/blob/master/tools/rebase) to do this, including stashing local changes you don't want to commit.
Don't use it until you understand what it is doing (and then please improve it if you find shortcomings).

### After someone else rebases a shared branch[¶](#After-someone-else-rebases-a-shared-branch)
1.  Update your git database by [switching to and updating master branch](#Switching-toupdating-a-local-branch).
2.  Delete the branch and re-checkout:
```
git branch -D 1234_my_feature
git checkout -t origin/1234_my_feature
git submodule init
git submodule update
```

## Submodules[¶](#Submodules)

Submodules are:

* By themselves, separate repositories.
* When in a parent project, simply a pointer to a specific commit.

### Developing a feature that requires submodule changes[¶](#Developing-a-feature-that-requires-submodule-changes)

1.  Once you have created a feature branch, go in and make a new branch in the submodule:
```
cd lib/cldcom
git checkout master
git pull --rebase
git checkout -b 1234_my_feature
```
2.  Do development like you would with a regular feature branch, e.g.:
```# Do some work and commit...
git add file.py
git commit -m "Submodule feature"git push -u
# Or rebase your current work against master to update...
git checkout master
git pull --rebase
git checkout 1234_my_feature
git rebase master
git push -f
```
You must push the submodule changes before you push the main project that uses them. Otherwise, you'll break the repo for other people!

3. Go back to main project and add submodule pointer:
```
cd ../../
git add lib/cldcom
git commit -m "Updating submodule."
```

### Submodule conflicts while rebasing against master[¶](#Submodule-conflicts-while-rebasing-against-master)

These should only happen when you have also changed code in the submodule in your branch.

1. Go into the submodule, rebase your branch against master:
```
git checkout master
git pull --rebase
git checkout 1234_my_feature
git rebase master
git push -f
```
2. Go back to main project, add submodule pointer:
```
cd ../../
git add lib/cldcom
```
3. If there aren't other conflicts, continue the rebase:
```
git rebase --continue
```

### What does "new commits" mean in `git status`?[¶](#What-does-new-commits-mean-in-git-status)

* If you just switched branches, remember to update your submodules to correspond to the versions the new branch needs:
```
git submodule update
```
* If you were doing development in the submodules, remember to follow the [submodule development steps](#Developing-a-feature-that-requires-submodule-changes).

### What "untracked content" mean in `git status`?[¶](#What-untracked-content-mean-in-git-status)
* You edited something in a submodule without committing it. Go into the submodule directory to see what it is.
* If you were doing development in the submodules, remember to follow the [submodule development steps](#Developing-a-feature-that-requires-submodule-changes).

### How to determine which branch a submodule is set to[¶](#How-to-determine-which-branch-a-submodule-is-set-to)

This is difficult, because submodules are not actually set to a branch; they are set to a commit, which can be part of more than one branch. When inside of the submodule's directory, issue this command:
```
When inside a submodule directory:
git branch -a --contains HEAD
```

* This indicates the submodule is definitely on master:
```
* (no branch)
  remotes/origin/HEAD - origin/master
  remotes/origin/master
```
* This indicates the submodule is definitely on the 1234 feature branch:
```
* (no branch)
  1234_my_feature
  remotes/origin/1234_my_feature
```
* But if you get more than these results, you can't know for sure. You'll have to talk to the creator of the main feature branch to see what they set it to.


## One-time setup tasks[¶](#One-time-setup-tasks)

### Cloning a repository initially[¶](#Cloning-a-repository-initially)

#### Cloning a repo from Github[¶](#Cloning-a-repo-from-Github)
```
cd ~/src/git
git clone git@github.com:Navisite/cloud-ui.git
```

#### Cloning a repo from an internal Git server[¶](#Cloning-a-repo-from-an-internal-Git-server)
```
cd ~/src/git
git clone ssh://rnd@10.208.9.55/git/portal.git
```

### Setting up visual diff/conflict resolution[¶](#Setting-up-visual-diffconflict-resolution)

Git can be configured to use an external diff or merge tool (or both).  In this example we will use Meld, a visual diff tool.

#### meld as conflict resolution tool[¶](#meld-as-conflict-resolution-tool)

1.  Install Meld:
```
sudo apt-get install meld
```
2.  Now, when you use [git merge-tool](#Conflict-resolution) to resolve conflicts, meld should show up as the default option (or you may need to type it).

#### Meld as diff tool[¶](#Meld-as-diff-tool)

If you don't like looking at text diffs, you can also use meld as the output when you issue a `git diff`.

1. Create a wrapper script in your home folder called "`.git-diff.sh`" (you can place this file elsewhere if you like):
```#!/bin/bash
meld "$2" "$5"```
2. Make your wrapper script executable:
```
chmod +x ~/.git-diff.sh
```
3. Tell git to use the wrapper script for diffs:
```
git config --global diff.external /home/USER/.git-diff.sh
```

For OSX, you can use [DiffMerge](http://www.sourcegear.com/diffmerge/).
Your wrapper script will contain the following:

```
#!/bin/bash
/Applications/DiffMerge.app/Contents/MacOS/DiffMerge -nosplash "$2" "$5"
```

Some notes about using meld as a diff tool:

* When doing a `git diff`, an instance of meld will be opened for each changed file, consecutively. If you want to cancel this process, go back to the prompt and CTRL-C.
* If you would like to use a text diff just once without undoing the meld config:
```git diff --no-ext-diff```
* Meld will likely show an error for submodule changes, or other irregular changes. Meld's not smart about git-related stuff, so just close that instance and move on.


## Miscellaneous tasks[¶](#Miscellaneous-tasks)

### Creating a backup of the current branch[¶](#Creating-a-backup-of-the-current-branch)
```
git branch 1234_my_feature_backup
```

### Aborting a rebase[¶](#Aborting-a-rebase)

```
git rebase --abort
```

You should also delete any temporary conflict files ending in `.orig` that may be present.

## Advanced Git stuff[¶](#Advanced-Git-stuff)

### Reversing the changes a commit made[¶](#Reversing-the-changes-a-commit-made)

Take a look here: [http://christoph.ruegg.name/blog/git-howto-revert-a-commit-already-pushed-to-a-remote-reposit.html](http://christoph.ruegg.name/blog/git-howto-revert-a-commit-already-pushed-to-a-remote-reposit.html)
And here: [https://code.google.com/p/git-core/source/browse/Documentation/howto/revert-a-faulty-merge.txt](https://code.google.com/p/git-core/source/browse/Documentation/howto/revert-a-faulty-merge.txt)

* Revert will make a new commit that is the exact opposite of the specified commit. Use the --no-commit if you don't want to autocommit the change.
```
git revert SHA
```

### Copy an individual commit to another branch[¶](#Copy-an-individual-commit-to-another-branch)

1.  Switch to the destination branch.
2.  Cherry-pick the commit you want. Use the --no-commit switch if you don't want to autocommit the change.
```
git cherry-pick SHA
```

### How do I see what remote branch my branch is pointing to?[¶](#How-do-I-see-what-remote-branch-my-branch-is-pointing-to)

```
git remote show origin
```

### Looking at a file from another branch or commit[¶](#Looking-at-a-file-from-another-branch-or-commit)

```
git show SHA:path/to/file.py
git show branch:path/to/file.py
```

### Create git patches for emailing[¶](#Create-git-patches-for-emailing)

```
git format-patch -M -C -1
```

The patch files are numbered '0001-*' to 'nnnn-*' and are formatted to be ready to email or attach to a bug ticket.

This example gives the '-1' argument to tell format-patch to generate a patch based on the last 1 checkins. To get checkins since a given revision, use a non-ambiguous stem of the SHA checksum, or if it had a branchname just use that. See the docs above for proper identifiers. The '-M -C' arguments tell it to detect copies and renames, they're just a good habit and often not necessary.

### Deleting a remote branch[¶](#Deleting-a-remote-branch)

```
git push origin :[remote branch] #Note the colon
```

### Make a local branch into a tracking branch[¶](#Make-a-local-branch-into-a-tracking-branch)

```
git branch --set-upstream 1234_my_feature origin/1234_my_feature
```

### Abandon local changes and revert to what's on the remote branch[¶](#Abandon-local-changes-and-revert-to-whats-on-the-remote-branch)

```
git fetch origin
git reset --hard origin/1234_my_feature
```

### Clean up old remote branches from the local repository[¶](#Clean-up-old-remote-branches-from-the-local-repository)

```
git remote update --prune
```

### How do I see the diff compared to the current master?[¶](#How-do-I-see-the-diff-compared-to-the-current-master)

```
git diff master
```

### How do I see what's on a branch, ignoring newer changes from master?[¶](#How-do-I-see-whats-on-a-branch-ignoring-newer-changes-from-master)

```
git diff $(git merge-base HEAD master)
```

### How do I see what files I have changed, compared to master?[¶](#How-do-I-see-what-files-I-have-changed-compared-to-master)

```
git diff --name-only master
```

### How do I the commit message of the latest commit?[¶](#How-do-I-the-commit-message-of-the-latest-commit)

If you accidentally gave something a wrong commit message and you have not yet pushed the commit, fixing the commit message is pretty easy.

```
git commit --amend
```

However, if you already pushed, make sure that nobody has pulled (and you will then need to re-push with a force).

### How do I see what commits I have made, compared to another branch?[¶](#How-do-I-see-what-commits-I-have-made-compared-to-another-branch)

```
git log [branch1 name]..[branch2_name]
```

Example: Compare local _master_ to remote _master_ after a fetch

```
git log master..origin/master
```

### View an individual commit[¶](#View-an-individual-commit)

```
git show SHA
```

### Finding when and where an issue was introduced[¶](#Finding-when-and-where-an-issue-was-introduced)

Since everybody makes mistakes and may break one thing while they are working on fixing something else, git provides us with the ability to quickly figure out what commit introduced the problem.
See: [http://webchick.net/node/99](http://webchick.net/node/99), [http://robots.thoughtbot.com/git-bisect](http://robots.thoughtbot.com/git-bisect)

```
git bisect
```

### Recovering (some) lost work[¶](#Recovering-some-lost-work)

Sometimes it may be beneficial to revive work that was lost doing a reset, rebase, or similar command. Git keeps track of lots of actions you take and since Git uses snapshots, you generally can recover what you need.
See: [http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html](http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html)

```
git reflog
```

### Notes on History[¶](#Notes-on-History)

History can prove to be very important. It allows you to see what happened over time and see how development progressed. Having your full history allows you to revert to any point in time and work from there. If you are like me and make sure you make commits when you have tackled the larger tasks of your work, this means you can always get back to a working state and start again. Through this, git allows for easy experimentation without fear of losing good work.
Additionally, you can learn about a developer and their coding process by looking at their git history. History can help make it clear if a developer tried a specific path and realized it didn't work before trying the solution they submitted.
That's why history can be very important. It can save hours or days of development or troubleshooting.

### Links:[¶](#Links)

[http://owenou.com/2012/01/13/ten-things-you-didnt-know-git-and-github-could-do.html](http://owenou.com/2012/01/13/ten-things-you-didnt-know-git-and-github-could-do.html)

# Footer[¶](#Footer)

* [git](/projects/cloud/wiki_extensions/tag?tag_id=36)
* [submodules](/projects/cloud/wiki_extensions/tag?tag_id=640)
* [squash](/projects/cloud/wiki_extensions/tag?tag_id=641)
* [rebase](/projects/cloud/wiki_extensions/tag?tag_id=642)
