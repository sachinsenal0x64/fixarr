
<p style="text-align:center;" align="center">
  <img align="center" src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/picx-images-hosting@master/logov2.5sr31yyd76w0.png" width="256px" height="256px"/>
</p>

<h1 align="center"> 🛠️ FIXARR  </h1>

<h4 align="center"> 🍿 Ultimate Movie | TV | Anime Renamer with Backup Media Servers (Plex | Emby | Jellyfin)</h4>

<br><br>

# 💕 Community

> 🍻 Join the community:  <a href="https://discord.gg/EbfftZ5Dd4">Discord</a>
> [![](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/discord.72y8nlaw5mdc.webp)](https://discord.gg/EbfftZ5Dd4)
 
<br>

# 🖼️ GUI

![FIXARR)](https://sachinsenal0x64.github.io/picx-images-hosting/Screenshot_20230920_223402.4i08ima1b4s0.png)


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
- 💎 FALLBACK SERVERS
- ✅ CROSS PLATFORM SUPPORT
  
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

# 📐 INSTALLATION

<br>


# 💻 From Source [MODE: HARD]

<br>

## 🗝 .ENV SETUP (Optional):

<br>

>Optional

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


or just run .sh File

```

<br>

🍎 For macOS :

```Terminal

For Mac OS With BREW:

if you already not install brew then install its from offical site : https://brew.sh/#install 

brew install python3
brew install python-tk
pip3 install customtkinter
pip3 install -r requirements.txt
python3 fixarr.py


or just run .sh File

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

### WINDOWS

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

#### MOVIE & TV API :  [THEMOVIEDB.ORG](https://wwww.themoviedb.org)
#### PARSER FOR TV SERIES: [PTN PROJECT](https://github.com/platelminto/parse-torrent-title)

<br>
<br>


<p style="text-align:center;" align="center">
   <a href="https://www.themoviedb.org">
  <img align="center" src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/picx-images-hosting@master/tmdb.6rfszs2oa2k0.svg" height="200"/>
   </a>
</p>

## License

MIT
