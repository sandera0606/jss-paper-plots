import pandas as pd
import hammock_plot

DATA_DIR="data/"
SAVE_DIR="figures/"

# data upload and column renaming
df_penguins = pd.read_csv("data_penguins.csv")
df_penguins["bill length (mm)"] = df_penguins["bill_length_mm"]
df_penguins["bill depth (mm)"] = df_penguins["bill_depth_mm"]

# variable list
var_list = ["species", "island", "bill length (mm)", "bill depth (mm)"]

label_options = {}
for var in var_list:
    label_options[var] = {'fontsize': 18}

large_label_options = {}
for var in var_list:
    large_label_options[var] = {'fontsize': 23}

# def minimal_example():
#     hammock = hammock_plot.Hammock(df_penguins)
#     ax = hammock.plot(
#         var=var_list,
#         display_figure=False,
#         missing=True,
#         save_path="figures/minimal_example.png",
#     )

def modified_layout():
    hammock = hammock_plot.Hammock(df_penguins)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        uni_vfill=0.15,
        label_options=large_label_options,
        uni_hfill=0.5,
        width=18,
        save_path="figures/minimal_example.png",
    )

def boxplots():
    hammock = hammock_plot.Hammock(df_penguins)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        uni_vfill=0.15,
        label_options=large_label_options,
        label=False,
        uni_hfill=0.4,
        save_path="figures/boxplots.png",
        display_type={"bill length (mm)": "box", "bill depth (mm)": "box"},
    )

def violinplots():
    hammock = hammock_plot.Hammock(df_penguins)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        label=False,
        uni_vfill=0.15,
        label_options=large_label_options,
        uni_hfill=0.4,
        save_path="figures/violinplots.png",
        display_type={"bill length (mm)": "violin", "bill depth (mm)": "violin"},
    )

def same_scale():
    hammock = hammock_plot.Hammock(df_penguins)
    ax = hammock.plot(
        var= var_list,
        display_figure=False,
        missing=True,
        uni_vfill=0.15,
        label_options=label_options,
        uni_hfill=0.5,
        width=18,
        save_path="figures/same_scale.png",
        same_scale=["bill length (mm)", "bill depth (mm)"],
        display_type={"bill length (mm)": "box", "bill depth (mm)": "box"},
    )

def highlighting():
    hammock = hammock_plot.Hammock(df_penguins)
    ax = hammock.plot(
        var= var_list,
        hi_var="bill length (mm)",
        hi_value="x>44.10",
        display_figure=False,
        missing=True,
        uni_vfill=0.15,
        label_options=label_options,
        uni_hfill=0.5,
        width=18,
        save_path="figures/highlighting.png",
        display_type={"bill length (mm)": "box", "bill depth (mm)": "box"},
    )

modified_layout()
boxplots()
violinplots()
same_scale()
highlighting()