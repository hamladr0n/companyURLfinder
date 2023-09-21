
import pandas as pd
from googlesearch import search

# Read the CSV file into a DataFrame
df = pd.read_csv('companies.csv')  # Assuming the column with company names is called 'Company'

# Create an empty list to store URLs
urls = []

# Loop through each company in the DataFrame
for company in df['Company']:
    query = f"{company} official website"
    
    # Perform Google search
    try:
        for j in search(query, num_results=1):
            urls.append(j)
            break
    except Exception as e:
        print(f"An error occurred: {e}")
        urls.append("N/A")

# Add the URLs to the DataFrame
df['Website'] = urls

# Write the DataFrame back to a new CSV file
df.to_csv('companies_with_websites.csv', index=False)
