#!/bin/bash


sudo apt install update
sudo apt install upgrade -y

sudo apt install build-essential
sudo apt install python3-venv


sudo snap install nvim --classic

sudo apt-add-repository ppa:fish-shell/release-3
sudo apt update
sudo apt install fish
sudo apt install stow

git clone https://github.com/TaiseiYokoshima/dotfiles $HOME/dotfiles

cd $HOME/dotfiles

stow fish
stow zellij
stow nvim





curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh



