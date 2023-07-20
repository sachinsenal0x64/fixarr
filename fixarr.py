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
from rich.console import Console
from rich.text import Text
from tqdm import tqdm
import threading
import platform
import signal
from rich.console import Console
import colorama
from colorama import Fore, Style, Back
import tkinter
import customtkinter as ctk
from PIL import Image
import tkinter.messagebox
import tkinter as tk
from tkinter import simpledialog, filedialog
from ctypes import windll
import ctypes
from dotenv import load_dotenv,find_dotenv
import rich
from langchain.tools import BraveSearch
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate



try:
    windll.shcore.SetProcessDpiAwareness(2)

except:

    pass


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()

load_dotenv(find_dotenv())

tmdb = os.getenv("TMDB_API_KEY")
brave_api = os.getenv("BRAVE_API")
open_ai = os.getenv("OPENAI_API_KEY")


budle_dir = getattr(sys,"_MEIPASS",path.abspath(path.dirname(__file__)))



path_to_app = path.join(budle_dir,'assets','plex.png')


path_to_app_1 = path.join(budle_dir,'assets','i.ico')


path_to_app_2 = path.join(budle_dir,'assets','movie.png')


path_to_app_3 = path.join(budle_dir,'assets','tv.png')


path_to_app_4 = path.join(budle_dir,'assets','delete.png')


path_to_app_5 = path.join(budle_dir,'assets','jellyfin.png')


path_to_app_6 = path.join(budle_dir,'assets','emby.png')


path_to_app_7 = path.join(budle_dir,'assets','logout.png')



app.iconbitmap(path_to_app_1)


if screensize[0] == 3840 and screensize[1] == 2160:
    app.geometry("1500x900")
    ctk.set_widget_scaling(2.0)

elif screensize[0] == 2560 and screensize[1] == 1440:
    app.geometry("1388x800")
    ctk.set_widget_scaling(1.0)


elif screensize[0] == 1920 and screensize[1] == 1080:
    app.geometry("1388x768")


elif screensize[0] == 1600 and screensize[1] == 900:
    app.geometry("1350x580")


elif screensize[0] == 1280 and screensize[1] == 720:
    app.geometry("1230x490")

else:
    app.geometry("800x600")


app.title("FIXARR")

app.resizable(width=False, height=False)



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
    size=(64, 64)
)

image_2 = ctk.CTkImage(
    light_image=Image.open(path_to_app_2),
    dark_image=Image.open(path_to_app_2),
    size=(64, 64),
)

image_3 = ctk.CTkImage(
    light_image=Image.open(path_to_app_3), dark_image=Image.open(path_to_app_3), size=(64, 64)
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
    light_image=Image.open(path_to_app_6), dark_image=Image.open(path_to_app_6), size=(64, 64)
)


image_7 = ctk.CTkImage(
    light_image=Image.open(path_to_app_7),
    dark_image=Image.open(path_to_app_7),
    size=(24, 24),
)




bu = tabview.add("Backup")
mv = tabview.add("Movie/Renamer")
tv = tabview.add("TV/Renamer")
tabview.add("Delete")


out = tabview_2.add("Rename Done")

done = tabview_2.add("Backup Done")

rmf = tabview_2.add("Delete Done")


fe = tabview_2.add("Searcher")



class BrowseDialog(simpledialog.Dialog):
    def body(self, master):
        self.var = tk.StringVar()
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



def del_browse():
    result = filedialog.askdirectory()

    if result:
        deletes(result)

        return result
    return None





def del_fi():
    del_browse()



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

    for root, dirs, files in os.walk(result, topdown=False):
        for file in files:
            for extension in ex:
                if file.endswith(extension):
                    time.sleep(2)

                    label_7 = ctk.CTkLabel(rmf, height=0, width=0)
                    label_7.place(x=0, y=50)

                    label_7.configure(
                        text=f"{os.path.join(root, file)}",
                        font=("Segeo UI", 20),
                        fg_color="#313131",
                        bg_color="#000000",
                        state="normal",
                        text_color="#a68017",
                    )

                    print(f"Deleting file: {os.path.join(root, file)}")
                    os.remove(os.path.join(root, file))
                    TOTAL_FILES_DELETED += 1
                    time.sleep(0.5)
                    break

        label_8 = ctk.CTkLabel(rmf, height=0, width=0)
        label_8.place(x=360, y=662)

        label_8.configure(
            text=f"✅ TOTAL : {TOTAL_FILES_DELETED} FILES DELETED",
            font=("Georgia 90 bold ", 18),
            state="normal",
            text_color="red",
        )

        # for folder in dirs:
        #     if folder.lower() in folders_to_delete:
        #         folder_path = os.path.join(root, folder)
        #         print(f"Deleting folder: {folder_path}")
        #         shutil.rmtree(folder_path)
        #         TOTAL_FOLDERS_DELETED += 1
        #         time.sleep(0.5)


def browse():
    result = filedialog.askdirectory()
    if result:
        file_rename(result)
        if os.path.isfile(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.insert("end", result)
            file_folder_listbox.configure(state="disabled")

        elif os.path.isdir(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.delete("1.0", "end")

            for current_root, dirs, files in os.walk(result):
                for file in files:
                    file_path = os.path.join(current_root, file)
                    file_folder_listbox.insert("end", file_path + "\n")

            file_folder_listbox.configure(state="disabled")

        return result
    return None


def tv_browse():
    result = filedialog.askdirectory()
    if result:
        tv_renamer(result)
        if os.path.isfile(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.insert("end", result)
            file_folder_listbox.configure(state="disabled")
              
        elif os.path.isdir(result):
            file_folder_listbox.configure(state="normal")
            file_folder_listbox.delete("1.0", "end")

            for current_root, dirs, files in os.walk(result):
                for file in files:
                    file_path = os.path.join(current_root, file)
                    file_folder_listbox.insert("end", file_path + "\n")

            file_folder_listbox.configure(state="disabled")

        return result
    return None
    

# Movie Renamer

def file_rename(file_or_folder):
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
                        .replace(".", " ").strip()
                        .replace("_", " ").strip()
                        .replace("-", " ").strip()
                        
                    )

                    print(movie_title)
                    year = year_match.group(2)

                else:
                    # If the year is not present, set it to an empty string
                    year = ""
                    movie_title = base_name.replace(".", " ").replace("_", " ").replace(" - "," ").strip()
                    print(movie_title)

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
                        "$":" "
                    }

                    for old, new in err.items():
                        result = result.replace(old, new)

                    date = data["results"][0]["release_date"][:4]
                    print(result)
                    print(date)

                    # Construct the new file name with the extracted movie title, release year, and original file extension
                    new_name = (
                        f"{result} ({date}){ext}" if year else f"{result} ({date}){ext}"
                    )

                    i = 1

                    old_path = os.path.join(path, name)
                    new_path = os.path.join(path, new_name)
                    mov_progressbar.start()
                    os.rename(old_path, new_path)
                    mov_progressbar.stop()

                    # create files for folders and rename
                    folder_name = f"{result} ({date})" if year else f"{result} ({date})"
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
                        return

                    # delete original file if it exists and is not the same as the destination file
                    if os.path.exists(old_path) and os.path.realpath(old_path) != os.path.realpath(dest_path):
                        os.remove(old_path)

                    # delete original folder if it is now empty
                    if not os.listdir(path):
                        os.rmdir(path)
                    
                    with tqdm(total=i, desc="Renaming : ", unit="Files") as pbar:
                                time.sleep(1)
                                pbar.update(1)
                                mv_p = pbar.n / i * 100
                                pbar.update(0)
                                mv_per = str(int(mv_p))
                                mv_precent.configure(text=mv_per + "%")
                                mv_precent.update()
                                mov_progressbar.set(pbar.n / i )
                                mov_progressbar.update()    
                        

                    TOTAL_FILES_RENAMED += 1


                else:
                    rich.print(f"AI PROCESSING: '{base_name}'")
                    
                    
                    tool = BraveSearch.from_api_key(api_key=brave_api, search_kwargs={"count": 1})
                    
                    res = tool.run(base_name + "movie")
                        
                        
                    question  = f"{res} "
                    
                    if question == []:
                        print("Not Found")
                        
                        
                    else:  
                        rich.print(question)
                    
                        llm = HuggingFaceHub(repo_id="declare-lab/flan-alpaca-large", model_kwargs={"temperature":6, "max_length": 512})
                                

                        prompt_template = PromptTemplate(
                                template = "your task is grab movie name and year using following format -> Name: Value Goes To here else set as None Year: Value Goes To here else set as None get data from {question} ",
                                input_variables=["question"]
                            )
                            
                                
                        chain = LLMChain(llm=llm, prompt=prompt_template)
                            
                        outs = chain.run(question)
                            
                        split_word = outs.split(" ")
                        
                        rich.print(split_word)
                        
                        names = split_word[1].strip()
                        
                        year = split_word[3].strip()
                        
                        rich.print(names)    
                        rich.print(year)
                    
                        #Construct the new file name with the extracted movie title, release year, and original file extension
                        new_name = (
                            f"{names} ({year}){ext}" if year else f"{names} ({year}){ext}"
                        )

                        i = 1

                        old_path = os.path.join(path, name)
                        new_path = os.path.join(path, new_name)
                        mov_progressbar.start()
                        os.rename(old_path, new_path)
                        mov_progressbar.stop()

                        # create files for folders and rename
                        folder_name = f"{names} ({year})" if year else f"{names} ({year})"
                        folder_path = os.path.join(file_or_folder, folder_name)

                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)


                        #move renamed file to folder
                        dest_path = os.path.join(folder_path, new_name)
                        try:
                            shutil.move(new_path, dest_path)
                        except shutil.Error:
                            # failed to move file to folder, restore original filename
                            os.rename(new_path, old_path)
                            return

                        # delete original file if it exists and is not the same as the destination file
                        if os.path.exists(old_path) and os.path.realpath(old_path) != os.path.realpath(dest_path):
                            os.remove(old_path)

                        # delete original folder if it is now empty
                        if not os.listdir(path):
                            os.rmdir(path)
                        
                        with tqdm(total=i, desc="Renaming : ", unit="Files") as pbar:
                                    time.sleep(1)
                                    pbar.update(1)
                                    mv_p = pbar.n / i * 100
                                    pbar.update(0)
                                    mv_per = str(int(mv_p))
                                    mv_precent.configure(text=mv_per + "%")
                                    mv_precent.update()
                                    mov_progressbar.set(pbar.n / i )
                                    mov_progressbar.update()    
                            

                        TOTAL_FILES_RENAMED += 1


    end_time = time.perf_counter()

    total_time = end_time - start_time
    
    console.print(f"Total Files Deleted: {TOTAL_FILES_DELETED}", style="bold red")
    console.print(f"Total Folders Deleted: {TOTAL_FOLDERS_DELETED}", style="bold red")
    console.print(f"Total Files Added: {TOTAL_FILES_ADDED} ", style="bold green")
    console.print(f"Total Files Renamed: {TOTAL_FILES_RENAMED} ", style="bold green")

    console.print(f"Total Time Spent: {total_time:.2f} seconds", style="blue")
    label = ctk.CTkLabel(out, height=0, width=0)
    label.place(x=360, y=662)

    label.configure(
        text=f"✅ TOTAL : {TOTAL_FILES_RENAMED} FILES RENAMED",
        font=("Georgia 90 bold ", 18),
        state="normal",
        text_color="Green",
    )


# TV RENAMER

def tv_renamer(file_or_folder):
    
    start_time = time.perf_counter()

    TOTAL_FILES_DELETED = 0
    TOTAL_FOLDERS_DELETED = 0
    TOTAL_FILES_ADDED = 0
    TOTAL_FILES_RENAMED = 0

    API_KEY = "6001ceb85e9ef2c42ab120589d2ffe68"

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
                    
                pattern = r"^(.+)\.S(\d{0,})E(\d{0,})"
                
                pattern_2 = r"^(\w+)"
                
                epi = r"\b\w+\s+(\w+ \w+)\b"
                
                year_pat = r"(\s[0-9]{3,})" or r"^(.+?)(?=\s?(?:\()?(\d{4})(?:\))?\s?)"
                

                match = re.search(pattern,base_name,re.IGNORECASE)
                
                match_2 = re.search(pattern_2,base_name,re.IGNORECASE)
                
                match_3 = re.search(year_pat,base_name,re.IGNORECASE)
                
                match_4 = re.search(epi,base_name,re.IGNORECASE)
                
                
                if match:
                    names = match.group(1).replace(".", " ").replace("_", " ").replace(" - ","").strip()
                    season = match.group(2)
                    episode = match.group(3)
                    print("Name:", names)
                    print("Season:", season)
                    print("Episode:", episode)    
                    
                
                
                if match_2:
                     names = match_2.group(1).replace(".", " ").replace("_", " ").replace(" - ","").strip() 
                     print("Name:", names)
                                
                
                if match_4:
                    episode = match_4.group(1)
                    print("Episode:", episode)
                
                
                
                if  match_3:
                    year = match_3.group(1) or match_3.group(2)
                    print("Year:", year)
                
                

                query_params = {'api_key': API_KEY, 'query': names, 'include_adult': True, 'with_genres': 0}

                if match_3:
                    query_params['year'] = year
                else:
                    query_params['year'] = None

                url = f"https://api.themoviedb.org/3/search/tv?{urlencode(query_params)}"
                
                
                response = requests.get(url)
                data = response.json()
                rich.print(data)
                    
    
              
                              

      
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
                        precent.configure(text=per + "%")
                        precent.update()
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
        label_2.place(x=360, y=662)

        label_2.configure(
            text=f"✅ Total Backup Added: {TOTAL_BACKUP}",
            font=("Georgia 90 bold ", 18),
            state="normal",
            text_color="Green",
        )

        label_3 = ctk.CTkLabel(done, height=0, width=0)
        label_3.place(x=0, y=50)

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
    fg_color="#313131",
    bg_color="#000000",
    state="disable",
    text_color="#b37c25",
    border_color="#313131",
    corner_radius=3.2,
)
file_folder_listbox.pack()


serc = ctk.CTkTextbox(fe, height=650, width=1500)
serc.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#313131",
    bg_color="#000000",
    state="disable",
    text_color="#b37c25",
    border_color="#313131",
    corner_radius=3.2,
)
serc.pack()


rem = ctk.CTkTextbox(rmf, height=650, width=1500)
rem.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#313131",
    bg_color="#000000",
    state="disable",
    text_color="#b37c25",
    border_color="#313131",
    corner_radius=3.2,
)
rem.pack()


coming = ctk.CTkLabel(fe, text="", height=0, width=0)
coming.place(x=360, y=652)

coming.configure(
    text=f"Seacher In Progress",
    font=("Georgia 90 bold ", 18),
    state="normal",
    text_color="Green",
)


bak_ups = ctk.CTkTextbox(done, height=650, width=1500)
bak_ups.configure(
    wrap="none",
    font=("Segeo UI", 20),
    fg_color="#313131",
    bg_color="#000000",
    state="disable",
    text_color="#b37c25",
    border_color="#313131",
    corner_radius=3.2,
)
bak_ups.pack()


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
    command=start_processing_tv
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


button_6 = ctk.CTkButton(master=app, text="EXIT", command=app.destroy)


button_6.place(
    relx=0.018,
    rely=0.97,
    anchor=ctk.SW,
)

button_6.configure(
    border_width=0,
    border_spacing=5,
    width=45,
    height=10,
    fg_color="#494ae1",
    font=("Georgia", 20),
    hover_color="#913370",
    image=image_7,
    compound="left",
    corner_radius=4,
    border_color="#313131",
    state="normal",
    bg_color="#313131",
)


precent = ctk.CTkLabel(bu, text="0%")
precent.place(relx=0.45, rely=0.20)


# PROGRESS BAR


bak_progressbar = ctk.CTkProgressBar(bu, orientation="horizontal", mode="determinate")
bak_progressbar.configure(progress_color="green")
bak_progressbar.place(relx=0.14, rely=0.25)

bak_progressbar.set(0)

mv_precent = ctk.CTkLabel(mv, text="0%")
mv_precent.place(relx=0.45, rely=0.20)

mov_progressbar = ctk.CTkProgressBar(mv, orientation="horizontal", mode="determinate")
mov_progressbar.configure(progress_color="green")
mov_progressbar.place(relx=0.12, rely=0.25)

mov_progressbar.set(0)


tv_precent = ctk.CTkLabel(tv, text="0%")
tv_precent.place(relx=0.45, rely=0.20)

tv_progressbar = ctk.CTkProgressBar(tv, orientation="horizontal", mode="determinate")
tv_progressbar.configure(progress_color="green")
tv_progressbar.place(relx=0.12, rely=0.25)

tv_progressbar.set(0)




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

    user_home = os.environ["USERPROFILE"]
    src_root = os.path.join(user_home, "AppData", "Local")
    dst_root = os.path.join(user_home, "Documents")

    nff = os.path.join(dst_root, nf)
    if not os.path.exists(nff):
        os.mkdir(nff)

    folder_name = "Plex Media Server"
    stop_flag = False

    app.mainloop()
