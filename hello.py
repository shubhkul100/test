import tkinter as tk
app = tk.Tk()
app.title("Test")
app.state('zoomed')
app.configure(bg="black")
label = tk.Label(app, text="TEST", font=("Arial", 24, "bold"), fg="white", bg="black")
label.pack(pady=20)
app.mainloop()
