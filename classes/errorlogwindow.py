import tkinter as tk
from tkinter import END, Toplevel, ttk, messagebox, filedialog
from tkinter import scrolledtext




class ErrorLogWindow(Toplevel):

    def __init__(self, errors):
        Toplevel.__init__(self)
        self.errors = errors
        labelfontsize = 14
        entryfontsize = 14

        self.geometry("800x470")
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
        for f in self.errors:
            self.errorstextbox.insert(END,f+'\n')


        # Save and Settings buttons
        cancel_button = ttk.Button(
            self, text="Cancel", style='Outline.TButton', command=self.quit)
        cancel_button.grid(column=0, row=7, sticky=tk.W,
                           padx=10, pady=5, ipady=20, ipadx=20)


        # # version Label
        # version_label = ttk.Label(
        #     self, text="Version: " + constants.version, font=("Arial", 10))
        # version_label.grid(column=1, row=8, sticky=tk.E,
        #                    padx=(0, 5), pady=(10, 10))
