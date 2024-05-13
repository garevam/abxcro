import tkinter as tk


# Function to acquire user input
# Prototype! It does not validate input. Precautions must be taken to ensure that only valid numerical input is entered
# and to protect against malicious code injection
def acquire_input():
    expenditure = float(entry_expenditure.get())
    current_capacity = float(entry_current_capacity.get())
    return expenditure, current_capacity


# Function to calculate and display the final result, taking into account the chosen modificators
# Must add error reporting functionality, exception handling
def calculate_output(input_expenditure, input_current_capacity):
    # Prototype formula, assumes that the performance/energy expenditure relationship in directly proportional and
    # linear. This is not accurate: for example, the 0-20% and 80-100% ranges are much less efficient than the 20-80%
    # range. Accurate data and a proper formula must be sourced
    result = input_current_capacity / input_expenditure * 100

    # Adjust the result based on the selected mode from "Fahrweise" (driving style) section
    # These values have been arbitrarily chosen as placeholder. Accurate values must be sourced
    mode_fahrweise = mode_var_fahrweise.get()
    if mode_fahrweise == "Sportlich":
        result *= 0.75  # Reduce the result by 25%
    elif mode_fahrweise == "Oekonomisch":
        result *= 1.25  # Increase the result by 25%

    # Adjust the result based on the selected mode from "Wetter" section
    # These values have been arbitrarily chosen as placeholder. Accurate values must be sourced
    mode_wetter = mode_var_wetter.get()
    if mode_wetter == "Regen":
        result *= 0.85  # Decrease the result by additional 15%
    elif mode_wetter == "Schnee":
        result *= 0.75  # Decrease the result by additional 25%

    label_result.config(text="Verbliebende Reichweite (in km): " + str(result))


# Function to handle radio button selection for the "Fahrweise" section
def select_mode_fahrweise():
    fahrweisemode = mode_var_fahrweise.get()
    print("Selected mode (Fahrweise):", fahrweisemode)


# Function to handle radio button selection for the "Wetter" section
def select_mode_wetter():
    weathermode = mode_var_wetter.get()
    print("Selected mode (Wetter):", weathermode)


"""
GUI CONFIGURATION CODE
"""

# Create main window
root = tk.Tk()
root.title("Komme ich noch Heim?")

# Create input fields
label_expenditure = tk.Label(root, text="Energieverbrauch pro 100km (in kWh):")
label_expenditure.grid(row=0, column=0, padx=5, pady=5)
entry_expenditure = tk.Entry(root)
entry_expenditure.grid(row=0, column=1, padx=5, pady=5)

label_current_capacity = tk.Label(root, text="Aktuelle Kapazität (in kWh):")
label_current_capacity.grid(row=1, column=0, padx=5, pady=5)
entry_current_capacity = tk.Entry(root)
entry_current_capacity.grid(row=1, column=1, padx=5, pady=5)

# Create output field
label_result = tk.Label(root, text="Verbliebende Reichweite (in km) ")
label_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create radio buttons for "Fahrweise" (driving style) section
mode_var_fahrweise = tk.StringVar()
mode_var_fahrweise.set("Normal")  # Default selection
label_fahrweise = tk.Label(root, text="Fahrweise:")
label_fahrweise.grid(row=3, column=0, padx=5, pady=5)
modes_fahrweise = ["Sportlich", "Normal", "Oekonomisch"]
for i, mode in enumerate(modes_fahrweise):
    tk.Radiobutton(root, text=mode, variable=mode_var_fahrweise, value=mode, command=select_mode_fahrweise).grid(row=3,
                                                                                                                 column=i + 1,
                                                                                                                 padx=5,
                                                                                                                 pady=5)

# Create radio buttons for "Wetter" section
mode_var_wetter = tk.StringVar()
mode_var_wetter.set("Soennig")  # Default selection
label_wetter = tk.Label(root, text="Wetter:")
label_wetter.grid(row=4, column=0, padx=5, pady=5)
modes_wetter = ["Regen", "Soennig", "Schnee"]
for i, mode in enumerate(modes_wetter):
    tk.Radiobutton(root, text=mode, variable=mode_var_wetter, value=mode, command=select_mode_wetter).grid(row=4,
                                                                                                           column=i + 1,
                                                                                                           padx=5,
                                                                                                           pady=5)

# Create button to calculate output
calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_output(*acquire_input()))
calculate_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

"""
/GUI CONFIGURATION CODE
"""


def main():
    root.mainloop()  # Launches and maintains a responsive tkinter GUI window


if __name__ == "__main__":
    main()
