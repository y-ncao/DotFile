## Create semi links for config files
```bash
# For linux
ln -sf ~/src/git/DotFile/bashrc/bashrc ~/.bashrc

# For Mac
ln -sf ~/src/git/DotFile/bashrc/bashrc ~/.bash_profile

ln -sf ~/src/git/DotFile/emacs/linux_emacs ~/.emacs
ln -sf ~/src/git/DotFile/emacs/emacs.d ~/.emacs.d

ln -sf ~/src/git/DotFile/fonts ~/.fonts

ln -sf ~/src/git/DotFile/git/gitignore ~/.gitignore
ln -sf ~/src/git/DotFile/git/gitconfig ~/.gitconfig
ln -sf ~/src/git/DotFile/git/git-completion ~/.git-completion

ln -sf ~/src/git/DotFile/tmux/tmux.conf ~/.tmux.conf
```

## For Github
```bash
cd ~/.ssh
ssh-keygen -t rsa -C "cyandterry@hotmail.com"
ssh-add id_rsa

# gitignore
git config --global core.excludesfile '~/.gitignore'

# Linux only, Paste to Github
sudo apt-get install xclip

xclip -sel clip < ~/.ssh/id_rsa.pub
```

## Install necessary tools
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-mode
sudo apt-get install keychain
```

## Install tool to set mouse focus, search 'Advanced Setting' for making changes
```bash
sudo apt-get install gnome-tweak-tool
```

## Tool for ssh
```bash
sudo apt-get install openssh-client openssh-server
```


## Setup ntp, which syncs the time from website
```bash
sudo apt-get install ntp
```

## Iterm2

This is deprecated. You just need to sync it from dropbox
[Install](http://iterm2.com/)
Check this [config](http://imwuyu.me/talk-about/cool-iterm2.html/) and [theme](https://github.com/mbadolato/iTerm2-Color-Schemes)

1. Update theme to Monokai Soda
2. Update Font
3. Set global show/hide key
4. Preference -> Keys -> Remap Modifier Keys. Swap left option and left command
5. Preference -> Profiles -> Keys -> Left option key act as  +Esc

## Atom
1. Install `sync-settings`
2. 51b0d73b77c1f3a01ebaafab1043f073c22e9169 - pat
3. 68389d5f56c6c053163cb0369f44cdaf - gid
