import tkinter as tk
from tkinter import ttk

class SuhuKoverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Konversi Suhu")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f8ff")

        # Membuat frame untuk tata letak
        self.frame = ttk.Frame(root, padding="30", relief="groove", borderwidth=2)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Membuat label dan entry untuk input suhu
        self.label = ttk.Label(self.frame, text="Masukkan suhu:", font=("Times New Roman", 14, "bold"))
        self.label.pack(pady=10)
        self.entry = ttk.Entry(self.frame, width=20, font=("Times New Roman", 14))
        self.entry.pack(pady=10)

        # Pilihan untuk jenis suhu input
        self.input_scale_var = tk.StringVar(value="Celsius")
        self.input_scale_label = ttk.Label(self.frame, text="Pilih jenis suhu input:", font=("Times New Roman", 14))
        self.input_scale_label.pack(pady=10)
        self.input_scale_menu = ttk.Combobox(self.frame, textvariable=self.input_scale_var,values=["Celsius", "Fahrenheit", "Kelvin", "Reamur"], font=("Times New Roman", 14))
        self.input_scale_menu.pack(pady=10)

        # Pilihan untuk jenis suhu output
        self.output_scale_var = tk.StringVar(value="Fahrenheit")
        self.output_scale_label = ttk.Label(self.frame, text="Pilih jenis suhu output:", font=("Times New Roman", 14))
        self.output_scale_label.pack(pady=10)
        self.output_scale_menu = ttk.Combobox(self.frame, textvariable=self.output_scale_var,values=["Celsius", "Fahrenheit", "Kelvin", "Reamur"], font=("Times New Roman", 14))
        self.output_scale_menu.pack(pady=10)

        # Tombol untuk melakukan konversi
        self.konversi_button = ttk.Button(self.frame, text="Konversi", command=self.convert_temperature, width=15)
        self.konversi_button.pack(pady=20)

        # Label untuk menampilkan hasil
        self.hasil_label = ttk.Label(self.frame, text="", font=("Times New Roman", 16, "bold"))
        self.hasil_label.pack(pady=20)

    def convert_temperature(self):
        try:
            input_temp = float(self.entry.get())
            input_scale = self.input_scale_var.get()
            output_scale = self.output_scale_var.get()
            
            if input_scale == "Celsius":
                celsius = input_temp
            elif input_scale == "Fahrenheit":
                celsius = (input_temp - 32) * 5/9
            elif input_scale == "Kelvin":
                celsius = input_temp - 273.15
            else:  # Reamur
                celsius = input_temp * 5/4

            if output_scale == "Celsius":
                hasil = celsius
            elif output_scale == "Fahrenheit":
                hasil = (celsius * 9/5) + 32
            elif output_scale == "Kelvin":
                hasil = celsius + 273.15
            else:  # Reamur
                hasil = celsius * 4/5

            self.hasil_label.config(text=f"{input_temp} °{input_scale[0]} = {hasil:.2f} °{output_scale[0]}")
        except ValueError:
            self.hasil_label.config(text="Input tidak valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SuhuKoverterApp(root)
    root.mainloop()
