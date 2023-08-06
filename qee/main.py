import pandas as pd
from qee.functions import get_files_by_extension

# df.to_csv(file.replace("xls", "csv"), sep=';', index=False)
files = get_files_by_extension("./data/xls", "xls")
df0 = pd.read_excel(files[0])
df1 = pd.read_excel(files[1]).columns[2:]

print(df1)
# df.to_csv("./data/combined.csv", sep=';', index=False)
