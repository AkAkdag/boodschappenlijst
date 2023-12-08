import tkinter as tk
from tkinter import messagebox

class BoodschappenLijst:
    def __init__(self):
        self.artikellen = []

    def voeg_artikel_toe(self, artikel):
        self.artikellen.append(artikel)

    def verwijder_artikel(self, artikel):
        if artikel in self.artikellen:
            self.artikellen.remove(artikel)
            return True
        return False

    def leegmaken_lijst(self):
        self.artikellen.clear()

    def toon_lijst(self):
        return self.artikellen

class BoodschappenLijstAppTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title("Boodschappenlijst App")

        self.boodschappen_lijst = BoodschappenLijst()

        self.create_widgets()



    def create_widgets(self):

        
        self.label = tk.Label(self.master, text="Boodschappenlijst", fg="blue", bg="lightblue", font= "5" )
        self.label.pack()



        # ronde buttons
        ronde_button_style = {"borderwidth": 2, "relief": tk.GROOVE, "width": 12, "height": 2, "bg": "blue", "fg": "white", }
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.add_button = tk.Button(self.master, text="Voeg toe", command=self.voeg_artikel_toe)
        self.add_button.config(**ronde_button_style)
        self.add_button.pack()

        self.show_button = tk.Button(self.master, text="Toon lijst", command=self.toon_lijst)
        self.show_button.config(**ronde_button_style)
        self.show_button.pack()

        self.remove_button = tk.Button(self.master, text="Verwijder artikel", command=self.verwijder_artikel)
        self.remove_button.config(**ronde_button_style)
        self.remove_button.pack()

        self.clear_button = tk.Button(self.master, text="Wis lijst", command=self.wis_lijst)
        self.clear_button.config(**ronde_button_style)
        self.clear_button.pack()

        self.quit_button = tk.Button(self.master, text="Stoppen", command=self.master.destroy)
        self.quit_button.config(**ronde_button_style)
        self.quit_button.pack()

        # Label to display the list
        self.list_label = tk.Label(self.master, text="")
        self.list_label.pack()

    def voeg_artikel_toe(self):
        artikel = self.entry.get().upper()
        self.boodschappen_lijst.voeg_artikel_toe(artikel)
        messagebox.showinfo("Succes", f"{artikel} is aan de lijst toegevoegd")
        self.entry.delete(0, tk.END)

    def toon_lijst(self):
        lijst = self.boodschappen_lijst.toon_lijst()
        if not lijst:
            self.list_label.config(text="U heeft nul artikelen in uw lijst")
        else:
            self.list_label.config(text="Artikelen in de lijst:\n" + "\n".join(lijst))

    def verwijder_artikel(self):
        artikel = self.entry.get().upper()
        if self.boodschappen_lijst.verwijder_artikel(artikel):
            messagebox.showinfo("Succes", f"{artikel} is van de lijst verwijderd")
        else:
            messagebox.showwarning("Waarschuwing", "Dat artikel staat niet in de lijst")
        self.entry.delete(0, tk.END)

    def wis_lijst(self):
        self.boodschappen_lijst.leegmaken_lijst()
        messagebox.showinfo("Succes", "Lijst is leeg")

def main():
    root = tk.Tk()
    root.configure(bg="lightblue")
    app = BoodschappenLijstAppTkinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
