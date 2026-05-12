from load_data import load_dataset
from clean_data import clean_dataset
from visualize import create_charts

# Load dataset
df = load_dataset()

# Clean dataset
df = clean_dataset(df)

# Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

# Create charts
create_charts(df)

print("Project Completed Successfully!")