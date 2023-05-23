                                                                
<h1 align="center"> FIXARR 🛠️ </h1>

<h4 align="center"> Movie & Tv Renamer With Backup Media Server (Plex / Emby / Jellyfin)</h4>


<p style="text-align:center;" align="center">
  <img align="center" src="https://user-images.githubusercontent.com/127573781/230660856-13721628-6b2c-4f25-bb9d-ea1f9ee82f0d.png" height="40%" width="40%" />
</p>


# FIXARR 🛠️

![Screenshot (231)](https://user-images.githubusercontent.com/127573781/230511871-3b343e7d-42a3-4a4e-9f0d-c52e9cb0470f.png)



For Linux :

```bash
For Ubuntu or other distros with Apt:
sudo apt-get install python3-tk

For Fedora:
sudo dnf install python3-tkinter

pip3 install -r requirements.txt
python3 fixarr.py
```

For macOS :


```terminal
brew install python-tk@3.10
pip3 install -r requirements.txt
python3 fixarr.py

or just run .bat File also you can create bat_shortcut
```


For Windows:


```cmd
pip install -r requirements.txt
python fixarr.py
```



IF YOU WANT TO MAKE STANDALONE (RUN AS EXE) AND MORE FASTER YOU CAN USE NUITKA TO COMPILE CODE INTO C AFTER ITS WILL BUILD YOUR CODE INTO EXE FILE


For Windows :

```compile

[Install C Compiler  (http://www.codeblocks.org/downloads/binaries/) to work with this also setup GCC env path in your os ] 

open your cmd in Fixarr PATH

pip -v install nuitka 

nuitka --mingw64 --standalone --windows-icon-from-ico=./assets/i.ico --include-data-dir=./assets=./assets --onefile --windows-company-name=FIXARR --windows-product-version=0.1.0 --plugin-enable=tk-inter fixarr.py
```

## 🏮 NOTE

# Some Features are Still in Development :)

## License

MIT
