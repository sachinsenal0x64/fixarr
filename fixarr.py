__author__ = "FIXARR"

__version__ = "0.1.0"


import re
import pathlib
import requests
import json
from os import path
from urllib.parse import urlencode
import os
import shutil
import datetime
import subprocess
import sys
import time
import rich
from rich.console import Console
from rich.text import Text
from tqdm import tqdm
import threading
import platform
import signal
from rich.console import Console
import colorama
from colorama import Fore, Style, Back
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import simpledialog, filedialog
from dotenv import load_dotenv, find_dotenv
import rich
from itertools import islice
import PTN
from thefuzz import fuzz, process


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()

load_dotenv(find_dotenv())

tmdb = os.getenv("TMDB_API_KEY")


budle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))


path_to_app = path.join(budle_dir, "assets", "plex.png")


path_to_app_1 = path.join(budle_dir, "assets", "i.ico")


path_to_app_2 = path.join(budle_dir, "assets", "movie.png")


path_to_app_3 = path.join(budle_dir, "assets", "tv.png")


path_to_app_4 = path.join(budle_dir, "assets", "delete.png")


path_to_app_5 = path.join(budle_dir, "assets", "jellyfin.png")


path_to_app_6 = path.join(budle_dir, "assets", "emby.png")


path_to_app_7 = path.join(budle_dir, "assets", "logout.png")


WIDTH, HEIGHT = app.winfo_screenwidth(), app.winfo_screenheight()


if platform.system() == "Windows":
    if WIDTH == 3840 and HEIGHT == 2160:
        app.geometry("1500x900")
        ctk.set_widget_scaling(2.0)

    elif WIDTH == 2560 and HEIGHT == 1440:
        app.geometry("1388x800")
        ctk.set_widget_scaling(1.0)

    elif WIDTH == 1920 and HEIGHT == 1080:
        app.geometry("1388x768")

    elif WIDTH == 1600 and HEIGHT == 900:
        app.geometry("1350x580")

    elif WIDTH == 1280 and HEIGHT == 720:
        app.geometry("1230x490")

    else:
        app.geometry("1000x600")

    app.iconbitmap(path_to_app_1)


if platform.system() == "Linux":
    if WIDTH == 3840 and HEIGHT == 2160:
        app.geometry("1500x900")
        ctk.set_widget_scaling(2.0)

    elif WIDTH == 2560 and HEIGHT == 1440:
        app.geometry("1388x800")
        ctk.set_widget_scaling(1.0)

    elif WIDTH == 1920 and HEIGHT == 1080:
        app.geometry("1388x768")

    elif WIDTH == 1600 and HEIGHT == 900:
        app.geometry("1350x580")

    elif WIDTH == 1280 and HEIGHT == 720:
        app.geometry("1230x490")

    else:
        app.geometry("1000x600")

    log = Image.open(path_to_app_1)
    logo = ImageTk.PhotoImage(log)

    app.tk.call("wm", "iconphoto", app._w, logo)


app.title("FIXARR")

app.resizable(width=True, height=True)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


__date__ = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
win_version = platform.win32_ver()[0]
platform = platform.system() + " " + win_version


tabview = ctk.CTkTabview(app)
tabview_2 = ctk.CTkTabview(app)

tabview.pack(fill="both", side="left", expand=True, padx=20, pady=20)
tabview.configure()


tabview_2.pack(fill="both", side="right", expand=True, padx=20, pady=20)

tabview.columnconfigure(0, weight=1)
tabview.rowconfigure(3, weight=1)

tabview_2.columnconfigure(0, weight=1)
tabview_2.rowconfigure(3, weight=1)


image = ctk.CTkImage(
    light_image=Image.open(path_to_app),
    dark_image=Image.open(path_to_app),
    size=(64, 64),
)

image_2 = ctk.CTkImage(
    light_image=Image.open(path_to_app_2),
    dark_image=Image.open(path_to_app_2),
    size=(64, 64),
)

image_3 = ctk.CTkImage(
    light_image=Image.open(path_to_app_3),
    dark_image=Image.open(path_to_app_3),
    size=(64, 64),
)


image_4 = ctk.CTkImage(
    light_image=Image.open(path_to_app_4),
    dark_image=Image.open(path_to_app_4),
    size=(64, 64),
)


image_5 = ctk.CTkImage(
    light_image=Image.open(path_to_app_5),
    dark_image=Image.open(path_to_app_5),
    size=(64, 64),
)


image_6 = ctk.CTkImage(
    light_image=Image.open(path_to_app_6),
    dark_image=Image.open(path_to_app_6),
    size=(64, 64),
)


image_7 = ctk.CTkImage(
    light_image=Image.open(path_to_app_7),
    dark_image=Image.open(path_to_app_7),
    size=(24, 24),
)


bu = tabview.add("Backup")
mv = tabview.add("Movie/Renamer")
tv = tabview.add("TV/Renamer")
de = tabview.add("Delete")


out = tabview_2.add("Rename Done")

done = tabview_2.add("Backup Done")

rmf = tabview_2.add("Delete Done")

fe = tabview_2.add("Searcher")


class BrowseDialog(simpledialog.Dialog):
    def body(self, master):
        self.var = ctk.StringVar()
        self.var.set("Folder")

        choices = ["Folder"]
        combobox = ctk.CTkOptionMenu(master, values=choices, variable=self.var)
        combobox.pack(padx=20, pady=10)

    def apply(self):
        choice = self.var.get()
        if choice == "File":
            self.result = filedialog.askopenfilename()
        elif choice == "Folder":
            self.result = filedialog.askdirectory()
        else:
            self.result = None


def remove_empty_directories(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
                print(f"Deleted directory: {dir_path}")
            except OSError as e:
                print(f"Error deleting directory: {dir_path}, {e}")
                continue


label_8 = ctk.CTkLabel(rmf, height=0, width=0)
label = ctk.CTkLabel(out, height=0, width=0)


def del_fi():
    result = filedialog.askdirectory()
    label_8.pack_forget()
    if result:
        if os.path.isfile(result):
            rem.configure(state="normal")
            rem.insert("end", result)
            rem.configure(state="disabled")

        elif os.path.isdir(result):
            for current_root, dirs, files in os.walk(result):
                for file in files:
                    file_path = os.path.join(current_root, file)
                    rem.configure(state="normal")
                    # rem.delete("1.0", "end")
                    rem.insert("end", file_path + "\n")
                    rem.configure(state="disabled")

        deletes(result)

        return result
    return None


def deletes(result):
    TOTAL_FILES_DELETED = 0

    ex = [
        ".txt",
        ".csv",
        ".xlsx",
        ".xls",
        ".pptx",
        ".ppt",
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".pdf",
        ".doc",
        ".exe",
        ".srt",
        ".xml",
        ".rtf",
        ".nfo",
        ".src",
    ]

    #   folders_to_delete = [
    #         folder.lower()
    #         for folder in input(
    #             "Enter the name of the folders to delete, separated by commas: "
    #         ).split(",")
    #     ]

    for path, dirs, files in os.walk(result, topdown=False):
        for name in files:
            rename_path = pathlib.PurePath(path, name)
            print(rename_path)

            num_files = sum(
                [len(files) for path, dirs, files in os.walk(result, topdown=False)]
            )

            t = num_files

            for extension in ex:
                if name.endswith(extension):
                    if not name.endswith(tuple(extension)):
                        continue
                    else:
                        print(f"Deleting file: {os.path.join(path, name)}")
                        os.remove(os.path.join(path, name))
                        TOTAL_FILES_DELETED += 1

        for current_root, dirs, files in os.walk(result, topdown=False):
            for file in files:
                rem.configure(state="normal")
                file_path = os.path.join(current_root, file)
                # rem.delete("1.0", "end")
                rem.insert("end", file_path + "\n")
                rem.configure(state="disabled")

        label_8.configure(
            text=f"✅ TOTAL : {TOTAL_FILES_DELETED} FILES DELETED",
            font=("Segeo UI", 18),
            state="normal",
            text_color="#bf214b",
        )
        label_8.pack()

        # for folder in dirs:
        #     if folder.lower() in folders_to_delete:
        #         folder_path = os.path.join(root, folder)
        #         print(f"Deleting folder: {folder_path}")
        #         shutil.rmtree(folder_path)
        #         TOTAL_FOLDERS_DELETED += 1
        #         time.sleep(0.5)


def browse():
    result = filedialog.askdirectory()
    label.pack_forget()
    if result:
        if os.path.isfile(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.insert("end", result)
            file_folder_listbox.configure(state="disabled")

        elif os.path.isdir(result):
            for current_root, dirs, files in os.walk(result):
                for file in files:
                    file_path = os.path.join(current_root, file)
                    file_folder_listbox.configure(state="normal")
                    # file_folder_listbox.delete("1.0", "end")
                    file_folder_listbox.insert("end", file_path + "\n")
                    file_folder_listbox.configure(state="disabled")

        movie_rename(result)
        return result
    return None


def tv_browse():
    result = filedialog.askdirectory()
    if result:
        if os.path.isfile(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.insert("end", result)
            file_folder_listbox.configure(state="disabled")

        elif os.path.isdir(result):
            for current_root, dirs, files in os.walk(result):
                for file in files:
                    file_path = os.path.join(current_root, file)
                    file_folder_listbox.configure(state="normal")
                    # file_folder_listbox.delete("1.0", "end")
                    file_folder_listbox.insert("end", file_path + "\n")
                    file_folder_listbox.configure(state="disabled")

        tv_renamer(result)
        return result

    return None


# Movie Renamer


def movie_rename(file_or_folder):
    start_time = time.perf_counter()

    TOTAL_FILES_DELETED = 0
    TOTAL_FOLDERS_DELETED = 0
    TOTAL_FILES_ADDED = 0
    TOTAL_FILES_RENAMED = 0

    API_KEY = tmdb

    ext = [
        ".webm",
        ".mkv",
        ".flv",
        ".vob",
        ".ogv",
        ".ogg",
        ".rrc",
        ".gifv",
        ".mng",
        ".mov",
        ".avi",
        ".qt",
        ".wmv",
        ".yuv",
        ".rm",
        ".asf",
        ".amv",
        ".mp4",
        ".m4p",
        ".m4v",
        ".mpg",
        ".mp2",
        ".mpeg",
        ".mpe",
        ".mpv",
        ".m4v",
        ".svi",
        ".3gp",
        ".3g2",
        ".mxf",
        ".roq",
        ".nsv",
        ".flv",
        ".f4v",
        ".f4p",
        ".f4a",
        ".f4b",
        ".mod",
    ]

    for path, dirs, files in os.walk(file_or_folder):
        for name in files:
            rename_path = pathlib.PurePath(path, name)
            print(rename_path)

            num_files = sum(
                [len(files) for path, dirs, files in os.walk(file_or_folder)]
            )

            t = num_files

            # if ext not in name then dont do anything else rename
            if not name.endswith(tuple(ext)):
                continue

            else:
                # Extract the file name and extension from the file path
                base_name, ext = os.path.splitext(name)

                # Extract the year from the movie file name (assuming it is in the format 'Movie Title (YYYY)')
                year_match = re.search(
                    r"^(.+?)(?=\s?(?:\()?(\d{4})(?:\))?\s?)", base_name, re.IGNORECASE
                )

                if year_match:
                    # Extract the movie title and year from the file name
                    movie_title = (
                        year_match.group(1)
                        .split("- ")[-1]
                        .split("= ")[-1]
                        .split(" – ")[-1]
                        .replace(".", " ")
                        .strip()
                        .replace("_", " ")
                        .strip()
                        .replace("-", " ")
                        .strip()
                    )

                    print(movie_title)

                    year = year_match.group(2)

                    rich.print(year)

                else:
                    # If the year is not present, set it to an empty string
                    year = ""
                    movie_title = (
                        base_name.replace(".", " ")
                        .replace("_", " ")
                        .replace(" - ", " ")
                        .replace(" = ", " ")
                        .strip()
                    )
                    rich.print(movie_title)

                # Add the year parameter to the movie db API URL
                url = f"https://api.themoviedb.org/3/search/movie?{urlencode({'api_key':API_KEY,'query':movie_title,'year':year,'include_adult':True,'with_genres':0})}"

                response = requests.get(url)
                print(json.dumps(response.json(), indent=4))
                data = response.json()

                if data["results"]:
                    # Use the first search result as the movie title
                    result = data["results"][0]["title"]

                    err = {
                        ":": " ",
                        "/": " ",
                        "\\": " ",
                        "*": " ",
                        "?": " ",
                        '"': " ",
                        "<": " ",
                        ">": " ",
                        "|": " ",
                        ".": " ",
                        "$": " ",
                    }

                    for old, new in err.items():
                        result = result.replace(old, new)

                    date = data["results"][0]["release_date"][:4]
                    print(result)
                    print(date)

                    # Construct the new file name with the extracted movie title, release year, and original file extension
                    new_name = f"{result} ({date}){ext}" if year else f"{result}{ext}"

                    i = 1

                    old_path = os.path.join(path, name)
                    new_path = os.path.join(path, new_name)
                    mov_progressbar.start()
                    os.rename(old_path, new_path)
                    mov_progressbar.stop()

                    # create files for folders and rename
                    folder_name = f"{result} ({date})" if year else f"{result}"
                    folder_path = os.path.join(file_or_folder, folder_name)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    # move renamed file to folder
                    dest_path = os.path.join(folder_path, new_name)

                    try:
                        shutil.move(new_path, dest_path)
                    except shutil.Error:
                        # failed to move file to folder, restore original filename
                        os.rename(new_path, old_path)

                    with tqdm(total=i, desc="Renaming : ", unit="Files") as pbar:
                        time.sleep(1)
                        pbar.update(1)
                        mv_p = pbar.n / i * 100
                        pbar.update(0)
                        mv_per = str(int(mv_p))
                        mv_precent.configure(text=mv_per + "%")
                        mv_precent.update()
                        mov_progressbar.set(pbar.n / i)
                        mov_progressbar.update()

                    TOTAL_FILES_RENAMED += 1

                    remove_empty_directories(file_or_folder)

                else:
                    pass

    for current_root, dirs, files in os.walk(file_or_folder, topdown=False):
        for file in files:
            file_folder_listbox.configure(state="normal")
            file_path = os.path.join(current_root, file)
            # rem.delete("1.0", "end")
            file_folder_listbox.insert("end", file_path + "\n")
            file_folder_listbox.configure(state="disabled")

        end_time = time.perf_counter()

        total_time = end_time - start_time

        console.print(f"Total Files Deleted: {TOTAL_FILES_DELETED}", style="bold red")
        console.print(
            f"Total Folders Deleted: {TOTAL_FOLDERS_DELETED}", style="bold red"
        )
        console.print(f"Total Files Added: {TOTAL_FILES_ADDED} ", style="bold green")
        console.print(
            f"Total Files Renamed: {TOTAL_FILES_RENAMED} ", style="bold green"
        )
        console.print(f"Total Time Spent: {total_time:.2f} seconds", style="blue")

        label.pack()

        label.configure(
            text=f"✅ TOTAL : {TOTAL_FILES_RENAMED} FILES RENAMED",
            font=("Segeo UI", 18),
            state="normal",
            text_color="Green",
        )


# TV RENAMER


def tv_renamer(file_or_folder):
    count = []

    start_time = time.perf_counter()

    TOTAL_FILES_DELETED = 0
    TOTAL_FOLDERS_DELETED = 0
    TOTAL_FILES_ADDED = 0
    TOTAL_FILES_RENAMED = 0

    ext = [
        ".webm",
        ".mkv",
        ".flv",
        ".vob",
        ".ogv",
        ".ogg",
        ".rrc",
        ".gifv",
        ".mng",
        ".mov",
        ".avi",
        ".qt",
        ".wmv",
        ".yuv",
        ".rm",
        ".asf",
        ".amv",
        ".mp4",
        ".m4p",
        ".m4v",
        ".mpg",
        ".mp2",
        ".mpeg",
        ".mpe",
        ".mpv",
        ".m4v",
        ".svi",
        ".3gp",
        ".3g2",
        ".mxf",
        ".roq",
        ".nsv",
        ".flv",
        ".f4v",
        ".f4p",
        ".f4a",
        ".f4b",
        ".mod",
    ]

    for path, dirs, files in os.walk(file_or_folder):
        for name in files:
            rename_path = pathlib.PurePath(path, name)
            print(rename_path)

            num_files = sum(
                [len(files) for path, dirs, files in os.walk(file_or_folder)]
            )

            len_file = num_files

            dib = dirs

            print(dib)

            # if ext not in name then dont do anything else rename
            if not name.endswith(tuple(ext)):
                continue

            else:
                # Extract the file name and extension from the file path
                base_name, ext = os.path.splitext(name)

                title = None
                year = None

                max_similarity_ratio = 0
                episode_name = None

                match_3 = PTN.parse(base_name, standardise=False, coherent_types=True)

                if "title" in match_3:
                    title = match_3["title"]
                    rich.print("Title:", title)

                if "season" in match_3:
                    season = match_3.get("season", [])[0]
                    rich.print("Season:", season)

                if "episodeName" in match_3:
                    episode = match_3.get("episodeName", [])
                    rich.print("episodeName:", episode)

                if "year" in match_3:
                    data = match_3
                    year = data.get("year", [])[0]
                    rich.print("Year:", year)

                if "episode" in match_3:
                    episode = match_3.get("episode", [])[0]
                    rich.print("Episode:", episode)

                if "documentary" in match_3:
                    documentary = match_3.get("documentary", [])
                    rich.print("Documentary:", documentary)

                if IndexError:
                    pattern = r"^(\w+)\s(.+)$"
                    match = re.search(pattern, base_name)

                    if match:
                        title = match.group(1)
                        episode = match.group(2)
                        print("Name:", name)
                        print("Title:", title)

                query_params = {
                    "api_key": tmdb,
                    "query": title,
                    "year": year,
                    "include_adult": True,
                    "with_genres": 0,
                }

                url = (
                    f"https://api.themoviedb.org/3/search/tv?{urlencode(query_params)}"
                )

                response = requests.get(url)

                data = response.json()

                rich.print(data)

                try:
                    t_name = data["results"][0]["name"]
                    t_date = data["results"][0]["first_air_date"]

                    t_date = t_date[:4]

                    count.append(t_name)
                except:
                    pass

                # Check if any TV show matches the search query
                if data.get("results"):
                    # Get the ID of the first TV show in the search results (you can handle multiple results as needed)
                    tv_show_id = data["results"][0]["id"]

                    # Now, use the TV show ID to fetch information about its seasons
                    season_url = f"https://api.themoviedb.org/3/tv/{tv_show_id}?api_key={tmdb}"

                    season_response = requests.get(season_url)
                    season_data = season_response.json()

                    # Print information about seasons and episodes
                    rich.print("Seasons:")
                    for season in season_data["seasons"]:
                        rich.print(
                            f"Season {season['season_number']}: {season['name']}"
                        )

                        # Now, fetch information about episodes for each season
                        episode_url = f"https://api.themoviedb.org/3/tv/{tv_show_id}/season/{season['season_number']}?api_key={tmdb}"
                        episode_response = requests.get(episode_url)
                        episode_data = episode_response.json()
                        rich.print("Episodes:")

                        for episode_i in episode_data["episodes"]:
                            episode_number = episode_i["episode_number"]
                            ep_n = episode_i["name"]
                            print(episode_number)

                            # Calculate similarity_ratio using fuzzywuzzy
                            similarity_ratio = fuzz.ratio(
                                str(episode), str(episode_number)
                            )

                            if similarity_ratio > max_similarity_ratio:
                                max_similarity_ratio = similarity_ratio
                                episode_name = ep_n
                                episode = episode_number

                            print(
                                "Similarity Ratio:",
                                similarity_ratio,
                                "BASE_NAME:",
                                base_name,
                                "API_ONE:",
                                episode_name,
                            )

                            new_file_name = f"{t_name} - S{season['season_number']:02d}E{episode:02d} - {episode_name}{ext}"
                            rich.print(new_file_name)

                        tv_folder = f"{t_name} ({t_date})"
                        season_folder = f"Season {season['season_number']:02d}"

                        folder_path = os.path.join(file_or_folder, tv_folder)
                        season_path = os.path.join(folder_path, season_folder)

                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)

                        if not os.path.exists(season_path):
                            os.makedirs(season_path)

                        i = 1

                        # Get the old file path
                        old_file_path = os.path.join(path, name)

                        # Create the new file path
                        new_file_path = os.path.join(season_path, new_file_name)

                        tv_progressbar.start()

                        # Rename the file
                        try:
                            if not t_name in count:
                                os.rename(old_file_path, new_file_path)

                        except OSError as e:
                            print(f"An error occurred while renaming the file: {e}")
                            continue

                        tv_progressbar.stop()

                        with tqdm(total=i, desc="Renaming : ", unit="Files") as pbar:
                            time.sleep(1)
                            pbar.update(1)
                            tv_p = pbar.n / i * 100
                            pbar.update()
                            tv_per = str(int(tv_p))
                            tv_precent.configure(text=tv_per + "%")
                            tv_precent.update()
                            tv_progressbar.set(pbar.n / i)
                            tv_progressbar.update()

                        TOTAL_FILES_RENAMED += 1

                        remove_empty_directories(file_or_folder)

                if t_name in count:
                    print("Already Proccesing")
                    continue

                if FileExistsError:
                    continue

    end_time = time.perf_counter()

    for current_root, dirs, files in os.walk(file_or_folder, topdown=False):
        for file in files:
            file_folder_listbox.configure(state="normal")
            file_path = os.path.join(current_root, file)
            # rem.delete("1.0", "end")
            file_folder_listbox.insert("end", file_path + "\n")
            file_folder_listbox.configure(state="disabled")

        end_time = time.perf_counter()

        total_time = end_time - start_time

        console.print(f"Total Files Deleted: {TOTAL_FILES_DELETED}", style="bold red")
        console.print(
            f"Total Folders Deleted: {TOTAL_FOLDERS_DELETED}", style="bold red"
        )
        console.print(f"Total Files Added: {TOTAL_FILES_ADDED} ", style="bold green")
        console.print(
            f"Total Files Renamed: {TOTAL_FILES_RENAMED} ", style="bold green"
        )
        console.print(f"Total Time Spent: {total_time:.2f} seconds", style="blue")

        label.pack()

        label.configure(
            text=f"✅ TOTAL : {TOTAL_FILES_RENAMED} FILES RENAMED",
            font=("Segeo UI", 18),
            state="normal",
            text_color="Green",
        )


def backup():
    start = time.perf_counter()
    TOTAL_BACKUP = 0

    # Find and backup the source folder
    try:
        for root, dirs, files in os.walk(src_root):
            if folder_name in dirs:
                src_folder = os.path.join(root, folder_name)

                now = datetime.datetime.now()
                timestamp_str = now.strftime("%Y-%m-%d_%I-%M-%S_%p")

                backup_name = f"{folder_name}-backup_{timestamp_str}"

                # Create the backup folder & backing up the source folder
                root_path = os.path.join(dst_root, backup_name)
                os.mkdir(root_path)
                update_path = os.path.join(root_path, folder_name)

                text = Text(f"Backup to: {update_path} \n")
                text.stylize("bold green", 0, 11)
                text.stylize("#ff00af", 11, 13)
                text.stylize("yellow3", 13, 120)

                console.print("Backing up Plex Media Server... \n", style="bold green")
                console.print(text)

                # Count the number of files and directories to be copied
                num_files = sum(
                    [len(files) for root, dirs, files in os.walk(src_folder)]
                )
                # num_dirs = sum([len(dirs) for root, dirs, files in os.walk(src_folder)])
                total_files = num_files
                # TOTAL_BACKUP += 1

                with tqdm(total=total_files, desc="Backing up ", unit="File") as pbar:

                    def copy_function(src, dst):
                        if stop_flag:
                            return
                        if os.path.isdir(src):
                            shutil.copytree(src, dst)
                        else:
                            shutil.copy2(src, dst)

                        pbar.update(1)
                        bak_ = pbar.n / total_files * 100
                        per = str(int(bak_))
                        bak_precent.configure(text=per + "%")
                        bak_precent.update()
                        bak_progressbar.set(pbar.n / total_files)

                    shutil.copytree(
                        src_folder,
                        update_path,
                        dirs_exist_ok=True,
                        copy_function=copy_function,
                    )

                # Export the registry key to a backup file

                console.print("\nExporting Plex registry key... \n", style="bold green")

                now = datetime.datetime.now()
                timestamp_str = now.strftime("%Y-%m-%d_%I-%M-%S_%p")
                backup_name = f"plex-registry-backup_{timestamp_str}.reg"
                update_name = f"plex-registry-backup_{timestamp_str}"
                reg_path = r"HKEY_CURRENT_USER\Software\Plex, Inc."

                backup_path = os.path.join(dst_root, update_name)
                os.mkdir(backup_path)

                backup_files = os.path.join(backup_path, backup_name)

                file = Text(f"Backup to: {backup_files} \n")
                file.stylize("bold green", 0, 10)
                file.stylize("#ff00af", 10, 13)
                file.stylize("yellow3", 13, 129)

                console.print(file)

                subprocess.call(
                    ["REG", "EXPORT", reg_path, backup_files],
                    stdout=subprocess.DEVNULL,
                )

                shutil.move(backup_path, root_path)

                end_file = shutil.move(root_path, nff)

                end = time.perf_counter()
                TOTAL_BACKUP += 1
                break

        console.print(f"Time taken: {end - start:.2f} seconds \n", style="bright_cyan")
        console.print("Process Completed ! \n", style="#87ff00")
        console.print(f"Total Backup Added: {TOTAL_BACKUP} ", style="bold green")

        label_2 = ctk.CTkLabel(done, text="", height=0, width=0)
        label_2.pack()

        label_2.configure(
            text=f"✅ Total Backup Added: {TOTAL_BACKUP}",
            font=("Segeo UI", 18),
            state="normal",
            text_color="Green",
        )

        label_3 = ctk.CTkLabel(done, height=0, width=0)
        label_3.pack()

        label_3.configure(
            text=f"{end_file}",
            font=("Segeo UI", 20),
            fg_color="#313131",
            bg_color="#000000",
            state="normal",
            text_color="#a68017",
        )

    except KeyboardInterrupt:
        time.sleep(1)
        console.print("Exiting...! \n", style="bold red")
        sys.exit(1)


def signal_handler(x, y):
    console.print("\nExiting... \n", style="bold red")
    os._exit(0)


signal.signal(signal.SIGINT, signal_handler)


class ProcessingThread(threading.Thread):
    def __init__(self, target_function):
        super().__init__()
        self.target_function = target_function
        self.running = False

    def run(self):
        self.running = True
        self.target_function()

    def stop(self):
        self.running = False

    def restart(self, target_function):
        self.target_function = target_function
        self.stop()
        self.start()


processing_thread = None


def start_processing():
    global processing_thread

    # check if a thread is already running
    if processing_thread and processing_thread.running:
        # if so, stop the thread
        processing_thread.stop()

    # start a new thread for processing
    processing_thread = ProcessingThread(target_function=browse)
    processing_thread.start()


def start_processing_tv():
    global processing_thread

    # check if a thread is already running
    if processing_thread and processing_thread.running:
        # if so, stop the thread
        processing_thread.stop()

    # start a new thread for processing
    processing_thread = ProcessingThread(target_function=tv_browse)
    processing_thread.start()


def start_del():
    global processing_thread
    # check if a thread is already running
    if processing_thread and processing_thread.running:
        # if so, stop the thread
        processing_thread.stop()

    # start a new thread for processing
    processing_thread = ProcessingThread(target_function=del_fi)
    processing_thread.start()


def bak_u():
    global processing_thread

    # check if a thread is already running
    if processing_thread and processing_thread.running:
        # if so, stop the thread
        processing_thread.stop()

    # start a new thread for processing
    processing_thread = ProcessingThread(target_function=backup)
    processing_thread.start()


# TEXT BOX


file_folder_listbox = ctk.CTkTextbox(out, height=650, width=1500)
file_folder_listbox.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#212121",
    bg_color="#212121",
    state="disable",
    text_color="#b37c25",
    border_color="#212121",
    corner_radius=3.2,
)
file_folder_listbox.pack(fill=ctk.BOTH, expand=True)


serc = ctk.CTkTextbox(fe, height=650, width=1500)
serc.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#212121",
    bg_color="#212121",
    state="disable",
    text_color="#b37c25",
    border_color="#212121",
    corner_radius=3.2,
)
serc.pack(fill=ctk.BOTH, expand=True)


serc = ctk.CTkLabel(fe, height=0, width=0)
serc.pack()

serc.configure(
    text=f"🛠 IN PROGRESS",
    font=("Segeo UI", 18),
    state="normal",
    text_color="#d4af2a",
)


rem = ctk.CTkTextbox(rmf, height=650, width=1500)
rem.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#212121",
    bg_color="#212121",
    state="disable",
    text_color="#b37c25",
    border_color="#212121",
    corner_radius=3.2,
)
rem.pack(fill=ctk.BOTH, expand=True)


bak_ups = ctk.CTkTextbox(done, height=650, width=1500)
bak_ups.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#212121",
    bg_color="#212121",
    state="disable",
    text_color="#b37c25",
    border_color="#212121",
    corner_radius=3.2,
)
bak_ups.pack(fill=ctk.BOTH, expand=True)


button_2 = ctk.CTkButton(
    tabview.tab("Movie/Renamer"),
    text="MOVIE | TMDB",
    image=image_2,
    compound="left",
    font=("Segeo UI", 20),
    command=start_processing,
)


button_2.pack(side="left", padx=20, pady=20, expand=True)
button_2.grid(row=1, column=0, padx=25, pady=55, sticky="nsew")


button_3 = ctk.CTkButton(
    tabview.tab("TV/Renamer"),
    text="TV |  TMDB ",
    image=image_3,
    compound="left",
    font=("Segeo UI", 20),
    command=start_processing_tv,
)

button_3.pack(side="left", padx=20, pady=20, expand=True)
button_3.grid(row=1, column=0, padx=25, pady=55, ipadx=15, sticky="nsew")


button_4 = ctk.CTkButton(
    tabview.tab("Delete"),
    text="DELETE | FILES",
    image=image_4,
    compound="left",
    font=("Segeo UI", 20),
    command=start_del,
)


button_4.pack(side="left", padx=20, pady=20, expand=True)
button_4.grid(row=1, column=0, padx=25, pady=55, sticky="nsew")


button_1 = ctk.CTkButton(
    tabview.tab("Backup"),
    text="PLEX | BACKUP",
    image=image,
    compound="left",
    font=("Segoe UI", 20),
    command=bak_u,
)


button_1.grid(row=1, column=0, padx=20, pady=55, sticky="nsew")


button_5 = ctk.CTkButton(
    tabview.tab("Backup"),
    text="JELLYFIN | BACKUP",
    image=image_5,
    compound="left",
    font=("Segoe UI", 20),
)


button_5.grid(row=2, column=0, padx=20, pady=55, sticky="nsew")


button_7 = ctk.CTkButton(
    tabview.tab("Backup"),
    text="EMBY | BACKUP",
    image=image_6,
    compound="left",
    font=("Segoe UI", 20),
)


button_7.grid(row=3, column=0, padx=20, pady=55, sticky="nsew")


# PROGRESS BAR


bak_precent = ctk.CTkLabel(bu, text="0%")
bak_precent.place(x=140, y=140)

bak_progressbar = ctk.CTkProgressBar(bu, orientation="horizontal", mode="determinate")
bak_progressbar.configure(progress_color="green")
bak_progressbar.place(x=40, y=170)

bak_progressbar.set(0)

mv_precent = ctk.CTkLabel(mv, text="0%")
mv_precent.place(x=140, y=140)

mov_progressbar = ctk.CTkProgressBar(mv, orientation="horizontal", mode="determinate")
mov_progressbar.configure(progress_color="green")
mov_progressbar.place(x=40, y=170)

mov_progressbar.set(0)


tv_precent = ctk.CTkLabel(tv, text="0%")
tv_precent.place(x=140, y=140)

tv_progressbar = ctk.CTkProgressBar(tv, orientation="horizontal", mode="determinate")
tv_progressbar.configure(progress_color="green")
tv_progressbar.place(x=40, y=170)

tv_progressbar.set(0)


del_precent = ctk.CTkLabel(de, text="0%")
del_precent.place(x=140, y=140)


del_progressbar = ctk.CTkProgressBar(de, orientation="horizontal", mode="determinate")
del_progressbar.configure(progress_color="green")
del_progressbar.place(x=40, y=170)

del_progressbar.set(0)


if __name__ == "__main__":
    colorama.init()
    console = Console()
    ver = Text("\nVersion: 0.1.0")
    ver.stylize("bold yellow", 0, 8)
    ver.stylize("yellow", 8, 15)
    console.print("\nFIXARR", style="green_yellow")
    console.print(ver)
    console.print(f"\nDate: {__date__}", style="bright_cyan")
    console.print(f"OS: {platform} \n", style="bright_cyan")

    YELLOW = "\x1b[1;33;40m"
    RED = "\x1b[1;31;40m"

    nf = "PLEX BACKUPS"

    if platform == "Windows":
        user_home = os.environ["USERPROFILE"]
        src_root = os.path.join(user_home, "AppData", "Local")
        dst_root = os.path.join(user_home, "Documents")

        nff = os.path.join(dst_root, nf)
        if not os.path.exists(nff):
            os.mkdir(nff)

    elif platform == "Linux":
        pass

    elif platform == "Darwin":
        pass

    folder_name = "Plex Media Server"
    stop_flag = False

    app.mainloop()
