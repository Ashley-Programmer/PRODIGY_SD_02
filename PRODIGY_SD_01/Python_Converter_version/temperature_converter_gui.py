import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverter:
    def __init__(self, root):
        """Initialize the temperature converter application"""
        
        self.root = root
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.setup_events()
        
    def setup_window(self):
        """Set up the main window properties and styling"""
        
        # Basic window configuration
        self.root.title("Converter - ProDigy InfoTech")
        self.root.geometry("650x550")
        self.root.resizable(True, True)
        
        # Apply a modern theme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create custom styles for different elements
        style.configure('Title.TLabel', font=('Arial', 18, 'bold'), foreground="#001667")
        style.configure('Subtitle.TLabel', font=('Arial', 10), foreground="#4600e9")
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#34495e')
        style.configure('Result.TLabel', font=('Arial', 14, 'bold'), foreground='#27ae60')
        style.configure('Error.TLabel', font=('Arial', 12), foreground='#e74c3c')
        style.configure('Convert.TButton', font=('Arial', 12, 'bold'))
        
        # Center the window on screen
        self.center_window()
        
    def center_window(self):
        """Center the window on the screen"""
        
        self.root.update_idletasks()  # Make sure window is fully loaded
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_variables(self):
        """Create all the variables to store data"""
        
        self.temp_var = tk.StringVar()  # User's temperature input
        self.from_scale_var = tk.StringVar(value="celsius")  # Convert FROM this unit
        self.to_scale_var = tk.StringVar(value="fahrenheit")  # Convert TO this unit
        self.result_var = tk.StringVar()  # The conversion result
        self.formula_var = tk.StringVar()  # The formula used
        self.error_var = tk.StringVar()  # Error messages
        
    def create_widgets(self):
        """Create and arrange all the visual elements"""
        
        # Main container frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Make the window resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(8, weight=1)
        
        # TITLE SECTION
        title_label = ttk.Label(main_frame, text="🌡️ Auto Temperature Converter", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        subtitle_label = ttk.Label(main_frame, 
                                  text="Convert between Celsius, Fahrenheit, and Kelvin",
                                  style='Subtitle.TLabel')
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # TEMPERATURE INPUT SECTION
        ttk.Label(main_frame, text="Temperature Value:", 
                 style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        temp_entry = ttk.Entry(main_frame, textvariable=self.temp_var, 
                              font=('Arial', 12), width=20)
        temp_entry.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        temp_entry.focus()  # Put cursor here when app starts
        
        # FROM UNIT SELECTION (Left side)
        ttk.Label(main_frame, text="From:", 
                 style='Header.TLabel').grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        from_frame = ttk.Frame(main_frame)
        from_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Radiobutton(from_frame, text="Celsius (°C)", variable=self.from_scale_var, 
                       value="celsius").pack(anchor=tk.W)
        ttk.Radiobutton(from_frame, text="Fahrenheit (°F)", variable=self.from_scale_var, 
                       value="fahrenheit").pack(anchor=tk.W)
        ttk.Radiobutton(from_frame, text="Kelvin (K)", variable=self.from_scale_var, 
                       value="kelvin").pack(anchor=tk.W)
        
        # ARROW BETWEEN SELECTIONS
        ttk.Label(main_frame, text="→", font=('Arial', 20)).grid(row=5, column=1, padx=10)
        
        # TO UNIT SELECTION (Right side)
        ttk.Label(main_frame, text="To:", 
                 style='Header.TLabel').grid(row=4, column=2, sticky=tk.W, pady=(0, 5))
        
        to_frame = ttk.Frame(main_frame)
        to_frame.grid(row=5, column=2, sticky=(tk.W, tk.E), padx=(10, 0))
        
        ttk.Radiobutton(to_frame, text="Celsius (°C)", variable=self.to_scale_var, 
                       value="celsius").pack(anchor=tk.W)
        ttk.Radiobutton(to_frame, text="Fahrenheit (°F)", variable=self.to_scale_var, 
                       value="fahrenheit").pack(anchor=tk.W)
        ttk.Radiobutton(to_frame, text="Kelvin (K)", variable=self.to_scale_var, 
                       value="kelvin").pack(anchor=tk.W)
        
        # BUTTONS SECTION
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        convert_btn = ttk.Button(button_frame, text="Convert Temperature", 
                               command=self.convert_temperature, style='Convert.TButton')
        convert_btn.pack(side=tk.LEFT, padx=(0, 20))
        
        clear_btn = ttk.Button(button_frame, text="Clear All", 
                             command=self.clear_all)
        clear_btn.pack(side=tk.LEFT, padx=(20, 0))
        
        # RESULTS DISPLAY SECTION
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        result_frame.grid_columnconfigure(0, weight=1)
        
        # Main result display
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, 
                                     style='Result.TLabel', wraplength=500)
        self.result_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Formula display
        self.formula_label = ttk.Label(result_frame, textvariable=self.formula_var, 
                                      font=('Courier New', 10), foreground='#3498db')
        self.formula_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # ERROR MESSAGES SECTION
        self.error_label = ttk.Label(main_frame, textvariable=self.error_var, 
                                   style='Error.TLabel', wraplength=500)
        self.error_label.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Make columns expandable
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        
    def setup_events(self):
        """Set up keyboard shortcuts and real-time updates"""
        # Keyboard shortcuts
        self.root.bind('<Return>', lambda e: self.convert_temperature())  # Enter key
        self.root.bind('<Control-n>', lambda e: self.clear_all())  # Ctrl+N
        
        # Real-time conversion as user types or changes selections
        self.temp_var.trace('w', self.on_input_change)
        self.from_scale_var.trace('w', self.on_input_change)
        self.to_scale_var.trace('w', self.on_input_change)
        
    def on_input_change(self, *args):
        """Update conversion automatically when input changes"""
        
        # Clear previous errors
        self.error_var.set("")
        
        # Get the current temperature input
        temp_str = self.temp_var.get().strip()
        
        if not temp_str:
            # If empty, clear results
            self.result_var.set("")
            self.formula_var.set("")
            return
            
        try:
            # Try to convert the input to a number
            temp_value = float(temp_str)
            
            # Do the conversion (but don't show errors while typing)
            self.perform_conversion(temp_value, show_errors=False)
            
        except ValueError:
            
            # If not a valid number, just clear results (don't show error while typing)
            self.result_var.set("")
            self.formula_var.set("")
    
    def convert_temperature(self):
        """Main conversion function when button is clicked"""
        
        temp_str = self.temp_var.get().strip()
        
        # Check if user entered something
        if not temp_str:
            self.show_error("Please enter a temperature value")
            return
            
        try:
            # Convert input to number
            temp_value = float(temp_str)
            # Do the conversion (show errors this time)
            self.perform_conversion(temp_value, show_errors=True)
        except ValueError:
            self.show_error("Please enter a valid number")
    
    def perform_conversion(self, temp_value, show_errors=True):
        """Do the actual temperature conversion"""
        from_scale = self.from_scale_var.get()
        to_scale = self.to_scale_var.get()
        
        try:
            # Check if temperature is physically possible
            self.validate_temperature(temp_value, from_scale)
            
            # Do the conversion
            if from_scale == to_scale:
                # Same unit, no conversion needed
                converted_value = temp_value
            else:
                # Different units, convert
                converted_value = self.get_conversion(temp_value, from_scale, to_scale)
            
            # Show the result
            self.display_result(temp_value, from_scale, converted_value, to_scale)
            self.display_formula(from_scale, to_scale)
            
            # Clear any previous errors
            if show_errors:
                self.error_var.set("")
                
        except ValueError as e:
            # Something went wrong
            if show_errors:
                self.show_error(str(e))
            else:
                # Don't show errors during real-time typing
                self.result_var.set("")
                self.formula_var.set("")
    
    def validate_temperature(self, temp_value, scale):
        """Check if temperature is above absolute zero"""
        if scale == "celsius" and temp_value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        elif scale == "fahrenheit" and temp_value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        elif scale == "kelvin" and temp_value < 0:
            raise ValueError("Kelvin temperature cannot be negative")
    
    def get_conversion(self, temp_value, from_scale, to_scale):
        """Convert temperature between different scales"""
        # Dictionary of all possible conversions
        conversions = {
            ("celsius", "fahrenheit"): lambda c: (c * 9/5) + 32,
            ("celsius", "kelvin"): lambda c: c + 273.15,
            ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9,
            ("fahrenheit", "kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
            ("kelvin", "celsius"): lambda k: k - 273.15,
            ("kelvin", "fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32
        }
        
        # Find the right conversion function
        conversion_func = conversions.get((from_scale, to_scale))
        if conversion_func:
            return conversion_func(temp_value)
        else:
            raise ValueError(f"Conversion from {from_scale} to {to_scale} not supported")
    
    def display_result(self, original_value, from_scale, converted_value, to_scale):
        """Show the conversion result"""
        # Unit symbols for display
        units = {
            "celsius": "°C",
            "fahrenheit": "°F",
            "kelvin": "K"
        }
        
        # Format the result nicely
        result_text = f"{original_value}{units[from_scale]} = {converted_value:.2f}{units[to_scale]}"
        self.result_var.set(result_text)
    
    def display_formula(self, from_scale, to_scale):
        """Show the mathematical formula used"""
        # All the formulas
        formulas = {
            ("celsius", "fahrenheit"): "°F = (°C × 9/5) + 32",
            ("celsius", "kelvin"): "K = °C + 273.15",
            ("fahrenheit", "celsius"): "°C = (°F - 32) × 5/9",
            ("fahrenheit", "kelvin"): "K = (°F - 32) × 5/9 + 273.15",
            ("kelvin", "celsius"): "°C = K - 273.15",
            ("kelvin", "fahrenheit"): "°F = (K - 273.15) × 9/5 + 32"
        }
        
        # Get the right formula
        formula = formulas.get((from_scale, to_scale), "")
        if formula and from_scale != to_scale:
            self.formula_var.set(f"Formula: {formula}")
        else:
            self.formula_var.set("")  # No formula needed for same unit
    
    def show_error(self, message):
        """Display an error message"""
        self.error_var.set(f"Error: {message}")
        self.result_var.set("")  # Clear results when there's an error
        self.formula_var.set("")
    
    def clear_all(self):
        """Reset everything to starting state"""
        self.temp_var.set("")
        self.from_scale_var.set("celsius")
        self.to_scale_var.set("fahrenheit")
        self.result_var.set("")
        self.formula_var.set("")
        self.error_var.set("")
        
        # Put cursor back in temperature input
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Entry):
                        child.focus()
                        break

def main():
    """Start the application"""
    root = tk.Tk()
    app = TemperatureConverter(root)
    
    # Create an "About" dialog with temperature facts
    def show_about():
        about_text = """Temperature Converter v1.0
        
Built for ProDigy InfoTech

Interesting Temperature Facts:
• Absolute zero: -273.15°C (-459.67°F, 0K)
• Water freezes: 0°C (32°F, 273.15K)
• Water boils: 100°C (212°F, 373.15K)
• Human body temperature: ~37°C (98.6°F, 310.15K)
• Room temperature: ~20°C (68°F, 293.15K)

Keyboard Shortcuts:
• Enter: Convert
• Ctrl+N: Clear All
        """
        messagebox.showinfo("About Temperature Converter", about_text)
    
    # Add a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)
    help_menu.add_separator()
    help_menu.add_command(label="Exit", command=root.quit)
    
    # Ask for confirmation before closing
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Start the application
    root.mainloop()

# Run the application
if __name__ == "__main__":
    main()