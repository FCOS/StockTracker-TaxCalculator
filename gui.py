import tkinter as tk
from tkinter.filedialog import askopenfilename
from StockTracker import Portfolio


class StockTrackerGui:

    def __init__(self, master):
        self.master = master
        
        #Display
        self.master.title("StockTracker")
        self.master.columnconfigure(0, minsize=800, weight=1)
        self.master.rowconfigure(1, minsize=600, weight=1)

        # Header frame
        self.frm_header = tk.Frame(self.master)
        self.lbl_header_date = tk.Label(self.frm_header, text="28/10/2020", bg="red")
        self.lbl_header_date.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        self.lbl_header_value = tk.Label(self.frm_header, text="0", bg="blue")
        self.lbl_header_value.grid(row=0, column=1, sticky="sewn", padx=10, pady=10)
        self.frm_header.columnconfigure(1, minsize=500, weight=1)

        # Body Frame
        self.frm_body = tk.Frame(self.master, bg="pink")

        # Side bar sub frame
        self.frm_body_side_bar = tk.Frame(self.frm_body, bg="brown")
        self.btn_load_csv = tk.Button(self.frm_body_side_bar, text="Open Portfolio", command=self.load_csv)
        self.btn_enter_manual = tk.Button(self.frm_body_side_bar, text="New Portfolio")
        self.btn_reset = tk.Button(self.frm_body_side_bar, text="Close Portfolio", command=self.close_portfolio)
        self.btn_load_csv.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_reset.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.btn_reset.grid_remove()
        self.btn_enter_manual.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # Main body sub frame
        self.frm_body_main = tk.Frame(self.frm_body, bg="green")
        self.lbl_body_main = tk.Label(self.frm_body_main, text="body")
        self.lbl_body_main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.frm_body_main.rowconfigure(0, weight=1)
        self.frm_body_main.columnconfigure(0, weight=1)

        self.frm_body_side_bar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
        self.frm_body_main.grid(row=0, column=1, sticky="nesw", padx=10, pady=10)

        self.frm_body.columnconfigure(1, weight=1)
        self.frm_body.rowconfigure(0, weight=1)

        # Footer frame
        self.frm_footer = tk.Frame(self.master)
        self.lbl_footer_author = tk.Label(self.frm_footer, text="Developed by Fergal O'Shea - foshea@tcd.ie", bg="yellow")
        self.lbl_footer_author.grid(row=0, column=0, sticky="ews", padx=10, pady=1)

        # window
        self.frm_header.grid(row=0, column=0, sticky="news")
        self.frm_body.grid(row=1, column=0, sticky="news")
        self.frm_footer.grid(row=2, column=0)

        #self.reset_gui()

    def close_portfolio(self):
        self.portfolio = None

        # Reset values
        self.lbl_header_value["text"] = "0"

        #Remove close button
        self.btn_reset.grid_remove()
        # Recover add/new buttons
        self.btn_load_csv.grid()
        self.btn_enter_manual.grid()


    def load_csv(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )
        if not filepath:
            return
            
        self.portfolio = Portfolio(filepath, 'degiro')

        #window_frames = self.master.winfo_children()
        #print(window_frames)
        self.lbl_header_value["text"] = str(self.portfolio.value)

        #Add close portfolio button
        self.btn_reset.grid()

        # Remove 'new/add' buttons
        self.btn_load_csv.grid_remove()
        self.btn_enter_manual.grid_remove()


def configure_default_window():
    # Display stuff
    window.title("StockTracker")

    window.columnconfigure(0, minsize=800, weight=1)
    window.rowconfigure(1, minsize=600, weight=1)

    # Header frame
    frm_header = tk.Frame(window)
    lbl_header_date = tk.Label(frm_header, text="28/10/2020", bg="red")
    lbl_header_date.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

    lbl_header_value = tk.Label(frm_header, text="0", bg="blue")
    lbl_header_value.grid(row=0, column=1, sticky="sewn", padx=10, pady=10)
    #frm_header.columnconfigure(0, weight=1)
    frm_header.columnconfigure(1, minsize=500, weight=1)

    # Body Frame
    frm_body = tk.Frame(window, bg="pink")

    # Side bar sub frame
    frm_body_side_bar = tk.Frame(frm_body, bg="brown")
    btn_load_csv = tk.Button(frm_body_side_bar, text="Open Portfolio", command=load_csv)
    btn_enter_manual = tk.Button(frm_body_side_bar, text="New Portfolio")
    btn_load_csv.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_enter_manual.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    # Main body sub frame
    frm_body_main = tk.Frame(frm_body, bg="green")
    lbl_body_main = tk.Label(frm_body_main, text="body")
    lbl_body_main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    frm_body_main.rowconfigure(0, weight=1)
    frm_body_main.columnconfigure(0, weight=1)

    frm_body_side_bar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)
    frm_body_main.grid(row=0, column=1, sticky="nesw", padx=10, pady=10)

    frm_body.columnconfigure(1, weight=1)
    frm_body.rowconfigure(0, weight=1)

    # Footer frame
    frm_footer = tk.Frame(window)
    lbl_footer_author = tk.Label(frm_footer, text="Developed by Fergal O'Shea - foshea@tcd.ie", bg="yellow")
    lbl_footer_author.grid(row=0, column=0, sticky="ews", padx=10, pady=1)

    # window
    frm_header.grid(row=0, column=0, sticky="news")
    frm_body.grid(row=1, column=0, sticky="news")
    frm_footer.grid(row=2, column=0)

    return window



def main():
    window = tk.Tk()
    mainGui = StockTrackerGui(window)
    window.mainloop()

if __name__=="__main__":
    main()