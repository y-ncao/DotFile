####Create semi links for config files
```bash
ln -sf ~/src/git/DotFile/bashrc/bashrc ~/.bashrc

ln -sf ~/src/git/DotFile/linux_emacs ~/.emacs
ln -sf ~/src/git/DotFile/emacs.d ~/.emacs.d

ln -sf ~/src/git/DotFile/fonts ~/.fonts

ln -sf ~/src/git/DotFile/git/gitignore ~/.gitignore
ln -sf ~/src/git/DotFile/git/gitconfig ~/.gitconfig
ln -sf ~/src/git/DotFile/git/git-completion ~/.git-completion
```

####For Github
```bash
cd ~/.ssh
ssh-keygen -t rsa -C "cyandterry@hotmail.com"
ssh-add id_rsa

# gitignore
git config --global core.excludesfile '~/.gitignore'

# Linux only
sudo apt-get install xclip
# Paste to Github
xclip -sel clip < ~/.ssh/id_rsa.pub
```

####Install necessary tools
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-mode
sudo apt-get install keychain
```

####Install tool to set mouse focus, search 'Advanced Setting' for making changes
```bash
sudo apt-get install gnome-tweak-tool
```

####Tool for ssh
```bash
sudo apt-get install openssh-client openssh-server
```


####Setup ntp, which syncs the time from website
```bash
sudo apt-get install ntp
```
