###############################################################################
#                          FOR LINUX                                          #
###############################################################################

# Create semi links for config files
ln -sf ~/Dropbox/src/linux_bashrc ~/.bashrc
ln -sf ~/Dropbox/src/linux_emacs ~/.emacs
ln -sf ~/Dropbox/src/fonts ~/.fonts
ln -sf ~/Dropbox/src/gitignore ~/.gitignore
ln -sf ~/Dropbox/src/gitconfig ~/.gitconfig
ln -sf ~/Dropbox/src/git-completion ~/.git-completion
ln -sf ~/Dropbox/src/emacs.d ~/.emacs.d

# Install necessary tools
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-mode
sudo apt-get install keychain

# Install tool to set mouse focus, search 'Advanced Setting' for making changes
sudo apt-get install gnome-tweak-tool

# For Github
cd ~/.ssh
ssh-keygen -t rsa -C "cyandterry@hotmail.com"
ssh-add id_rsa

sudo apt-get install xclip
# Paste to Github
xclip -sel clip < ~/.ssh/id_rsa.pub

# Tool for ssh
sudo apt-get install openssh-client openssh-server

# Setup global gitignore
git config --global core.excludesfile '~/.gitignore'

# Setup ntp, which syncs the time from website
sudo apt-get install ntp

###############################################################################
#                          FOR MAC                                            #
###############################################################################
ln -sf ~/Dropbox/src/mac_bashrc ~/.bash_profile
ln -sf ~/Dropbox/src/mac_emacs ~/.emacs
ln -sf ~/Dropbox/src/fonts ~/.fonts
ln -sf ~/Dropbox/src/gitignore ~/.gitignore
ln -sf ~/Dropbox/src/gitconfig ~/.gitconfig
ln -sf ~/Dropbox/src/git-completion ~/.git-completion
ls -sf ~/Dropbox/src/emacs.d ~/.emacs.d
