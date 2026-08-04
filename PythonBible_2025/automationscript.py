import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from datetime import datetime


class BackupGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Backup Tool")
        self.root.geometry("400x200")

        self.setup_ui()

    def setup_ui(self):
        # Origen
        tk.Label(self.root, text="Carpeta Origen:").pack(pady=5)
        self.origen_entry = tk.Entry(self.root, width=50)
        self.origen_entry.pack(pady=5)
        tk.Button(self.root, text="Seleccionar Origen",
                  command=self.seleccionar_origen).pack(pady=5)

        # Destino
        tk.Label(self.root, text="Carpeta Destino:").pack(pady=5)
        self.destino_entry = tk.Entry(self.root, width=50)
        self.destino_entry.pack(pady=5)
        tk.Button(self.root, text="Seleccionar Destino",
                  command=self.seleccionar_destino).pack(pady=5)

        # Botón Backup
        tk.Button(self.root, text="Realizar Backup",
                  command=self.hacer_backup, bg="green", fg="white").pack(pady=20)

    def seleccionar_origen(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.origen_entry.delete(0, tk.END)
            self.origen_entry.insert(0, carpeta)

    def seleccionar_destino(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.destino_entry.delete(0, tk.END)
            self.destino_entry.insert(0, carpeta)

    def hacer_backup(self):
        origen = self.origen_entry.get()
        destino = self.destino_entry.get()

        if not origen or not destino:
            messagebox.showerror("Error", "Selecciona origen y destino")
            return

        try:
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            destino_final = os.path.join(destino, f"backup_{fecha}")
            shutil.copytree(origen, destino_final)
            messagebox.showinfo("Éxito", f"Backup completado:\n{destino_final}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en backup:\n{str(e)}")

    def run(self):
        self.root.mainloop()


# Ejecutar interfaz
if __name__ == "__main__":
    app = BackupGUI()
    app.run()

