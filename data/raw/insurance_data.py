import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/linear-regression-project-tutorial/main/medical_insurance_cost.csv"

df = pd.read_csv(url)

df.to_csv('insurance_data.csv', index=False)
print("Dataset saved as 'insurance_data.csv'")