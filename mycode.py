import pandas as pd
import os

## create a sample DataFrame with column names  
data = [
    {"id": 1, "name": "Aarav", "age": 21, "city": "Delhi"},
    {"id": 2, "name": "Ishita", "age": 22, "city": "Mumbai"},
    {"id": 3, "name": "Kabir", "age": 20, "city": "Bangalore"},
    {"id": 4, "name": "Meera", "age": 23, "city": "Hyderabad"},
    {"id": 5, "name": "Rohan", "age": 19, "city": "Chennai"},
    {"id": 6, "name": "Sneha", "age": 24, "city": "Pune"},
    {"id": 7, "name": "Yash", "age": 22, "city": "Ahmedabad"},
    {"id": 8, "name": "Diya", "age": 21, "city": "Kolkata"},
    {"id": 9, "name": "Arjun", "age": 23, "city": "Jaipur"},
    {"id": 10, "name": "Simran", "age": 20, "city": "Lucknow"}
]



df=pd.DataFrame(data)


## Ennsure the 'data' directory exists at root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)  ## if already a file exists with this name , then it donot overwrites it  

# Define the path
file_path=os.path.join(data_dir,'sample_data.csv')



## Add new row to df for V2
new_row_loc={"id": 11, "name": "Palak", "age": 19, "city": "Jaipur"}
df.loc[len(df.index)]=new_row_loc

# Save the Dataframe to csv file , including column names
df.to_csv(file_path,index=False)

print(f'CSV file saved to {file_path}')
