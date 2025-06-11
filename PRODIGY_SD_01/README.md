## Temperature Conversion Program

# A comprehensive temperature conversion utility that converts temperatures between Celsius, Fahrenheit, and Kelvin scales.

## 🌡️ Overview

# This program provides an easy-to-use interface for converting temperatures between the three most commonly used temperature scales:

- Celsius (°C) - Metric scale where water freezes at 0° and boils at 100°
- Fahrenheit (°F) - Imperial scale where water freezes at 32° and boils at 212°
- Kelvin (K) - Absolute temperature scale starting at absolute zero

# ✨ Features

- Convert between all three temperature scales
- Input validation to ensure valid temperature values
- User-friendly command-line interface
- Error handling for invalid inputs
- Support for decimal values
- Clear output formatting with proper units

# 🚀 Getting Started

# This project includes implementations in both JavaScript and Python with GUI interfaces.
JavaScript Version (Web-based GUI)

# Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- No additional installations required

## Installation

- Clone this repository or download the source code
- Open index.html in your web browser
- The application runs directly in the browser

- Python Version (Desktop GUI)

# Prerequisites

- Python3 higher
- tkinter (usually included with Python)

## Installation

- Clone this repository or download the source code

# Install required dependencies:

- bashpip install tkinter

# Run the GUI application:

- bashpython temperature_converter_gui.py

# 💡 Usage

# JavaScript Web Version

- Open index.html in your browser
- Enter a temperature value in the input field
- Select source and target temperature scales from dropdown menus
- Click "Convert" button to see the result
- The conversion happens instantly with live validation

# Python Desktop Version

- Run the Python GUI application
- Enter temperature value in the input field
- Select source and target scales using radio buttons or dropdowns
- Click "Convert" button to see the result
- Use "Clear" to reset all fields

# Example Conversions

- 0°C = 32°F = 273.15K (Water freezing point)
- 100°C = 212°F = 373.15K (Water boiling point)
- -273.15°C = -459.67°F = 0K (Absolute zero)

## 🧮 Conversion Formulas

# Celsius to Fahrenheit

- °F = (°C × 9/5) + 32

# Celsius to Kelvin

- K = °C + 273.15

# Fahrenheit to Celsius

- °C = (°F - 32) × 5/9

# Fahrenheit to Kelvin

- K = (°F - 32) × 5/9 + 273.15

# Kelvin to Celsius

- °C = K - 273.15

# Kelvin to Fahrenheit

- °F = (K - 273.15) × 9/5 + 32

# 🔧 Technical Implementation

# Core Functions

- celsius_to_fahrenheit(celsius) - Converts Celsius to Fahrenheit
- celsius_to_kelvin(celsius) - Converts Celsius to Kelvin
- fahrenheit_to_celsius(fahrenheit) - Converts Fahrenheit to Celsius
- fahrenheit_to_kelvin(fahrenheit) - Converts Fahrenheit to Kelvin
- kelvin_to_celsius(kelvin) - Converts Kelvin to Celsius
- kelvin_to_fahrenheit(kelvin) - Converts Kelvin to Fahrenheit
- convert_temperature(value, from_scale, to_scale) - Main conversion function
- validate_input(value, scale) - Input validation function
- main() - Main program loop with user interface

# Input Validation

- Checks for valid numeric input
- Validates temperature scales (C, F, K)
- Ensures Kelvin values are not below absolute zero (-273.15°C)
- Handles invalid input gracefully with error messages

## 🧪 Testing

# The program includes input validation and error handling for:

- Non-numeric inputs
- Invalid temperature scales
- Temperatures below absolute zero in Kelvin
- Edge cases and boundary conditions

## 🤝 Contributing

- Fork the repository
- Create a feature branch
- Make your changes
- Add tests if applicable
- Submit a pull request

## 📄 License

- This project is open source and available under the MIT License.

## 🎯 Future Enhancements

# JavaScript Version

- Progressive Web App (PWA) functionality
- Dark/light theme toggle
- Temperature conversion history
- Responsive design for mobile devices
- Real-time conversion as you type
- Temperature scale comparison charts

# Python Version

- Modern UI with PyQt5/PyQt6 or tkinter themes
- System tray integration
- Batch conversion from CSV files
- Temperature logging and graphing
- Keyboard shortcuts
- Multiple window support

## Both Versions

- Scientific notation support
- Temperature conversion API
- Unit tests with automated testing
- Internationalization (multiple languages)
- Accessibility features

Built as part of ProDigy InfoTech internship program
