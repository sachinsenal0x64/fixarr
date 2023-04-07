                                                                
<h1 align="center"> FIXARR 🎬 </h1>

<h2 align="center"> Movie & Tv Renamer With Backup Media Server (Plex / Emby / Jellyfin) 🎬 </h2>



![Jackiza_triangle_rainbow_color_dark_mode_backgreound_classic_lo_447774d7-7360-4e9f-b9d0-7cf5c0b60ed3](https://user-images.githubusercontent.com/127573781/230596627-3c2407f6-2421-45ba-8588-e7613bc5d147.png)



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
```

For Windows:

```cmd
pip install -r requirements.txt
python fixarr.py
```


IF YOU WANT TO MAKE STANDALONE AND RUN AS EXE AND MORE FASTER YOU CAN USE NUITKA TO COMPILE CODE INTO C

```compile

[Install C Compiler and Clang Cli to work with this also setup clang env in your os ]

pip install Nuitka
nuitka --mingw64 --standalone --windows-icon-from-ico=./assets/i.ico --include-data-dir=./assets=./assets --onefile --windows-company-name=FIXARR --windows-product-version=1.0.0 --plugin-enable=tk-inter --windows-disable-console fixarr.py
```


# Some Features are Still in Development :)

## License

MIT
