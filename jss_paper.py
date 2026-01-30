import pandas as pd
import hammock_plot

DATA_DIR="data/"
SAVE_DIR="figures/"

# data upload and column renaming
df_penguins = pd.read_csv(os.path.join(DATA_DIR, "data_penguins.csv"))
df_penguins["bill length (mm)"] = df_penguins["bill_length_mm"]
df_penguins["bill depth (mm)"] = df_penguins["bill_depth_mm"]
df_penguins["flipper length (mm)"] = df_penguins["flipper_length_mm"]

def minimal_example():
    var_list = ["species", "island", "bill length (mm)", "flipper length (mm)", "bill depth (mm)"]
    df = df_penguins

    hammock = hammock_plot.Hammock(df)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        save_path=os.path.join(SAVE_DIR, "minimal_example.png"),
        display_type={"bill length\n(mm)":"box", "flipper length\n(mm)": "box"},
    )

def bigger_text():
    var_list = ["species", "island", "bill length (mm)", "flipper length (mm)", "bill depth (mm)"]
    df = df_penguins

    label_options = {}

    for var in var_list:
        label_options[var] = {'fontsize': 16}

    hammock = hammock_plot.Hammock(df)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        uni_vfill=0.15,
        label_options=label_options,
        uni_hfill=0.4,
        width=20,
        save_path=os.path.join(SAVE_DIR, "bigger_text.png"),
        display_type={"bill length\n(mm)":"box", "flipper length\n(mm)": "box"},
    )
