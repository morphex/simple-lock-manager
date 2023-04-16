#!/bin/bash

old_directory=$PWD
cd /home/morphex
if [[ ! -L .emacs ]]; then
    echo ".emacs not a symbolic link, exiting."
    exit 1
fi

rm -f .emacs
ln -s .emacs-plain .emacs

cd $old_directory
emacs "$@"
