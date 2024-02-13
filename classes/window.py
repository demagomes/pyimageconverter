from pathlib import Path
import tkinter as tk
from tkinter import END, filedialog, scrolledtext, ttk
from ttkbootstrap import Style
from classes.converter import Converter
from classes.utils import Utils
from classes.extenions import Extensions

#DONE - Update files when combo changes and there is a path set
#TODO - fix the ... buttons padding
#TODO - Organise this class better, breackdown the functions further where possible and reuse code
#DONE - Convert the files and update the target files
#TODO - learn how to unit test GUI if possible
#TODO - make the path entries disabled for typing
#TODO - dialogbox when finished with errors / or errors panel on may screen
#TODO - convert button validation if all variables are set for it to work or dialogbox

class Window(tk.Tk):
    sourcefiles = []

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


        self.create_widgets()

    def create_widgets(self):
        # Source and Target Folder panels
        self.widget_sourcefolder()
        self.widget_targetfolder()
        self.widget_progressbar()
        self.widget_buttons()

    def widget_buttons(self):
        # Convert
        convert_button = ttk.Button(self, text="Convert",command=self.command_convert)
        convert_button.grid(column=1, row=7, sticky=tk.E,padx=10, pady=5, ipady=20, ipadx=20)

    def widget_sourcefolder(self):
        # frame
        sourcefolder_label_widget = ttk.Label(self, text="Source Folder", font=(None, self.entryfontsize))
        sourcefolder_labelframe = ttk.LabelFrame(self, labelwidget=sourcefolder_label_widget)
        sourcefolder_labelframe.grid(column=0, row=1, sticky=tk.EW, padx=10, pady=(20, 10))
        sourcefolder_labelframe.columnconfigure(0, weight=20)
        sourcefolder_labelframe.columnconfigure(1, weight=1)
        
        # File type combobox
        self.sourcefiletype_combo = ttk.Combobox(sourcefolder_labelframe,values=self.extoptions)
        self.sourcefiletype_combo.current(0)
        self.sourcefiletype_combo.grid(column=0,row=1,columnspan=2,sticky=tk.EW, padx=(10,10), pady=(5,10))
        

        # Path entry
        self.sourcefolder_entry = ttk.Entry(sourcefolder_labelframe,font=(None, self.entryfontsize),state='disabled')
        self.sourcefolder_entry.grid(column=0, row=2, sticky=tk.EW, padx=(10,0), pady=(5,10))
        self.sourcefolder_button = ttk.Button(sourcefolder_labelframe, text="...",command=self.command_sourcefolderdialog)
        self.sourcefolder_button.grid(column=1,row=2,padx=0,pady=(5,10),ipady=2)

        # Source Folder Content ScrolledText 
        self.sourcefilestextbox = scrolledtext.ScrolledText(
            master=sourcefolder_labelframe,
            highlightthickness=1

        )
        self.sourcefilestextbox.grid(column=0, row=5, columnspan=2,sticky=tk.EW, padx=(10,0), pady=(5,10))
        default_txt = "Source Folder Content"
        self.sourcefilestextbox.insert(END, default_txt)

    def widget_targetfolder(self):
        # frame
        targetfolder_label_widget = ttk.Label(self, text="Target Folder", font=(None, self.entryfontsize))
        targetfolder_labelframe = ttk.LabelFrame(self, labelwidget=targetfolder_label_widget)
        targetfolder_labelframe.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=(20, 10))
        targetfolder_labelframe.columnconfigure(0, weight=20)
        targetfolder_labelframe.columnconfigure(1, weight=1)

        # File type combobox
        self.targetfiletype_combo = ttk.Combobox(targetfolder_labelframe,values=self.extoptions)
        self.targetfiletype_combo.current(2)
        self.targetfiletype_combo.grid(column=0,row=1,columnspan=2,sticky=tk.EW, padx=(10,10), pady=(5,10))

        self.targetfolder_entry = ttk.Entry(targetfolder_labelframe,font=(None, self.entryfontsize),state='disabled')
        self.targetfolder_entry.grid(column=0, row=2, sticky=tk.EW, padx=(10,0), pady=(5,10))
        self.targetfolder_button = ttk.Button(targetfolder_labelframe, text="...",command=self.command_targetfolderdialog)
        self.targetfolder_button.grid(column=1,row=2,padx=0,pady=(5,10),ipady=2)
    
        # Target Folder Content ScrolledText 
        self.targetfilestextbox = scrolledtext.ScrolledText(
            master=targetfolder_labelframe,
            highlightthickness=1
        )
        self.targetfilestextbox.grid(column=0, row=5, columnspan=2,sticky=tk.EW, padx=(10,0), pady=(5,10))
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
            lookupext = self.extensions.getextensions(self.extoptions[self.sourcefiletype_combo.current()])
            self.sourcefiles = self.utils.listdirectory(lookupext,d)

            self.sourcefilestextbox.delete('1.0', END) #REVIEW - WHy does it need 1.0 when the entry needs just 0, need to understand this parameters.
            for f in self.sourcefiles:
                self.sourcefilestextbox.insert(END,f+'\n')
    
    def command_targetfolderdialog(self):
        d = filedialog.askdirectory(parent=self)
        if d:
            self.targetfolder_entry.config(state='enabled')
            self.targetfolder_entry.delete(0, tk.END)
            self.targetfolder_entry.insert(0,d)
            self.targetfolder_entry.config(state='disabled')

            # get list of images from folder
            lookupext = self.extensions.getextensions(self.extoptions[self.targetfiletype_combo.current()])
            targetfiles = self.utils.listdirectory(lookupext,d)
            self.targetfilestextbox.delete('1.0', END) #REVIEW - WHy does it need 1.0 when the entry needs just 0, need to understand this parameters.
            for f in targetfiles:
                self.targetfilestextbox.insert(END,f+'\n')

    def widget_progressbar(self):
        # Status frame
        status_label_widget = ttk.Label(
            self, text="Status:", font=(None, self.entryfontsize))
        status_labelframe = ttk.LabelFrame(
            self, labelwidget=status_label_widget)
        status_labelframe.grid(column=0, row=6, columnspan=2,
                               sticky=tk.EW, padx=10, pady=(20, 10))
        status_labelframe.columnconfigure(1, weight=1)
        # status_labelframe.columnconfigure(2, weight=30)

        self.pb = ttk.Progressbar(
            status_labelframe,
            orient='horizontal',
            # mode='indeterminate',
            value=0
        )
        self.pb.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=(5, 10))

    def command_convert(self):
        errors = []
        self.pb['maximum'] = len(self.sourcefiles)
        self.pb['value'] = 0
        self.pb.update()

        for i,image in enumerate(self.sourcefiles):
                imagepath = self.sourcefolder_entry.get() + '/' + image
                newext = self.extoptions[self.targetfiletype_combo.current()]
                name = self.targetfolder_entry.get() + '/' + Path(image).stem+self.extensions.setextension(newext)
                errors.append(self.converter.convert(imagepath,name))
                self.pb['value'] = i+1
                self.pb.update()
        
        if errors != []:
            self.utils.cprint('Errors:','ERROR')
            for e in errors:
                if e != '':
                    print(e)

        #FIXME - This sessions needs to be better coded into functions as it appears 3 times in this class
        # get list of images from folder
        d = self.targetfolder_entry.get()
        lookupext = self.extensions.getextensions(self.extoptions[self.targetfiletype_combo.current()])
        targetfiles = self.utils.listdirectory(lookupext,d)
        self.targetfilestextbox.delete('1.0', END) #REVIEW - WHy does it need 1.0 when the entry needs just 0, need to understand this parameters.
        for f in targetfiles:
            self.targetfilestextbox.insert(END,f+'\n')