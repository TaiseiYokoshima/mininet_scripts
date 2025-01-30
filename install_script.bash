#!/bin/bash



sudo apt update

sudo apt install -y build-essential
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


sudo apt upgrade -y

sudo snap install nvim --classic
sudo apt-add-repository ppa:fish-shell/release-3 -y
sudo apt update


sudo apt install -y python3-venv fish stow nodejs npm net-tools ripgrep zip python3-pip
source ~/.bashrc


git clone https://github.com/TaiseiYokoshima/dotfiles



cd ~/dotfiles


mkdir -p ~/.config

stow fish
stow zellij
stow nvim








cargo install zellij
cargo install exa

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mininet_setup="$SCRIPT_DIR/setup_mininet.bash"


bash "$mininet_setup"
