#!/bin/bash


cd ~

git clone https://github.com/mininet/mininet



cd mininet


git checkout -b mininet-2.3.0 2.3.0




sed -i 's/^\(\s*\)git clone git/\1git clone https/' ./util/install.sh
sed -i 's/\(.*\)python2 python3/\1python3/' ./util/install.sh


cd ~


./mininet/util/install.sh -a

