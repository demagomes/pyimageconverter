from pathlib import Path
import tkinter as tk
from tkinter import END, filedialog, scrolledtext, ttk
from tkinter import messagebox
from ttkbootstrap import Style
from classes.converter import Converter
from classes.errorlogwindow import ErrorLogWindow
from classes.utils import Utils
from classes.extenions import Extensions


#TODO - Refactor the GUI functions so some granular test can be added in the form of unittests



class Window(tk.Tk):
    '''Application Main Window class using tkinter and ttkbootstrap

    Args:
        tk: Toplevel widget of Tk which represents mostly the main window of an application. It has an associated Tcl interpreter
    '''
    sourcefiles = []
    errors = []

    def __init__(self):
        super().__init__()
        self.labelfontsize = 14
        self.entryfontsize = 14
        self.geometry("820x725")
        self.resizable(False, False)
        self.title('Python Image Converter')
        self.iconbitmap('icon.ico')
        self.style = Style(theme='journal')

         # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # set the converter and util instances
        self.converter = Converter()
        self.utils = Utils()
        self.extensions = Extensions()

        # file extension options
        self.extoptions = ['JPEG','PNG','WEBP']
       

        self.resize = tk.IntVar(value=100)


        self.create_widgets()

    def create_widgets(self):
        '''Call function to create and display the window's elements
        '''
        self.widget_sourcefolder()
        self.widget_targetfolder()
        self.widget_imageresizing()
        self.widget_progressbar()
        self.widget_buttons()

    def widget_buttons(self):
        # Error Logs
        errors_button = ttk.Button(self, text="Errors",command=self.command_errorslog)
        errors_button.grid(column=0, row=7, sticky=tk.W,padx=10, pady=5, ipady=20, ipadx=20)
        # Convert
        convert_button = ttk.Button(self, text="Convert",command=self.command_convert)
        convert_button.grid(column=1, row=7, sticky=tk.E,padx=10, pady=5, ipady=20, ipadx=20)

    def command_errorslog(self):
        '''Calls Error Logs Window
        '''
        ErrorLogWindow(self.errors)

    def widget_sourcefolder(self):
        # frame
        sourcefolder_label_widget = ttk.Label(self, text="Source Folder", font=(None, self.entryfontsize))
        sourcefolder_labelframe = ttk.LabelFrame(self, labelwidget=sourcefolder_label_widget)
        sourcefolder_labelframe.grid(column=0, row=1, sticky=tk.EW, padx=10)
        sourcefolder_labelframe.columnconfigure(0, weight=20)
        sourcefolder_labelframe.columnconfigure(1, weight=1)
        
        # File type combobox
        self.sourcefiletype_combo = ttk.Combobox(sourcefolder_labelframe,values=self.extoptions,state='readonly')
        self.sourcefiletype_combo.current(0)
        self.sourcefiletype_combo.grid(column=0,row=1,columnspan=2,sticky=tk.EW, padx=(10,10), pady=(5,0))
        self.sourcefiletype_combo.bind('<<ComboboxSelected>>',self.command_sourcetypecombochange)

        # Path entry
        self.sourcefolder_entry = ttk.Entry(sourcefolder_labelframe,font=(None, self.entryfontsize),state='disabled')
        self.sourcefolder_entry.grid(column=0, row=2, sticky=tk.EW, padx=(10,0), pady=(5,0))

        # select folder button
        self.sourcefolder_button = ttk.Button(sourcefolder_labelframe, text="...",command=self.command_sourcefolderdialog)
        self.sourcefolder_button.grid(column=1,row=2,padx=(0,10),pady=(5,0),ipady=2)

        # Source Folder Content ScrolledText 
        self.sourcefilestextbox = scrolledtext.ScrolledText(master=sourcefolder_labelframe,highlightthickness=1)
        self.sourcefilestextbox.grid(column=0, row=5, columnspan=2,sticky=tk.EW, padx=(10,0), pady=(5,5))
        default_txt = "Source Folder Content"
        self.sourcefilestextbox.insert(END, default_txt)

    def widget_targetfolder(self):
        # frame
        targetfolder_label_widget = ttk.Label(self, text="Target Folder", font=(None, self.entryfontsize))
        targetfolder_labelframe = ttk.LabelFrame(self, labelwidget=targetfolder_label_widget)
        targetfolder_labelframe.grid(column=1, row=1, sticky=tk.EW, padx=10)
        targetfolder_labelframe.columnconfigure(0, weight=20)
        targetfolder_labelframe.columnconfigure(1, weight=1)

        # File type combobox
        self.targetfiletype_combo = ttk.Combobox(targetfolder_labelframe,values=self.extoptions,state='readonly')
        self.targetfiletype_combo.current(2)
        self.targetfiletype_combo.grid(column=0,columnspan=2,row=1,sticky=tk.EW, padx=(10,10), pady=(5,0))
        self.targetfiletype_combo.bind('<<ComboboxSelected>>',self.command_targettypecombochange)

        # Path entry
        self.targetfolder_entry = ttk.Entry(targetfolder_labelframe,font=(None, self.entryfontsize),state='disabled')
        self.targetfolder_entry.grid(column=0, row=2, sticky=tk.EW, padx=(10,0), pady=(5,0))

        # select folder button        
        self.targetfolder_button = ttk.Button(targetfolder_labelframe, text="...",command=self.command_targetfolderdialog)
        self.targetfolder_button.grid(column=1,row=2,padx=(0,10),pady=(5,0),ipady=2)
    
        # Target Folder Content ScrolledText 
        self.targetfilestextbox = scrolledtext.ScrolledText(
            master=targetfolder_labelframe,
            highlightthickness=1
        )
        self.targetfilestextbox.grid(column=0, row=4, columnspan=2,sticky=tk.EW, padx=(10,0), pady=(5,5))
        default_txt = "Target Folder Content"
        self.targetfilestextbox.insert(END, default_txt)
        
    def command_sourcefolderdialog(self):
        d = filedialog.askdirectory(parent=self)
        if d:
            self.sourcefolder_entry.config(state='enabled')
            self.sourcefolder_entry.delete(0, END)
            self.sourcefolder_entry.insert(0,d)
            self.sourcefolder_entry.config(state='disabled')

            # get list of images from folder
            self.subcommand_updatesourcefolder()
    
    def command_targetfolderdialog(self):
        d = filedialog.askdirectory(parent=self)
        if d:
            self.targetfolder_entry.config(state='enabled')
            self.targetfolder_entry.delete(0, tk.END)
            self.targetfolder_entry.insert(0,d)
            self.targetfolder_entry.config(state='disabled')

            # updates target foldere images list
            self.subcommand_updatetargetfolder()

    def widget_progressbar(self):
        '''Creates and display the progress bar that is updated by command_convert function
        '''
        # Status frame
        status_label_widget = ttk.Label(self, text="Status:", font=(None, self.entryfontsize))
        status_labelframe = ttk.LabelFrame(self, labelwidget=status_label_widget)
        status_labelframe.grid(column=0, row=6, columnspan=2,sticky=tk.EW, padx=10, pady=(0, 5))
        status_labelframe.columnconfigure(1, weight=1)

        self.pb = ttk.Progressbar(
            status_labelframe,
            orient='horizontal',
            value=0
        )
        self.pb.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=(5, 10))

    def command_convert(self):
        '''Converts the files form source to target folder based on file types selected.
        it also saves the error logs.
        '''

        # flow control var 
        continueflow = True

        # Validate entries and AppInfo Project Location
        if self.sourcefolder_entry.get() == '':
            self.validationbox('Please select the Source Folder')
            continueflow = False
        
        if self.targetfolder_entry.get() == '' and continueflow:
            self.validationbox('Please select the Target Folder')
            continueflow = False

        if len(self.sourcefiles) == 0 and continueflow:
            self.validationbox('Source folder doesn\'t have any Image of specified type')
            continueflow = False


        if continueflow:
            
            self.pb['maximum'] = len(self.sourcefiles)
            self.pb['value'] = 0
            self.pb.update()

            for i,image in enumerate(self.sourcefiles):
                    imagepath = self.sourcefolder_entry.get() + '/' + image
                    newext = self.extoptions[self.targetfiletype_combo.current()]
                    name = self.targetfolder_entry.get() + '/' + Path(image).stem+self.extensions.setextension(newext)
                    log = self.converter.convert(imagepath,name,int(self.resize.get()))
                    if log != '':
                        self.errors.append(log)
                    self.pb['value'] = i+1
                    self.pb.update()
                    self.subcommand_updatetargetfolder()
            
            messagebox.showinfo(title='Processes Finished', message='Process Finished with ' + str(len(self.errors)) + ' Errors')
            
    def validationbox(self, message):
        '''Show validation messagebox

        Args:
            message (str): message to be displayed in the messagebox
        '''
        messagebox.showerror(title='Validation Error', message=message,)

    def subcommand_updatetargetfolder(self):
        d = self.targetfolder_entry.get()
        lookupext = self.extensions.getextensions(self.extoptions[self.targetfiletype_combo.current()])
        targetfiles = self.utils.listdirectory(lookupext,d)
        self.targetfilestextbox.delete('1.0', END)
        for f in targetfiles:
            self.targetfilestextbox.insert(END,f+'\n')
    
    def subcommand_updatesourcefolder(self):
        d = self.sourcefolder_entry.get()
        lookupext = self.extensions.getextensions(self.extoptions[self.sourcefiletype_combo.current()])
        self.sourcefiles = self.utils.listdirectory(lookupext,d)
        self.sourcefilestextbox.delete('1.0', END)
        for f in self.sourcefiles:
            self.sourcefilestextbox.insert(END,f+'\n')

    def command_sourcetypecombochange(self,event):
        if self.sourcefolder_entry.get() != '':
            self.subcommand_updatesourcefolder()
    
    def command_targettypecombochange(self,event):
        if self.targetfolder_entry.get() != '':
            self.subcommand_updatetargetfolder()

    def widget_imageresizing(self):
        '''Creates and display the the resizing options
        '''
        # Status frame
        resizing_label_widget = ttk.Label(
            self, text="Resizing Options (100% doesn\'t resize the image, the other options do):", font=(None, self.entryfontsize))
        resizing_labelframe = ttk.LabelFrame(
            self, labelwidget=resizing_label_widget)
        resizing_labelframe.grid(column=0, row=5, columnspan=2,sticky=tk.EW, padx=10, pady=(5, 5))
        resizing_labelframe.columnconfigure(0, weight=1)
        resizing_labelframe.columnconfigure(1, weight=1)
        resizing_labelframe.columnconfigure(2, weight=1)
        resizing_labelframe.columnconfigure(3, weight=1)

        # Size Combobox
        self.targetfilesize_25 = ttk.Radiobutton(resizing_labelframe,value=25,text='25%',style='Toolbutton',variable=self.resize)
        self.targetfilesize_50 = ttk.Radiobutton(resizing_labelframe,value=50,text='50%',style='Toolbutton',variable=self.resize)
        self.targetfilesize_75 = ttk.Radiobutton(resizing_labelframe,value=75,text='75%',style='Toolbutton',variable=self.resize)
        self.targetfilesize_100 = ttk.Radiobutton(resizing_labelframe,value=100,text='100%',style='Toolbutton',variable=self.resize)
        self.targetfilesize_25.grid(column=0, row=1,sticky=tk.EW, padx=(5,0), pady=(5,10))
        self.targetfilesize_50.grid(column=1, row=1,sticky=tk.EW, padx=(1,0), pady=(5,10))
        self.targetfilesize_75.grid(column=2, row=1,sticky=tk.EW, padx=(1,0), pady=(5,10))
        self.targetfilesize_100.grid(column=3, row=1,sticky=tk.EW, padx=(1,5), pady=(5,10))

