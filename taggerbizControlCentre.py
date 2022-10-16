# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
import os
from tkinter import filedialog as fd, DISABLED
from tkinter import messagebox
from tkinter import simpledialog
import time


class ConfigurateTaggerBiz(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid
        # self.window = tk.Tk()
        # self.window.title("TAGGER.biz control centre")
        # self.window.rowconfigure(0, minsize=400, weight=1)
        # self.window.columnconfigure(1, minsize=10, weight=1)
        self.filepath = "./taggerbizexportconfig.txt"
        self.filearray = ["", "", "", "", "", "", "", ""]
        self.ii = 0
        self.directory_01_txt = ""
        self.directory_02_txt = ""
        self.directory_03_txt = ""
        self.directory_04_txt = ""
        self.directory_05_txt = ""
        self.directory_06_txt = ""
        self.taggerbiz_email_txt = ""
        self.taggerbiz_drive_txt = ""
        self.read_directories()

        def open_directory(mydir, mytitle):
            """Open a file for editing."""

            dirpath = fd.askdirectory(initialdir=mydir, title=mytitle, parent=None)
            print(dirpath)

            if not dirpath:
                return
            return dirpath

        def exportClicked():
            print("Export clicked")
            mydir = open_directory(self.filearray[0], "export jpg directory")
            btn_export_jpg_txt_var.set(mydir)
            self.directory_01_txt = mydir
            save_file(self)

        def exportTextClicked():
            print("Export clicked")
            mydir = "this is the directory where you exported your images as jpgfiles in Lightroom.  Send this directory to TAGGERB.biz"
            tk.messagebox.showinfo("export directory", mydir)

            # btn_export_jpg_txt_var.set(mydir)
            # self.export_jpg_txt = mydir

        def lightroomClicked():
            print("Lightroom clicked")
            mydir = open_directory(self.filearray[1], "YOUR Lightroom directory")
            btn_lightroom_dir_txt_var.set(mydir)
            self.directory_02_txt = mydir
            save_file(self)

        def lightroomTextClicked():
            print("Lightroom clicked")
            mydir = "this is the directory where you original Lightroom files are. Your MASTER directory!"
            tk.messagebox.showinfo("Lightroom directory", mydir)

        def lightroomExportClicked():
            print("Lightroom export clicked")
            mydir = open_directory(self.filearray[2], "EXPORT Lightroom directory")
            btn_lightroom_export_dir_txt_var.set(mydir)
            self.directory_03_txt = mydir
            save_file(self)

        def lightroomExportTextClicked():
            print("Lightroom extract clicked")
            mydir = "this directory will be filled with copies of images from your Lightroom directory. Send this directory to TAGGERB.biz"
            tk.messagebox.showinfo("Lightroom extract directory", mydir)

        def lightroomDuplicatesClicked():
            print("Lightroom duplicates clicked")
            mydir = open_directory(self.filearray[3], "DUPLICATES Lightroom directory")
            btn_lightroom_duplicates_dir_txt_var.set(mydir)
            self.directory_04_txt = mydir
            save_file(self)

        def lightroomDuplicatesTextClicked():
            print("Lightroom export clicked")
            mydir = "this is the directory that will be filled with images that can't be processed, because these are duplicates. You can have a look at them and try to eliminate the duplicate images"
            tk.messagebox.showinfo("Lightroom duplicates directory", mydir)

        def taggerBizExportClicked():
            print("taggerBiz Export clicked")
            mydir = open_directory(self.filearray[4], "TAGGER.biz export directory")
            btn_taggerbiz_export_dir_txt_var.set(mydir)
            self.directory_05_txt = mydir
            save_file(self)

        def taggerBizExportTextClicked():
            print("taggerBizExport clicked")
            mydir = "this is the directory for the export to TAGGER.biz"
            tk.messagebox.showinfo("TAGGER.biz export directory", mydir)

        def taggerBizImportClicked():
            print("taggerBiz Import clicked")
            mydir = open_directory(self.filearray[5], "TAGGER.biz import directory")
            btn_taggerbiz_import_dir_txt_var.set(mydir)
            self.directory_06_txt = mydir
            save_file(self)

        def taggerBizImportTextClicked():
            print("taggerBizImport clicked")
            mydir = "this is the directory for the import from TAGGER.biz"
            tk.messagebox.showinfo("TAGGER.biz import directory", mydir)

        def taggerBizEmailClicked():
            print("taggerBiz Email clicked")
            myEmail = tk.simpledialog.askstring(title="please enter your email address",
                                                prompt="please enter your email address")
            btn_taggerbiz_email_txt_var.set(myEmail)
            self.taggerbiz_email_txt = myEmail
            save_file(self)

        def taggerBizEmailTextClicked():
            print("taggerBizEmail clicked")
            mydir = "the email address is required for preparing the TAGGER.biz package "
            tk.messagebox.showinfo("Email address", mydir)

        def taggerBizDriveClicked():
            print("taggerBizDrive clicked")
            myDrive = tk.simpledialog.askstring(title="please enter the Drive for TAGGER.biz",
                                                prompt="please enter the Drive for TAGGER.biz")
            btn_taggerbiz_drive_txt_var.set(myDrive)
            self.taggerbiz_drive_txt = myDrive
            self.directory_01_txt = myDrive + "/TAGGER.biz.package/JgpExport"
            self.directory_03_txt = myDrive + "/TAGGER.biz.package/LightroomExtract"
            self.directory_04_txt = myDrive + "/TAGGER.biz.package/LightroomDuplicates"
            self.directory_05_txt = myDrive + "/TAGGER.biz.package/export"
            self.directory_06_txt = myDrive + "/TAGGER.biz.package/import"
            try:
               os.makedirs(self.directory_01_txt, exist_ok=True, mode=0o777)
            except OSError as error:
                myMessage = "Directory '%s' can not be created" % self.directory_01_txt
                tk.messagebox.showinfo("INFO",message=myMessage)
            try:
               os.makedirs(self.directory_03_txt, exist_ok=True, mode=0o777)
            except OSError as error:
                myMessage = "Directory '%s' can not be created" % self.directory_03_txt
                tk.messagebox.showinfo("INFO",message=myMessage)
            try:
               os.makedirs(self.directory_04_txt, exist_ok=True, mode=0o777)
            except OSError as error:
                myMessage = "Directory '%s' can not be created" % self.directory_04_txt
                tk.messagebox.showinfo("INFO",message=myMessage)
            try:
               os.makedirs(self.directory_05_txt, exist_ok=True, mode=0o777)
            except OSError as error:
                myMessage = "Directory '%s' can not be created" % self.directory_05_txt
                tk.messagebox.showinfo("INFO",message=myMessage)
            try:
               os.makedirs(self.directory_06_txt, exist_ok=True, mode=0o777)
            except OSError as error:
                myMessage = "Directory '%s' can not be created" % self.directory_06_txt
                tk.messagebox.showinfo("INFO",message=myMessage)
            save_file(self)
            self.read_directories()
            btn_export_jpg_txt_var.set(self.filearray[0])
            btn_lightroom_dir_txt_var.set(self.filearray[1])
            btn_lightroom_export_dir_txt_var.set(self.filearray[2])
            btn_lightroom_duplicates_dir_txt_var.set(self.filearray[3])
            btn_taggerbiz_export_dir_txt_var.set(self.filearray[4])
            btn_taggerbiz_import_dir_txt_var.set(self.filearray[5])
            btn_taggerbiz_email_txt_var.set(self.filearray[6])
            btn_taggerbiz_drive_txt_var.set(self.filearray[7])

        def taggerBizDriveTextClicked():
            print("taggerBizDriveText clicked")
            mydir = "the drive is required for preparing the TAGGER.biz directories "
            tk.messagebox.showinfo("Drive", mydir)

        def startPrepareClicked():
            import os
            filepath = "./taggerbizruntimeconfig.txt"
            ii = 0
            scriptpath = ""

            with open(filepath, "r") as input_file:
                for x in input_file:
                    ii = ii + 1
                    if (ii == 1):
                        scriptpath = str(x).strip("\n")
                input_file.close()

            os.system(scriptpath)
            stream = os.popen(scriptpath)
            output = stream.read()
            print(output)
            print("done")

        def startImportClicked():
            import os
            filepath = "./taggerbizruntimeconfig.txt"
            ii = 0
            scriptpath = ""

            with open(filepath, "r") as input_file:
                for x in input_file:
                    ii = ii + 1
                    if (ii == 2):
                        scriptpath = str(x).strip("\n")
                input_file.close()

            os.system(scriptpath)
            stream = os.popen(scriptpath)
            output = stream.read()
            print(output)
            print("done")

        def startTaggerbizscriptTxtclicked():
            print("TAGGER.biz script clicked")
            mydir = "By clicking on the GREEN button left you start the TAGGER.biz script to prepare your delivery " + \
                    "package."
            tk.messagebox.showinfo("TAGGER.biz script", mydir)

        def startTaggerbizscriptImportTxtclicked():
            print("TAGGER.biz Import script clicked")
            mydir = "By clicking on the YELLOW button left you start the TAGGER.biz script to import your received " + \
                    "package."
            tk.messagebox.showinfo("TAGGER.biz script", mydir)

        def save_file(self):
            """Save the current file as a new file."""

            # filepath = fd.asksaveasfilename(
            #    defaultextension="txt",
            #    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            # )
            filepath = "./taggerbizexportconfig.txt"
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                output_file.write(self.directory_01_txt + "\n")
                output_file.write(self.directory_02_txt + "\n")
                output_file.write(self.directory_03_txt + "\n")
                output_file.write(self.directory_04_txt + "\n")
                output_file.write(self.directory_05_txt + "\n")
                output_file.write(self.directory_06_txt + "\n")
                output_file.write(self.taggerbiz_email_txt + "\n")
                output_file.write(self.taggerbiz_drive_txt + "\n")
            output_file.close()

        self.fr_buttons = tk.Frame(master, relief=tk.RAISED, bd=2)
        self.btn_export_jpg = tk.Button(self.fr_buttons, text="export jpg directory",
                                        command=exportClicked, bg="lightgreen",
                                        highlightbackground="lightgreen",
                                        fg="black",
                                        state=DISABLED)
        btn_export_jpg_txt_var = tk.StringVar()
        self.btn_export_jpg_txt = tk.Button(self.fr_buttons, textvariable=btn_export_jpg_txt_var,
                                            command=exportTextClicked)
        btn_export_jpg_txt_var.set(self.filearray[0])

        self.btn_lightroom_dir = tk.Button(self.fr_buttons, text="YOUR Lightroom directory",
                                           command=lightroomClicked, highlightbackground="cyan", bg="cyan")
        btn_lightroom_dir_txt_var = tk.StringVar()
        self.btn_lightroom_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_lightroom_dir_txt_var,
                                               command=lightroomTextClicked)
        btn_lightroom_dir_txt_var.set(self.filearray[1])

        self.btn_lightroom_export_dir = tk.Button(self.fr_buttons, text="EXTRACT Lightroom directory",
                                                  command=lightroomExportClicked,
                                                  highlightbackground="lightgreen",
                                                  bg="lightgreen",
                                                  state=DISABLED)
        btn_lightroom_export_dir_txt_var = tk.StringVar()
        self.btn_lightroom_export_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_lightroom_export_dir_txt_var,
                                                      command=lightroomExportTextClicked)
        btn_lightroom_export_dir_txt_var.set(self.filearray[2])

        self.btn_lightroom_duplicates_dir = tk.Button(self.fr_buttons, text="Lightroom duplicates",
                                                      command=lightroomDuplicatesClicked,
                                                      highlightbackground="lightgreen",
                                                      bg="lightgreen",
                                                      state=DISABLED)
        btn_lightroom_duplicates_dir_txt_var = tk.StringVar()
        self.btn_lightroom_duplicates_dir_txt = tk.Button(self.fr_buttons,
                                                          textvariable=btn_lightroom_duplicates_dir_txt_var,
                                                          command=lightroomDuplicatesTextClicked)
        btn_lightroom_duplicates_dir_txt_var.set(self.filearray[3])

        self.btn_taggerbiz_export_dir = tk.Button(self.fr_buttons, text="TAGGER.biz export",
                                                  command=taggerBizExportClicked,
                                                  bg="lightgreen",
                                                  highlightbackground="lightgreen",
                                                  state=DISABLED)
        btn_taggerbiz_export_dir_txt_var = tk.StringVar()
        self.btn_taggerbiz_export_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_taggerbiz_export_dir_txt_var,
                                                      command=taggerBizExportTextClicked)
        btn_taggerbiz_export_dir_txt_var.set(self.filearray[4])

        self.btn_taggerbiz_import_dir = tk.Button(self.fr_buttons, text="TAGGER.biz import",
                                                  command=taggerBizImportClicked,
                                                  bg="lightgreen", highlightbackground="lightgreen",
                                                  state=DISABLED)
        btn_taggerbiz_import_dir_txt_var = tk.StringVar()
        self.btn_taggerbiz_import_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_taggerbiz_import_dir_txt_var,
                                                      command=taggerBizImportTextClicked)
        btn_taggerbiz_import_dir_txt_var.set(self.filearray[5])

        self.btn_taggerbiz_email = tk.Button(self.fr_buttons, text="TAGGER.biz email",
                                             command=taggerBizEmailClicked,
                                             bg="green", highlightbackground="green")
        btn_taggerbiz_email_txt_var = tk.StringVar()
        self.btn_taggerbiz_email_txt = tk.Button(self.fr_buttons, textvariable=btn_taggerbiz_email_txt_var,
                                                 command=taggerBizEmailTextClicked)
        btn_taggerbiz_email_txt_var.set(self.filearray[6])

        self.btn_taggerbiz_email = tk.Button(self.fr_buttons, text="TAGGER.biz email",
                                             command=taggerBizEmailClicked,
                                             bg="green", highlightbackground="green")
        btn_taggerbiz_drive_txt_var = tk.StringVar()
        self.btn_taggerbiz_drive_txt = tk.Button(self.fr_buttons, textvariable=btn_taggerbiz_drive_txt_var,
                                                 command=taggerBizDriveTextClicked)
        btn_taggerbiz_drive_txt_var.set(self.filearray[7])
        self.btn_taggerbiz_drive = tk.Button(self.fr_buttons, text="TAGGER.biz Drive",
                                             command=taggerBizDriveClicked,
                                             bg="green", highlightbackground="green")

        self.btn_start_taggerbizscript = tk.Button(self.fr_buttons, text="start EXPORT script",
                                                   command=startPrepareClicked,
                                                   bg="green", highlightbackground="green")
        btn_start_taggerbizscript_txt_var = tk.StringVar()
        self.btn_start_taggerbizscript_txt = tk.Button(self.fr_buttons,
                                                       textvariable=btn_start_taggerbizscript_txt_var,
                                                       command=startTaggerbizscriptTxtclicked)
        btn_start_taggerbizscript_txt_var.set("help");
        self.btn_start_taggerbiz_import_script = tk.Button(self.fr_buttons, text="start IMPORT script",
                                                           command=startImportClicked,
                                                           bg="yellow", highlightbackground="yellow")
        btn_start_taggerbizscript_import_txt_var = tk.StringVar()
        self.btn_start_taggerbizscript_import_txt = tk.Button(self.fr_buttons,
                                                              textvariable=btn_start_taggerbizscript_import_txt_var,
                                                              command=startTaggerbizscriptImportTxtclicked)

        btn_start_taggerbizscript_import_txt_var.set("help");
        self.btn_export_jpg.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.btn_export_jpg_txt.grid(row=4, column=1, sticky="ew", padx=5)
        self.btn_lightroom_dir.grid(row=2, column=0, sticky="ew", padx=5)
        self.btn_lightroom_dir_txt.grid(row=2, column=1, sticky="ew", padx=5)
        self.btn_lightroom_export_dir.grid(row=5, column=0, sticky="ew", padx=5)
        self.btn_lightroom_export_dir_txt.grid(row=5, column=1, sticky="ew", padx=5)
        self.btn_lightroom_duplicates_dir.grid(row=3, column=0, sticky="ew", padx=5)
        self.btn_lightroom_duplicates_dir_txt.grid(row=3, column=1, sticky="ew", padx=5)
        self.btn_taggerbiz_export_dir.grid(row=6, column=0, sticky="ew", padx=5)
        self.btn_taggerbiz_export_dir_txt.grid(row=6, column=1, sticky="ew", padx=5)
        self.btn_taggerbiz_import_dir.grid(row=7, column=0, sticky="ew", padx=5)
        self.btn_taggerbiz_import_dir_txt.grid(row=7, column=1, sticky="ew", padx=5)
        self.btn_start_taggerbizscript.grid(row=8, column=0, sticky="ew", padx=5)
        self.btn_start_taggerbizscript_txt.grid(row=8, column=1, sticky="ew", padx=5)
        self.btn_start_taggerbiz_import_script.grid(row=9, column=0, sticky="ew", padx=5)
        self.btn_start_taggerbizscript_import_txt.grid(row=9, column=1, sticky="ew", padx=5)
        self.btn_taggerbiz_email.grid(row=0, column=0, sticky="ew", padx=5)
        self.btn_taggerbiz_email_txt.grid(row=0, column=1, sticky="ew", padx=5)
        self.btn_taggerbiz_drive.grid(row=1, column=0, sticky="ew", padx=5)
        self.btn_taggerbiz_drive_txt.grid(row=1, column=1, sticky="ew", padx=5)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

    def read_directories(self):
        with open(self.filepath, "r") as input_file:
            ii = 0
            for x in input_file:
                self.filearray[ii] = str(x).strip("\n")
                ii = ii + 1
                if (ii == 1):
                    self.directory_01_txt = str(x).strip("\n")
                elif (ii == 2):
                    self.directory_02_txt = str(x).strip("\n")
                elif (ii == 3):
                    self.directory_03_txt = str(x).strip("\n")
                elif (ii == 4):
                    self.directory_04_txt = str(x).strip("\n")
                elif (ii == 5):
                    self.directory_05_txt = str(x).strip("\n")
                elif (ii == 6):
                    self.directory_06_txt = str(x).strip("\n")
                elif (ii == 7):
                    self.taggerbiz_email_txt = str(x).strip("\n")
                elif (ii == 8):
                    self.taggerbiz_drive_txt = str(x).strip("\n")
        input_file.close()


if __name__ == '__main__':
    # https://stackoverflow.com/questions/33637292/change-tkinter-frame-title/33637380
    root = tk.Tk()
    root.wm_title("TAGGER.biz control centre")
    myConf = ConfigurateTaggerBiz(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
