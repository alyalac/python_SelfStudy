import customtkinter as ctk
 
# --- Window ---
app = ctk.CTk()
app.title("GRAP")
app.geometry("500x400")


def info_dev():
    result.configure(state="normal")
    result.delete("1.0","end")
    result.insert("end", "Andrei Camata - Yala")
    result.configure(state="disabled")

def about_graph():
    result.configure(state="normal")
    result.delete("1.0", "end")
    result.insert("end", "A Graph is a mathematical structure used to model.\n")
    result.insert("end", "A graph (G = (V, E)) consists of a non-empty set of Vertices (V)")
    result.configure(state="disabled")

# --- Widgets ---
btn = ctk.CTkButton(app, text="About Graph", command=about_graph)
btn.pack(pady=20)

btn = ctk.CTkButton(app, text="Dev", command=info_dev)
btn.pack(pady=20)


result = ctk.CTkTextbox(app, width=400, height=150)
result.pack()



result = ctk.CTkTextbox(app, width=400, height=150)
result.pack()







# --- Run ---
app.mainloop()

