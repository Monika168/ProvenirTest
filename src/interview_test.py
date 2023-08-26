import pandas as pd
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Load Data
# Import customers and purchases datasets from CSV files.
customers = pd.read_csv('/home/oem/Documents/PycharmProjects/DE_challenge/challenge/customers.csv')
purchases = pd.read_csv('/home/oem/Documents/PycharmProjects/DE_challenge/challenge/purchases.csv')

# Data Transformation
# Concatenate first_name and last_name to form a new column full_name.
# Use multiprocessing to speed up the operation.
def combine_names(row):
    """Combine the first name and last name into a full name."""
    return f"{row['first_name']} {row['last_name']}"

with Pool() as pool:
    customers['full_name'] = pool.map(combine_names, [row for _, row in customers.iterrows()])

# Categorize age into age groups (Young, Middle-aged, Senior).
def categorize_age(age):
    """Categorize age into one of the three age groups."""
    if 18 <= age <= 30:
        return 'Young'
    elif 30 < age <= 45:
        return 'Middle-aged'
    else:
        return 'Senior'

with Pool() as pool:
    customers['age_group'] = pool.map(categorize_age, customers['age'])

# Join Operation
# Merge customers and purchases data on the customer_id.
# Using an outer join to ensure no data is lost.
combined_data = pd.merge(customers, purchases, on='customer_id', how='outer')

# Analysis
# Compute the total spending for each age group.
age_group_spending = combined_data.groupby('age_group').sum()['price'].reset_index()

# Visualization
# Create a bar chart to showcase the total spending by age group.
plt.bar(age_group_spending['age_group'], age_group_spending['price'])
plt.title('Total Spending by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Spending')
plt.tight_layout()
plt.savefig('total_spending_by_age_group.png')

# Output
# Save the combined and transformed data into a CSV file.
combined_data.to_csv('combined_data.csv', index=False)
# Save the total spending by age group into another CSV file.
age_group_spending.to_csv('age_group_spending.csv', index=False)
