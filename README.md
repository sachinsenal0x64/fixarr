                                                                
<h1 align="center"> 🛠️ FIXARR  </h1>

<h4 align="center"> Movie & Tv Renamer With Backup Media Server (Plex / Emby / Jellyfin)</h4>


<p style="text-align:center;" align="center">
  <img align="center" src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/picx-images-hosting@master/FIXARR LOGO.10it15i3tejk.webp"/>
</p>


# 🛠️ FIXARR 

![Screenshot (231)](https://user-images.githubusercontent.com/127573781/230511871-3b343e7d-42a3-4a4e-9f0d-c52e9cb0470f.png)

<br>


##  🚀 Features

-  🎬 MOVIE RENAMER
-  📺 TV RENAMER (⭕ in progress)
-  🔺 PLEX BACKUP
-  ⚡️ MULTI THREADING 
-  🐟 JELLYFIN BACKUP (⭕ in progress)
-  ❄ EMBY BACKUP (⭕ in progress)
-  ⏬ MOVIE & TV SEACHER (⭕ in progress)

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

For Linux :

```Terminal

For Ubuntu And Other Debian Based Distro With APT:

sudo apt-get install software-properties-common
sudo apt-get install python3.10
sudo apt-get install python3-tk

pip3 install -r requirements.txt
python3 fixarr.py

For Fedora:

sudo dnf install python3
sudo dnf install python3-tkinter

pip3 install -r requirements.txt
python3 fixarr.py

```

For macOS :


```Terminal

For Mac OS With BREW:

if your already not install brew then install its from offical site : https://brew.sh/#install 

brew install python3
brew install python-tk@3.10
pip3 install -r requirements.txt
python3 fixarr.py

or just run .bat File also you can create bat_shortcut
```


For Windows:


```CMD
First Install Python  

pip install -r requirements.txt
python fixarr.py
```



IF YOU WANT TO MAKE OWN STANDALONE EXE USE NUITKA TO COMPILE SOURCE CODE INTO C AFTER ITS CAN RUN AS EXE.  OR  YOU CAN JUST DOWNLOAD PRE BUILD INSTALLER FROM [RELEASES](https://github.com/sachinsenal0x64/FIXARR/releases)


For Windows :

```compile

[Install C Compiler  (http://www.codeblocks.org/downloads/binaries/) and download (including compiler) setup & to work with this setup GCC env path (C:\Program Files\CodeBlocks\MinGW\bin) in your OS SYSTEM ENV ] 

open your cmd in Fixarr PATH

pip -v install nuitka 

nuitka --mingw64 --standalone --windows-icon-from-ico=./assets/i.ico --include-data-dir=./assets=./assets --onefile --windows-company-name=FIXARR --product-name=FIXARR --product-version=0.1.0  --file-version=0.1.0 --plugin-enable=tk-inter fixarr.py

```

## 🏮 NOTE

## 🚀 Some Features are Still in Development :)

## License

MIT
