#!/bin/bash

old_directory=$PWD
cd $HOME
./simple-lock-manager/get_lock.py emacs
if [ $? -ne 0 ]; then
    echo "Error, exiting"
    exit 1
fi
if [[ ! -L .emacs ]]; then
    echo ".emacs not a symbolic link, exiting."
    exit 1
fi

rm -f .emacs
ln -s .emacs-custom .emacs

cd $old_directory
emacs "$@"
$HOME/simple-lock-manager/remove_lock.py emacs
