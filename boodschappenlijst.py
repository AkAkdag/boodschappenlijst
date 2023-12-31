# "# De broncode van dit programma is ontwikkeld met behulp van de programmeertaal Python, waarbij de programmeerstijl gericht is op objectgeoriënteerd programmeren (OOP). 
# In deze implementatie worden de fundamentele principes van OOP toegepast om de software te structureren en functionaliteiten te organiseren. 
# Dit omvat het gebruik van klassen en objecten om de verschillende entiteiten in het programma te modelleren, waardoor de code meer modulair, herbruikbaar en gemakkelijk te begrijpen wordt.
# Het gebruik van OOP draagt bij aan een efficiënte ontwikkeling en onderhoud van de software, terwijl het ook de leesbaarheid en uitbreidbaarheid bevordert.


import tkinter as tk
from tkinter import messagebox

class BoodschappenLijst:
    def __init__(self):
        self.artikelen = {}

    def voeg_artikel_toe(self, artikel, hoeveelheid=1, prijs=0.0):
        if artikel in self.artikelen:
            self.artikelen[artikel]['hoeveelheid'] += hoeveelheid
            self.artikelen[artikel]['prijs'] += (hoeveelheid * prijs)
        else:
            self.artikelen[artikel] = {'hoeveelheid': hoeveelheid, 'prijs': (hoeveelheid * prijs)}

    def verwijder_artikel(self, artikel, hoeveelheid=1):
        if artikel in self.artikelen:
            self.artikelen[artikel]['hoeveelheid'] -= hoeveelheid
            if self.artikelen[artikel]['hoeveelheid'] <= 0:
                del self.artikelen[artikel]
            else:
                self.artikelen[artikel]['prijs'] -= (hoeveelheid * self.artikelen[artikel]['prijs'] / (self.artikelen[artikel]['hoeveelheid'] + hoeveelheid))
            return True
        return False

    def leegmaken_lijst(self):
        self.artikelen.clear()

    def toon_lijst(self):
        return self.artikelen

    def bereken_totaal_prijs(self):
        totaal_prijs = sum(data['prijs'] for data in self.artikelen.values())
        return totaal_prijs

class BoodschappenLijstAppTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title("Boodschappenlijst App")

        self.boodschappen_lijst = BoodschappenLijst()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Boodschappenlijst", fg="blue", bg="lightblue", font="5")
        self.label.pack()

        # ronde buttons
        ronde_button_style = {"borderwidth": 2, "relief": tk.GROOVE, "width": 12, "height": 2, "bg": "blue", "fg": "white"}

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.quantity_label = tk.Label(self.master, text="Hoeveelheid:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.pack()

        self.price_label = tk.Label(self.master, text="Prijs:")
        self.price_label.pack()

        self.price_entry = tk.Entry(self.master)
        self.price_entry.pack()

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

        self.total_price_label = tk.Label(self.master, text="Totaal Prijs: €0.00")
        self.total_price_label.pack()

        self.quit_button = tk.Button(self.master, text="Stoppen", command=self.master.destroy)
        self.quit_button.config(**ronde_button_style)
        self.quit_button.pack()

        # Label om de lijst weer te geven
        self.list_label = tk.Label(self.master, text="")
        self.list_label.pack()

    def voeg_artikel_toe(self):
        artikel = self.entry.get().upper()
        hoeveelheid = int(self.quantity_entry.get()) if self.quantity_entry.get() else 1
        prijs_entry_value = self.price_entry.get().replace(',', '.')
        prijs = float(prijs_entry_value) if prijs_entry_value else 0.0

        self.boodschappen_lijst.voeg_artikel_toe(artikel, hoeveelheid, prijs)
        messagebox.showinfo("Succes", f"{hoeveelheid} x {artikel} is aan de lijst toegevoegd voor €{prijs:.2f}")
        self.entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.update_total_price_label()

    def toon_lijst(self):
        lijst = self.boodschappen_lijst.toon_lijst()
        if not lijst:
            self.list_label.config(text="U heeft nul artikelen in uw lijst")
        else:
            self.list_label.config(text="Artikelen in de lijst:\n" + "\n".join([f"{artikel}: {data['hoeveelheid']} stuks, €{data['prijs']:.2f}" for artikel, data in lijst.items()]))
        self.update_total_price_label()

    def verwijder_artikel(self):
        artikel = self.entry.get().upper()
        hoeveelheid = int(self.quantity_entry.get()) if self.quantity_entry.get() else 1
        if self.boodschappen_lijst.verwijder_artikel(artikel, hoeveelheid):
            messagebox.showinfo("Succes", f"{hoeveelheid} x {artikel} is van de lijst verwijderd")
        else:
            messagebox.showwarning("Waarschuwing", "Dat artikel staat niet in de lijst")
        self.entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.update_total_price_label()

    def wis_lijst(self):
        self.boodschappen_lijst.leegmaken_lijst()
        messagebox.showinfo("Succes", "Lijst is leeg")
        self.update_total_price_label()

    def update_total_price_label(self):
        totaal_prijs = self.boodschappen_lijst.bereken_totaal_prijs()
        self.total_price_label.config(text=f"Totaal Prijs: €{totaal_prijs:.2f}")

def main():
    root = tk.Tk()
    root.configure(bg="lightblue")
    app = BoodschappenLijstAppTkinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
