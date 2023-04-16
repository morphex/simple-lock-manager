# simple-lock-manager
Simple set of scripts to manage file-based locks, for example for shell scripting

One use-case is if you have an application that stores its files for example in

$HOME/.myapp

and you want to be able to switch between different profiles by
pointing (symlinking) $HOME/.myapp to $HOME/myapp/profile1 or
$HOME/myapp/profile2 in a script.

Examples of basic profile switch is in examples.

Basic use is

./get_lock.py lockname

to acquire a lock, and

./remove_lock.py lockname to release a lock.

Locks do not persist between reboots, and default storage of locks is
in $HOME/.simple-lock-manager
