import pandas as pd

# Create a dataframe of students
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22],
    'Grade': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Print the original dataframe
print("Original DataFrame:")
print(df)

# Adding a new column to the dataframe
df['Gender'] = ['Female', 'Male', 'Male']

# Print the dataframe after adding a new column
print("\nDataFrame after adding a new column (Gender):")
print(df)

# Adding a new row to the dataframe
new_row = {'Name': 'David', 'Age': 19, 'Grade': 'A', 'Gender': 'Male'}
df = df.append(new_row, ignore_index=True)

# Print the dataframe after adding a new row
print("\nDataFrame after adding a new row:")
print(df)
