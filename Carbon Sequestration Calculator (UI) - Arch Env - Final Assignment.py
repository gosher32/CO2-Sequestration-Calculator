import tkinter as tk
from tkinter import messagebox

# Databases
tree_sequestration = {
    "Eucalyptus": 38,
    "Other Deciduous": 12,
    "Oak": 10,
    "Pine": 21,
    "Other Coniferous": 12,
}

grass_sequestration = {
    "Standard Lawn Grass": 0.403506,
    "Turf Grass": 0.11485,
    "Switch Grass": 1.121,
    "Other Native Grass": 0.7846,
}


def calculate_sequestration():
    try:
        total_sequestration = 0

        # Validate and calculate tree sequestration
        for tree, rate in tree_sequestration.items():
            num_trees = tree_entries[tree].get()
            # Check if input is numeric or empty (defaults to 0)
            if num_trees.strip() == "":
                num_trees = 0
            elif not num_trees.isdigit():
                raise ValueError(
                    f"Error - Only positive numeric inputs are accepted for {tree}.")
            else:
                num_trees = int(num_trees)

            if num_trees < 0:
                raise ValueError(
                    f"Error - Negative values are not accepted for {tree}.")
            total_sequestration += num_trees * rate

        # Validate and calculate grass sequestration
        for grass, rate in grass_sequestration.items():
            area = grass_entries[grass].get()
            # Check if input is numeric or empty (defaults to 0.0)
            if area.strip() == "":
                area = 0.0
            elif not area.replace('.', '', 1).isdigit():
                raise ValueError(
                    f"Error - Only positive numeric inputs are accepted for {grass}.")
            else:
                area = float(area)

            if area < 0:
                raise ValueError(
                    f"Error - Negative values are not accepted for {grass}.")
            total_sequestration += area * rate

        # Display result
        result_label.config(
            text=f"Total Annual CO2 Sequestration: {total_sequestration:.2f} kg")
    except ValueError as e:
        # Display custom error messages for invalid inputs
        messagebox.showerror("Input Error", str(e))
    except Exception:
        # General error message for any unexpected issues
        messagebox.showerror(
            "Input Error", "Error - Only positive numeric inputs are accepted, please try again.")


# Set up the main window
root = tk.Tk()
root.title("Carbon Sequestration Calculator")

# Colors and styles
background_color = "#F0E1C6"  # Tan Off-white (background color)
frame_color = "#F0E1C6"       # Tan off-white (frame color)
button_color = "#A7B79E"       # Sage green (accent color)
# Font set to Averia Serif Libre Bold
font_main = ("Averia Serif Libre", 12, "bold")
font_label = ("Averia Serif Libre", 10, "bold")
text_color = "#2C6B2F"         # Forest green (text color)

root.configure(bg=background_color)

# Create frames with updated frame color
tree_frame = tk.LabelFrame(root, text="Tree Sequestration",
                           font=font_main, bg=frame_color, fg=text_color, padx=10, pady=10)
tree_frame.pack(padx=10, pady=10, fill="both")

grass_frame = tk.LabelFrame(root, text="Grass Sequestration",
                            font=font_main, bg=frame_color, fg=text_color, padx=10, pady=10)
grass_frame.pack(padx=10, pady=10, fill="both")

# Tree input fields
tree_entries = {}
for tree in tree_sequestration.keys():
    row = tk.Frame(tree_frame, bg=frame_color)
    label = tk.Label(row, text=f"{tree} (Number):", font=font_label,
                     bg=frame_color, anchor="w", fg=text_color)
    entry = tk.Entry(row, font=font_label)
    tree_entries[tree] = entry
    row.pack(fill="x", padx=5, pady=2)
    label.pack(side="left", padx=5)
    entry.pack(side="right", padx=5, expand=True, fill="x")

# Grass input fields
grass_entries = {}
for grass in grass_sequestration.keys():
    row = tk.Frame(grass_frame, bg=frame_color)
    label = tk.Label(row, text=f"{grass} (m²):", font=font_label,
                     bg=frame_color, anchor="w", fg=text_color)
    entry = tk.Entry(row, font=font_label)
    grass_entries[grass] = entry
    row.pack(fill="x", padx=5, pady=2)
    label.pack(side="left", padx=5)
    entry.pack(side="right", padx=5, expand=True, fill="x")

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=font_main,
                             bg=button_color, fg="white", command=calculate_sequestration)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Total Annual CO2 Sequestration: ", font=(
    "Averia Serif Libre", 14, "bold"), bg=background_color, fg=text_color)
result_label.pack(pady=10)

# Run the application
root.mainloop()
