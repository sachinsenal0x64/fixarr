# FIXARR
Movie &amp; Tv Renamer With Backup Media Server (Plex / Emby / Jellyfin)

![Screenshot (231)](https://user-images.githubusercontent.com/127573781/230511871-3b343e7d-42a3-4a4e-9f0d-c52e9cb0470f.png)




For Linux and macOS:

```bash
pip3 install -r requirements.txt
python3 fixarr.py
```


For windows:

```cmd
pip install -r requirements.txt
python fixarr.py
```


IF YOU WANT TO MAKE RUN AS STANDALONE EXE AND MORE FASTER YOU CAN USE NUITKA TO COMPILE CODE INTO C LANG

```compile

[Install C Compiler and Clang Cli to work with this also setup clang env in your os ]

pip install Nuitka
nuitka --mingw64 --standalone --windows-icon-from-ico=./assets/i.ico --include-data-dir=./assets=./assets --onefile --windows-company-name=FIXARR --windows-product-version=1.0.0 --plugin-enable=tk-inter --windows-disable-console fixarr.py
```




## License

MIT
