<h1 align="center"> 🛠️ FIXARR  </h1>

<h4 align="center"> Movie & Tv Renamer With Backup Media Server (Plex / Emby / Jellyfin)</h4>

<p style="text-align:center;" align="center">
  <img align="center" src="https://cdn.staticaly.com/gh/sachinsenal0x64/picx-images-hosting@master/logov2.5sr31yyd76w0.png" width="256px" height="256px"/>
</p>

# 🖼️ GUI

![FIXARR)](https://cdn.staticaly.com/gh/sachinsenal0x64/picx-images-hosting@master/fixarr-ui.dkw2033foqo.png)

<br>

## 🚀 Features

- 🎬 MOVIE RENAMER
- 📺 TV RENAMER
- 👧 ANIME RENAMER (⭕ in progress)
- 🔺 PLEX BACKUP
- ⚡️ MULTI THREADING
- ♻ PURG UNNECESSARY FILES (NFO,SRT)
- 🐟 JELLYFIN BACKUP (⭕ in progress)
- ❄ EMBY BACKUP (⭕ in progress)
- ⏬ MOVIE & TV SEACHER (⭕ in progress)
  
- 💎 FALLBACK SERVERS  (IF RENAME PROCESS FAIL ITS TRY OTHER SOURCES TO SCRAP CORRECT NAME  THIS API IS PRIVATE ONLY AVAILABLE IN [RELEASES](https://github.com/sachinsenal0x64/FIXARR/releases) BUT ITS ALSO HAVE IN SOURCE CODE WITHOUT API KEY AND ENDPOINTS BTW IF YOUR DEVELOPER YOU CAN REPLACE WITH IMDB API)

<br>

## 💡 Pros

- 🍕 Accurate Results (Even Torrent Movies Can Rename Without Any Issue)
- 🆓 Fully Free And Open Source
- 🧰 All in One Place
- 🧾 Easy to Use

<br>

## 👎 Cons

- 🐌 Slowly Develop

<br>

## 🏮 NOTE

## 🚀 Some Features are Still in Development :)


<br>


## 🆕 BETA CHANNEL

[BETA](https://github.com/sachinsenal0x64/FIXARR)


<br>

# 📐 INSTALLATION

<br>


#### 🏮 YOU DONT WANT TO COMPILE FROM SOURCE CODE ITS OPTIONAL. YOU CAN GET PREBUILD INSTALLER FROM [RELEASES](https://github.com/sachinsenal0x64/FIXARR/releases)

# 💻 From Source [MODE: HARD]

<br>

## 🗝 .ENV SETUP (Important):

<br>

- Rename **.env.example** to **.env**
  
- You can get api key from [THE MOVIE DB](https://www.themoviedb.org/settings/api?language=en-US) and its totally free.

```
TMDB_API_KEY=tmdbkey
```

<br>

🐧For GNU/Linux :

```Terminal

🐧 Debian Based Distros :

sudo apt-get install software-properties-common
sudo apt-get install python3.10


pip3 install customtkinter
pip3 install -r requirements.txt
python3 fixarr.py


🐧 Fedora Based Distros:

sudo dnf install python3
pip3 install customtkinter

pip3 install -r requirements.txt
python3 fixarr.py

```

<br>

🍎 For macOS :

```Terminal

For Mac OS With BREW:

if you already not install brew then install its from offical site : https://brew.sh/#install 

brew install python3

pip3 install customtkinter
pip3 install -r requirements.txt
python3 fixarr.py

```

<br>

🚪 For Windows:

```CMD
First Install Python (python.org) 

pip install -r requirements.txt
python fixarr.py


or just run .bat File also you can create bat_shortcut
```

<br>

## 🏮 NOTE

<br>

#### IF YOU WANT TO MAKE OWN STANDALONE APP (AKA .EXE or .BIN) USE NUITKA TO COMPILE SOURCE CODE INTO C 
<br>

```compile

[Install C Compiler  (http://www.codeblocks.org/downloads/binaries/) and download (including compiler) setup & to work with this setup GCC env path (C:\Program Files\CodeBlocks\MinGW\bin) in your OS SYSTEM ENV ] 

open your cmd in Fixarr PATH

pip -v install nuitka 

nuitka --mingw64 --standalone --windows-icon-from-ico=./assets/favicon.ico --include-data-dir=./assets=./assets --windows-company-name=FIXARR --product-name=FIXARR --product-version=0.1.0  --file-version=0.1.0 --plugin-enable=tk-inter fixarr.py
```

### GNU/LINUX



```
nuitka3 --clang --standalone --windows-icon-from-ico=./assets/favicon.ico --include-data-dir=./assets=./assets --windows-company-name=FIXARR --product-name=FIXARR --product-version=0.1.0  --file-version=0.1.0 --plugin-enable=tk-inter -o fixarr.bin fixarr.py

```


<br>

## 💡 CREDITS

#### MOVIE API & TV :  [THEMOVIEDB.ORG](https://wwww.themoviedb.org)
#### PARSER LIBARY FOR TV SERIES: [PTN PROJECT](https://github.com/platelminto/parse-torrent-title)

<br>
<br>


<p style="text-align:center;" align="center">
   <a href="https://www.themoviedb.org">
  <img align="center" src="https://github.com/FIXARR/FIXARR/blob/279c46c7744bfdbb2e99dd802637cea65d2fdc3d/assets/tmdb.svg" height="200"/>
   </a>
</p>

## License

MIT
