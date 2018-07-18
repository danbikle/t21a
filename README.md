# README

To work on this app, you need to follow these steps to setup your dev-environment:

* Get an Ubuntu 16.04 Linux host
* Add this syntax to .bashrc:

```

if [ -e ${HOME}/.rbenv ]; then
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(rbenv init -)"
fi
```

* Install Ruby 2.5.1 with these shell commands:

```
cd ~
git clone https://github.com/rbenv/rbenv .rbenv
git clone https://github.com/rbenv/ruby-build.git .rbenv/plugins/ruby-build
bash
rbenv install 2.5.1
rbenv global  2.5.1
```
