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
        self.card_collection = {}

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "pokemon":
            self.show_gacha_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_gacha_window(self):
        self.login_frame.destroy()

        self.gacha_frame = tk.Frame(self.master)
        self.gacha_frame.pack(pady=20)

        self.pack_label = tk.Label(self.gacha_frame, text="Pilih Pack:")
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

        self.collection_button = tk.Button(self.gacha_frame, text="Lihat Koleksi", command=self.show_collection)
        self.collection_button.pack(pady=10)

    def gacha(self):
        selected_indices = self.pack_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Tolong pilih pack terlebih dahulu")
            return

        selected_pack = self.pack_listbox.get(selected_indices[0])
        cards = {
            "Pack Scarlet EX": ["Lucario", "Koraidon EX", "Toxicroak EX", "Gardevoir EX", "Gyarados EX"],
            "Pack Violet EX": ["Arcanine EX", "Banette EX", "Magnezone EX", "Toxtricity", "Miraidon EX"],
            "Pack VSTAR Semesta": ["Charizard Vstar", "Mewtwo Vstar", "Mew Vmax", "Moltres V", "Giratina V", "Charizard Bercahaya"]
        }
        selected_card = random.choice(cards[selected_pack])
        self.animate_spin(selected_pack, cards[selected_pack], selected_card)

    def animate_spin(self, selected_pack, card_list, selected_card):
        self.result_textbox.delete(1.0, tk.END)
        spins = 15
        delay = 80

        def update_spin(count):
            if count < spins:
                display_card = random.choice(card_list)
                self.result_textbox.delete(1.0, tk.END)
                self.result_textbox.insert(tk.END, f"Spinning... {display_card}\n")
                self.master.after(delay, update_spin, count + 1)
            else:
                self.result_textbox.delete(1.0, tk.END)
                result_message = f"Kamu mendapatkan {selected_card} dari {selected_pack}!"
                self.result_textbox.insert(tk.END, result_message + "\n")
                self.update_collection(selected_card)

        update_spin(0)

    def update_collection(self, card):
        if card in self.card_collection:
            self.card_collection[card] += 1
        else:
            self.card_collection[card] = 1

    def show_collection(self):
        collection_window = tk.Toplevel(self.master)
        collection_window.title("Koleksi Kartu")
        collection_window.geometry("300x400")

        collection_textbox = tk.Text(collection_window, width=40, height=20, wrap=tk.WORD)
        collection_textbox.pack(pady=10)

        collection_textbox.insert(tk.END, "Daftar Kartu yang Didapat:\n")
        for card, count in self.card_collection.items():
            collection_textbox.insert(tk.END, f"{card}: {count}\n")

        close_button = tk.Button(collection_window, text="Tutup", command=collection_window.destroy)
        close_button.pack(pady=10)

def main():
    root = tk.Tk()
    root.game = PokemonGachaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()