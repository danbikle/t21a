# README

To work on this app, you need to follow these steps to setup your dev-environment:

* Get an Ubuntu 16.04 Linux host
* Add this syntax to ~/.bashrc:

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
gem install bundler
```

* Next, clone this app:

```
git clone git@bitbucket.org:bikle/t21a.git
```

* Then, install its packages:

```
cd t21a
bundle install
```

* Next, install Anaconda Python:

```
wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash Anaconda3-5.2.0-Linux-x86_64.sh -b
mv ~/anaconda3/bin/curl  ~/anaconda3/bin/curl_ana
echo 'export PATH="${HOME}/anaconda3/bin:$PATH"' >> ~/.bashrc
```

* Then, install Node.js:

```
cd ~
wget https://nodejs.org/dist/v10.7.0/node-v10.7.0-linux-x64.tar.xz
tar xf node-v10.7.0-linux-x64.tar.xz
ln -s  node-v10.7.0-linux-x64 node
echo 'export PATH="${HOME}/node/bin:$PATH"' >> ~/.bashrc
bash
```