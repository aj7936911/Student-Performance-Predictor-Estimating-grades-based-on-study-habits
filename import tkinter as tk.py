import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Student Performance Predictor")
root.geometry("900x600")
root.minsize(800, 550)

# ---------------- IMAGE PATHS ----------------
HOME_BG_PATH = r"C:\Users\ASUS\Downloads\cartoon-ai-robot-character-scene.jpg"
PREDICT_BG_PATH = r"C:\Users\ASUS\Downloads\view-robot-tending-maintaining-gardens.jpg"

# ---------------- FRAMES ----------------
home_page = tk.Frame(root)
predict_page = tk.Frame(root)

for frame in (home_page, predict_page):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# ---------------- BACKGROUND FUNCTION ----------------
def set_background(frame, img_path):
    img = Image.open(img_path)
    bg = tk.Label(frame)
    bg.place(relwidth=1, relheight=1)
    bg.lower()

    def resize(e):
        resized = img.resize((e.width, e.height))
        photo = ImageTk.PhotoImage(resized)
        bg.config(image=photo)
        bg.image = photo

    frame.bind("<Configure>", resize)

# ---------------- FADE FUNCTIONS ----------------
def fade_in(frame):
    frame.tkraise()
    root.attributes("-alpha", 0.0)

    def fade(alpha=0.0):
        if alpha >= 1.0:
            root.attributes("-alpha", 1.0)
            return
        root.attributes("-alpha", alpha)
        root.after(15, lambda: fade(alpha + 0.05))

    fade()

# ================= HOME PAGE =================
set_background(home_page, HOME_BG_PATH)

header = tk.Frame(home_page, bg="#0d47a1", height=80)
header.pack(fill="x")

tk.Label(
    header, text="Student Performance Predictor",
    font=("Arial", 24, "bold"),
    bg="#0d47a1", fg="white"
).pack(pady=(15, 0))

tk.Label(
    header, text="AI Project",
    font=("Arial", 11),
    bg="#0d47a1", fg="#cfd8dc"
).pack()

content = tk.Frame(home_page, bg="white", width=520, height=300)
content.place(relx=0.5, rely=0.5, anchor="center")
content.pack_propagate(False)

tk.Label(
    content, text="Welcome!",
    font=("Arial", 26, "bold"),
    bg="white", fg="#0d47a1"
).pack(pady=25)

tk.Label(
    content,
    text="Predict student performance\nbased on study habits using AI logic.",
    font=("Arial", 14),
    bg="white", fg="#333",
    justify="center"
).pack(pady=15)

tk.Button(
    content,
    text="Get Started",
    font=("Arial", 14, "bold"),
    bg="#0d47a1", fg="white",
    bd=0, width=18, height=2,
    command=lambda: fade_in(predict_page)
).pack(pady=25)

footer = tk.Frame(home_page, bg="#0d47a1", height=30)
footer.pack(side="bottom", fill="x")

tk.Label(
    footer, text="© Samsung Innovation Campus",
    bg="#0d47a1", fg="white",
    font=("Arial", 10)
).pack(pady=3)

# ================= PREDICT PAGE =================
set_background(predict_page, PREDICT_BG_PATH)

p_header = tk.Frame(predict_page, bg="#0d47a1", height=60)
p_header.pack(fill="x")

tk.Label(
    p_header, text="Student Performance Predictor",
    font=("Arial", 18, "bold"),
    bg="#0d47a1", fg="white"
).pack(pady=15)

card = tk.Frame(predict_page, bg="white", width=460, height=540)
card.place(relx=0.5, rely=0.15, anchor="n")
card.pack_propagate(False)

tk.Label(
    card, text="Enter Student Details",
    font=("Arial", 16, "bold"),
    bg="white", fg="#0d47a1"
).pack(pady=15)

tk.Label(card, text="Student Name", bg="white").pack(anchor="w", padx=30)
entry_name = tk.Entry(card, font=("Arial", 11))
entry_name.pack(fill="x", padx=30, pady=6)

def dropdown(label, values, default):
    tk.Label(card, text=label, bg="white").pack(anchor="w", padx=30)
    cb = ttk.Combobox(card, values=values, state="readonly")
    cb.set(default)
    cb.pack(fill="x", padx=30, pady=6)
    return cb

combo_study = dropdown("Study Hours (per day)", [str(i) for i in range(1,11)], "4")
combo_attendance = dropdown("Attendance (%)", [str(i) for i in range(50,101,5)], "75")
combo_practice = dropdown("Practice Tests Count", [str(i) for i in range(0,9)], "2")
combo_sleep = dropdown("Sleep Hours", [str(i) for i in range(4,11)], "7")

result = tk.Label(
    card, text="",
    font=("Arial", 14, "bold"),
    bg="white", fg="#0d47a1",
    justify="center", wraplength=380
)
result.pack(pady=15)

def predict():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("Required", "Please enter student name")
        return

    study = float(combo_study.get())
    attend = float(combo_attendance.get())
    practice = int(combo_practice.get())
    sleep = float(combo_sleep.get())

    marks = (study * 5) + (attend * 0.3) + (practice * 3) + (sleep * 2)
    marks = min(100, marks)

    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 55:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    result.config(
        text=f"Student Name: {name}\nMarks: {marks:.1f}\nGrade: {grade}"
    )

tk.Button(
    card, text="Predict Result",
    bg="#0d47a1", fg="white",
    font=("Arial", 12, "bold"),
    bd=0, height=2,
    command=predict
).pack(pady=10, padx=30, fill="x")

def back_home():
    result.config(text="")
    entry_name.delete(0, tk.END)
    fade_in(home_page)

tk.Button(
    card, text="← Back to Home",
    bg="white", fg="#0d47a1",
    bd=0,
    command=back_home
).pack(pady=10)

# ---------------- START ----------------
home_page.tkraise()
root.mainloop()
