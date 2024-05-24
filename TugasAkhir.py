import tkinter as tk
from tkinter import messagebox
import random

class PokemonGachaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokemon Gacha TCG")
        self.master.geometry("400x500")

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.gacha_frame = None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.show_gacha_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_gacha_window(self):
        self.login_frame.destroy()

        self.gacha_frame = tk.Frame(self.master)
        self.gacha_frame.pack(pady=20)

        self.pack_label = tk.Label(self.gacha_frame, text="Select Pack:")
        self.pack_label.pack(pady=5)

        self.pack_listbox = tk.Listbox(self.gacha_frame, height=5, selectmode=tk.SINGLE, exportselection=False)
        packs = ["Pack Scarlet EX", "Pack Violet EX", "Pack VSTAR Semesta"]
        for pack in packs:
            self.pack_listbox.insert(tk.END, pack)
        self.pack_listbox.pack(pady=10)

        self.gacha_button = tk.Button(self.gacha_frame, text="Gacha", command=self.gacha)
        self.gacha_button.pack(pady=10)

        self.result_textbox = tk.Text(self.gacha_frame, width=40, height=10, wrap=tk.WORD)
        self.result_textbox.pack(pady=10)

        self.logout_button = tk.Button(self.gacha_frame, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def gacha(self):
        selected_indices = self.pack_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Please select a pack")
            return

        selected_pack = self.pack_listbox.get(selected_indices[0])
        cards = {
            "Pack Scarlet EX": ["Lucario", "Koraidon EX", "Toxicroak EX", "Gardevoir EX", "Gyarados EX"],
            "Pack Violet EX": ["Arcanine EX", "Banette EX", "Magnezone EX", "Toxtricity", "Miraidon EX"],
            "Pack VSTAR Semesta": ["Charizard Vstar", "Mewtwo Vstar", "Mew Vmax", "Moltres V", "Giratina V", "Charizard Bercahaya"]
        }
        selected_card = random.choice(cards[selected_pack])
        result_message = f"Kamu mendapatkan {selected_card} dari {selected_pack}!"
        self.result_textbox.insert(tk.END, result_message + "\n")
        self.result_textbox.see(tk.END)

    def logout(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    game = PokemonGachaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
