import tkinter as tk

window = tk.Tk()
window.title("StockTracker")

window.columnconfigure(0, minsize=800, weight=1)
window.rowconfigure(1, minsize=600, weight=1)

# Header frame
frm_header = tk.Frame(window)
lbl_header_date = tk.Label(frm_header, text="28/10/2020", bg="red")
lbl_header_date.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

lbl_header_value = tk.Label(frm_header, text="£534.23", bg="blue")
lbl_header_value.grid(row=0, column=1, sticky="sewn", padx=10, pady=10)
#frm_header.columnconfigure(0, weight=1)
frm_header.columnconfigure(1, minsize=500, weight=1)

# Body Frame
frm_body = tk.Frame(window, bg="pink")

# Side bar sub frame
frm_body_side_bar = tk.Frame(frm_body, bg="brown")
btn_load_csv = tk.Button(frm_body_side_bar, text="Open Portfolio")
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

#window
frm_header.grid(row=0, column=0, sticky="news")
frm_body.grid(row=1, column=0, sticky="news")
frm_footer.grid(row=2, column=0)

window.mainloop()