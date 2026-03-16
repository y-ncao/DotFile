# DotFile

Dotfiles managed with [chezmoi](https://www.chezmoi.io/).

## Managed configs

- **zsh** — `.zshrc`, `.zprofile`, `.p10k.zsh` (Powerlevel10k)
- **git** — `.gitconfig`, `.config/git/ignore`
- **ghostty** — `.config/ghostty/config`
- **yazi** — `.config/yazi/yazi.toml`
- **emacs** — `.emacs` (Monokai theme, markdown-mode)

## New machine setup

### 1. Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv zsh)"
```

### 2. Install tools

```bash
brew install --cask ghostty
brew install chezmoi git zoxide yazi lazygit emacs aspell
```

### 3. Install Oh My Zsh + Powerlevel10k

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 4. Apply dotfiles

```bash
chezmoi init --apply https://github.com/y-ncao/DotFile.git
```

### 5. Set chezmoi source directory

```bash
echo 'sourceDir = "'$(chezmoi source-path)'"' > ~/.config/chezmoi/chezmoi.toml
```

### 6. Restart shell

```bash
exec zsh
```

## Day-to-day usage

```bash
# Edit a dotfile, then sync to repo
chezmoi re-add

# Pull latest on another machine and apply
chezmoi update

# See what would change
chezmoi diff
```

## Archive

Old configs (bashrc, iterm2, tmux, awesome, etc.) are preserved in `.archive/` with full git history.
