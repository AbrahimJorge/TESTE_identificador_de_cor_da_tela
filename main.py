import tkinter as tk
from functions.shared_functions import load_color_dataset
from app.click_function import ClickMode
from app.cropped_function import CroppedMode
from app.result_panel import ResultPanel

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Seletor de Cor")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.geometry("80x80+100+100") 
        self.root.configure(bg="#282828")

        self.is_menu_open = False
        
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.is_dragging_btn = False

       
        self.shared_panel = ResultPanel(self.root)

       
        self.click_mode = ClickMode(self.root, self.shared_panel)
        self.cropped_mode = CroppedMode(self.root, self.shared_panel)

       
        self.btn_ligar = tk.Label(self.root, text="🎨\nLIGAR", bg="#333333", fg="white", 
                                  font=("Arial", 10, "bold"), cursor="hand2")
        self.btn_ligar.pack(fill=tk.BOTH, expand=True)

        self.btn_ligar.bind("<ButtonPress-1>", self.on_btn_press)
        self.btn_ligar.bind("<B1-Motion>", self.on_btn_drag)
        self.btn_ligar.bind("<ButtonRelease-1>", self.on_btn_release)
        self.btn_ligar.bind("<ButtonPress-3>", self.quit_app)

       
        self.options_win = tk.Toplevel(self.root)
        self.options_win.overrideredirect(True)
        self.options_win.attributes('-topmost', True)
        self.options_win.configure(bg="magenta")
        self.options_win.wm_attributes("-transparentcolor", "magenta")
        self.options_win.withdraw()
        
        self.click_mode.options_win = self.options_win
        self.cropped_mode.options_win = self.options_win

        self.btn_click = tk.Button(self.options_win, text="Click", bg="#444444", fg="white",
                                   font=("Arial", 10, "bold"), cursor="hand2", command=self.activate_click)
        self.btn_click.place(x=0, y=0, width=80, height=80)

        self.btn_cropped = tk.Button(self.options_win, text="Cropped", bg="#444444", fg="white",
                                     font=("Arial", 10, "bold"), cursor="hand2", command=self.activate_cropped)
        self.btn_cropped.place(x=90, y=0, width=80, height=80)
        
        self.root.mainloop()

    def update_options_position(self):
       
        x = self.root.winfo_x() + self.root.winfo_width() + 10
        y = self.root.winfo_y()
        self.options_win.geometry(f"170x80+{x}+{y}")

   
    def on_btn_press(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        self.is_dragging_btn = False

    def on_btn_drag(self, event):
        deltax = event.x - self.drag_start_x
        deltay = event.y - self.drag_start_y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
        if self.is_menu_open:
            self.update_options_position()
        self.is_dragging_btn = True

    def on_btn_release(self, event):
        if not self.is_dragging_btn:
            self.toggle_menu()

   
    def toggle_menu(self):
        self.is_menu_open = not self.is_menu_open
        if self.is_menu_open:
            self.btn_ligar.config(bg="#d9534f")
            self.update_options_position()
            self.options_win.deiconify()
        else:
            self.btn_ligar.config(bg="#333333")
            self.options_win.withdraw()
           
            self.click_mode.deactivate()
            self.cropped_mode.deactivate()
            self.reset_buttons()

    def reset_buttons(self):
        self.btn_click.config(bg="#444444", text="Click")
        self.btn_cropped.config(bg="#444444", text="Cropped")

    def activate_click(self):
        self.reset_buttons()
        self.btn_click.config(bg="#5cb85c", text="ATIVO")
        self.cropped_mode.deactivate()
        self.click_mode.activate()

    def activate_cropped(self):
        self.reset_buttons()
        self.btn_cropped.config(bg="#5cb85c", text="ATIVO")
        self.click_mode.deactivate()
        self.cropped_mode.activate()

    def quit_app(self, event):
        self.click_mode.cleanup()
        self.cropped_mode.cleanup()
        self.shared_panel.destroy()
        self.options_win.destroy()
        self.root.destroy()

if __name__ == "__main__":
    print("Iniciando o sistema...")
    if load_color_dataset():
        print("Abrindo interface gráfica...")
        MainMenu()
    else:
        print("Falha ao inicializar o dataset. O programa será encerrado.")
