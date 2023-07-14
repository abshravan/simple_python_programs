import tkinter
import tkinter.ttk
import tkinter.messagebox


class MainWindow():

    C_FONT = ("Consolas", 16)
    C_TXT_MAXLEN = 32
    
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.title("Number Converter")
        self._window.geometry("1220x300")
        self._window.configure(background='light blue')
        self._window.resizable(False, False)
        
        self._input_format = tkinter.StringVar()
        self._output_format = tkinter.StringVar()

        label_input = tkinter.Label(self._window, text="Input:", font=MainWindow.C_FONT)
        label_input.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self._txt_input = tkinter.Entry(self._window, width=MainWindow.C_TXT_MAXLEN, font=MainWindow.C_FONT)
        self._txt_input.grid(row=0, column=1, pady=5)
        self._txt_input.focus()

        label_output = tkinter.Label(self._window, text="Output:", font=MainWindow.C_FONT)
        label_output.grid(row=0, column=2, padx=10, pady=5, sticky="e")

        self._stringvar_output = tkinter.StringVar()
        txt_output = tkinter.Entry(self._window, textvariable=self._stringvar_output, width=MainWindow.C_TXT_MAXLEN, state="readonly", font=MainWindow.C_FONT)
        txt_output.grid(row=0, column=3, pady=5)
        
        label_input_format = tkinter.Label(self._window, text="Input Format:", font=MainWindow.C_FONT)
        label_input_format.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        input_formats = ["Binary", "Decimal", "Hexadecimal"]
        self._combo_input_format = tkinter.ttk.Combobox(self._window, values=input_formats, textvariable=self._input_format, font=MainWindow.C_FONT)
        self._combo_input_format.grid(row=1, column=1, pady=5)
        self._combo_input_format.current(0)
        
        label_output_format = tkinter.Label(self._window, text="Output Format:", font=MainWindow.C_FONT)
        label_output_format.grid(row=1, column=2, padx=10, pady=5, sticky="e")
        
        output_formats = ["Binary", "Decimal", "Hexadecimal"]
        self._combo_output_format = tkinter.ttk.Combobox(self._window, values=output_formats, textvariable=self._output_format, font=MainWindow.C_FONT)
        self._combo_output_format.grid(row=1, column=3, pady=5)
        self._combo_output_format.current(1)

        self._bt_convert = tkinter.Button(self._window, text="Convert", font=MainWindow.C_FONT, command=self.evt_bt_convert)
        self._bt_convert.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

        self._bt_clear = tkinter.Button(self._window, text="Clear", font=MainWindow.C_FONT, command=self.evt_bt_clear)
        self._bt_clear.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

    def evt_bt_convert(self):
        try:
            input_value = self._txt_input.get().strip().replace(" ", "")
            input_format = self._input_format.get()
            output_format = self._output_format.get()

            output_value = self.convert(input_value, input_format, output_format)
            self._stringvar_output.set(output_value)

        except Exception:
            tkinter.messagebox.showerror("Error", "Invalid conversion")

    def evt_bt_clear(self):
        self._txt_input.delete(0, tkinter.END)
        self._stringvar_output.set("")

    def convert(self, value, input_format, output_format):
        if input_format == "Binary":
            if output_format == "Decimal":
                return str(int(value, 2))
            elif output_format == "Hexadecimal":
                return hex(int(value, 2))
        elif input_format == "Decimal":
            if output_format == "Binary":
                return bin(int(value))
            elif output_format == "Hexadecimal":
                return hex(int(value))
        elif input_format == "Hexadecimal":
            if output_format == "Binary":
                return bin(int(value, 16))
            elif output_format == "Decimal":
                return str(int(value, 16))
        
        return ""

    def mainloop(self):
        self._window.mainloop()


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()
