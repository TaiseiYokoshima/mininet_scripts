#!/bin/bash


sudo apt update
sudo apt upgrade -y

sudo snap install nvim --classic
sudo apt-add-repository ppa:fish-shell/release-3 -y
sudo apt update


sudo apt install -y build-essential python3-ven fish stow nodejs npm net-tools


git clone https://github.com/TaiseiYokoshima/dotfiles
cd ~/dotfiles

stow fish
stow zellij
stow nvim





curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh



cargo install zellij



