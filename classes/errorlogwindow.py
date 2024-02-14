import tkinter as tk
from tkinter import END, Toplevel, ttk, messagebox, filedialog
from tkinter import scrolledtext




class ErrorLogWindow(Toplevel):
    '''Error Log Window Class

    Args:
        Toplevel: Toplevel widget, the Main window
    '''

    def __init__(self, errors):
        Toplevel.__init__(self)
        self.errors = errors
        labelfontsize = 14
        entryfontsize = 14

        self.geometry("880x470")
        self.labelfontsize = labelfontsize
        self.entryfontsize = entryfontsize

        self.resizable(False, False)
        self.title('Python Image Converter - Error Logs')
        self.iconbitmap('icon.ico')

        # make sure only main window cant be changed
        self.grab_set()

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    # close window
    def quit(self):
        self.destroy()

    # populate form
    def create_widgets(self):
        
        # Label Frame
        project_label_widget = ttk.Label(self, text="Last Run's Error Logs", font=(None, self.entryfontsize))
        project_labelframe = ttk.LabelFrame(self, labelwidget=project_label_widget)
        project_labelframe.grid(column=0, row=1, columnspan=2, sticky=tk.EW, padx=10, pady=(20, 10))
        project_labelframe.columnconfigure(0, weight=1)


        # Errors ScrolledText 
        self.errorstextbox = scrolledtext.ScrolledText(
            master=project_labelframe,
            highlightthickness=1
        )
        self.errorstextbox.grid(column=0, row=5, columnspan=2,sticky=tk.EW, padx=(10,0), pady=(5,10))
        
        self.errorstextbox.delete('1.0', END) #REVIEW - WHy does it need 1.0 when the entry needs just 0, need to understand this parameters.
        for e in self.errors:
            if e != '':
                self.errorstextbox.insert(END,e+'\n')