#!/bin/bash


SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mininet_setup="$SCRIPT_DIR/setup_mininet.bash"

sudo apt update
sudo apt install -y build-essential
source ~/.bashrc



curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


sudo apt upgrade -y

sudo snap install nvim --classic
sudo apt-add-repository ppa:fish-shell/release-3 -y
sudo apt update


sudo apt install -y python3-venv fish stow npm net-tools ripgrep zip python3-pip curl
source ~/.bashrc

curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh


sudo apt update
sudo apt-get install -y nodejs
source ~/.bashrc
rm ./nodesource_setup.sh



cd ~
git clone https://github.com/TaiseiYokoshima/dotfiles



cd ~/dotfiles


mkdir -p ~/.config

stow fish
stow zellij
stow nvim




~/.cargo/bin/cargo install zellij
~/.cargo/bin/cargo install exa

cd ~

sudo chsh -s /bin/fish mininet

bash "$mininet_setup"



