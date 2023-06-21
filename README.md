[![Deploy static content to Pages](https://github.com/neoalienson/01man.com/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/neoalienson/01man.com/actions/workflows/pages/pages-build-deployment)

## Use with Docker
docker build . -t hexo
docker create --name=hexo -v /home/neo/Projects/01man.com/hexo-blog:/app -p 4000:4000 -p 3001:3001 hexo

## Setup hexo
   cd ./hexo-blog
   # required by mozjpeg
```# Mac
   brew install automake
   brew install libpng
```# Linux
   sudo apt install libpng-dev 
   sudo apt install auto-conf # required by hexo-all-minifier

   npm install

## Generate static site to hexo-blog to preview
    cd ./hexo-blog
    hexo server # start the local webserver to preview

# Theme
git clone https://github.com/viosey/hexo-theme-material.git material

## Setup GitHub Actions Runner
Docker cannot be used as the setup requires systemd

### Prerequisite
1. Create a new VM with Ubuntu
2. Install lates Node.js
3. sudo apt install libpng-dev
4. sudo npm install hexo-cli -g

### Setup GitHub Actions Runner
1. Download the latest runner package
2. unpack the package
3. run ./config.sh
4. run ./svc.sh install root
5. run ./svc.sh start

### Setup Chrome
1. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
2. sudo dpkg -i google-chrome-stable_current_amd64.deb
