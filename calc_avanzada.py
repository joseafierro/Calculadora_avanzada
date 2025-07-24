import tkinter as tk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Hybridge")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        self.entrada = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
        self.crear_botones()

    def agregar(self, valor):
        self.entrada.insert(tk.END, valor)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception as e:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def funcion_avanzada(self, tipo):
        try:
            valor = float(self.entrada.get())
            if tipo == 'sin':
                resultado = math.sin(math.radians(valor))
            elif tipo == 'cos':
                resultado = math.cos(math.radians(valor))
            elif tipo == 'log':
                resultado = math.log10(valor)
            elif tipo == 'sqrt':
                resultado = math.sqrt(valor)
            elif tipo == '^2':
                resultado = valor ** 2
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def crear_botones(self):
        botones = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
            ('C',5,0), ('sin',5,1), ('cos',5,2), ('log',5,3),
            ('sqrt',6,0), ('^2',6,1)
        ]

        for (text, row, col) in botones:
            if text == '=':
                cmd = self.calcular
            elif text == 'C':
                cmd = self.limpiar
            elif text in ('sin', 'cos', 'log', 'sqrt', '^2'):
                cmd = lambda t=text: self.funcion_avanzada(t)
            else:
                cmd = lambda t=text: self.agregar(t)

            b = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14), command=cmd)
            b.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
