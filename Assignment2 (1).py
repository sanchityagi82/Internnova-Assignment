# Task 1
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print("Array:")
print(arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
one_d = np.array([1,2,3,4,5])
print("One-dimensional array:")
print(one_d)
two_d = np.array([[1,2,3],[4,5,6]])
print("Two-dimensional array:")
print(two_d)

# Task 2
import numpy as np
arr = np.array([10,20,30,40,50,60])
print("First element:", arr[0])
print("Third element:", arr[2])
print("Array slicing:", arr[1:5])
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("Two-dimensional array:")
print(matrix)
print("Second row:", matrix[1])
print("Second column:", matrix[:, 1])
original = np.array([1,2,3,4,5,6])
reshaped = original.reshape(2,3)
print("Original array:")
print(original)
print("Reshaped array:")
print(reshaped)

# Task 3
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 10, 15, 20, 25])
print("Addition:", arr + arr2)
print("Subtraction:", arr - arr2)
print("Multiplication:", arr * arr2)
print("Division:", arr / arr2)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Standard Deviation:", np.std(arr))
print("Sum:", np.sum(arr))

# Task 4
import pandas as pd
series = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:")
print(series)
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya"],
    "Age": [20, 21, 22, 20],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
print("\nColumn Names:")
print(df.columns)
print("\nIndex:")
print(df.index)
df["Grade"] = ["A", "A+", "B", "A"]
print("\nUpdated DataFrame:")
print(df)


# TASK 5
import pandas as pd
df = pd.read_csv("data.csv")
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nRows and Columns:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
print(df.info())
print("\nStatistical Description:")
print(df.describe())

# Task 6
import pandas as pd
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [85, 92, 76, 88, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nName Column:")
print(df["Name"])
print("\nName and Marks:")
print(df[["Name", "Marks"]])
print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])
print("\nStudents whose age is 20:")
print(df[df["Age"] == 20])
print("\nSorted by Marks (Ascending):")
print(df.sort_values("Marks"))
print("\nSorted by Marks (Descending):")
print(df.sort_values("Marks", ascending=False))

# Task 7
import pandas as pd
import numpy as np
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha"],
    "Age": [20, 21, np.nan, 20, 23],
    "Marks": [85, np.nan, 76, 88, 95],
    "City": ["Delhi", "Noida", "Lucknow", np.nan, "Jaipur"]
}
df = pd.DataFrame(data)
print("Dataset before handling missing values:")
print(df)
print("\nMissing values:")
print(df.isnull())
print("\nCount of missing values:")
print(df.isnull().sum())
removed_df = df.dropna()
print("\nDataset after removing rows with missing values:")
print(removed_df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
print("\nDataset after filling missing values:")
print(df)


# Task 8
import pandas as pd
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Rahul", "Priya"],
    "Department": ["IT", "HR", "IT", "Sales"]
})
df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Salary": [40000, 45000, 35000, 50000]
})
merged_df = pd.merge(df1, df2, on="ID")
print("Merged DataFrame:")
print(merged_df)
df3 = pd.DataFrame({
    "ID": [5, 6],
    "Name": ["Neha", "Karan"],
    "Department": ["HR", "Sales"]
})
concatenated_df = pd.concat([df1, df3], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated_df)
grouped = merged_df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "count", "min", "max"]
)
print("\nGroupBy Analysis:")
print(grouped)
pivot = pd.pivot_table(
    merged_df,
    values="Salary",
    index="Department",
    aggfunc=["sum", "mean"]
)
print("\nPivot Table:")
print(pivot)

# Task 9
import pandas as pd
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya"],
    "Age": [20, 21, 22, 20],
    "Marks": [85, 92, 76, 88]
}
df = pd.DataFrame(data)
print("Final DataFrame:")
print(df)
df.to_csv("processed_data.csv", index=False)
print("\nData successfully exported to processed_data.csv")
check_df = pd.read_csv("processed_data.csv")
print("\nVerified exported data:")
print(check_df)

# TASK 10
import pandas as pd
import numpy as np
# -----------------------------------
# 1. Create Student Dataset
# -----------------------------------
data = {
    "Student": [
        "Aman", "Riya", "Rahul", "Priya", "Neha",
        "Karan", "Anjali", "Rohit", "Simran", "Arjun"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],
    "Department": [
        "CSE", "CSE", "ECE", "CSE", "ECE",
        "ECE", "CSE", "ECE", "CSE", "ECE"
    ],
    "Age": [20, 21, 22, 20, 23, 21, 22, 20, 23, 21],
    "Marks": [85, 92, 76, 88, 95, 81, np.nan, 74, 91, 87],
    "Attendance": [90, 95, 78, 88, 96, 82, 89, 75, 94, 91]
}
df = pd.DataFrame(data)
# -----------------------------------
# 2. Loading / Displaying Dataset
# -----------------------------------
print("STUDENT PERFORMANCE DATASET")
print(df)
# -----------------------------------
# 3. Data Inspection
# -----------------------------------
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nShape of dataset:")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nData types:")
print(df.dtypes)
print("\nDataset information:")
df.info()
print("\nStatistical summary:")
print(df.describe())
# -----------------------------------
# 4. Missing Values
# -----------------------------------
print("\nMissing values:")
print(df.isnull().sum())
# Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nDataset after handling missing values:")
print(df)
# -----------------------------------
# 5. Selecting Data
# -----------------------------------
print("\nStudent names:")
print(df["Student"])
print("\nStudent and Marks:")
print(df[["Student", "Marks"]])
# -----------------------------------
# 6. Filtering Data
# -----------------------------------
print("\nStudents scoring more than 85:")
print(df[df["Marks"] > 85])
print("\nStudents with attendance greater than 90:")
print(df[df["Attendance"] > 90])
# -----------------------------------
# 7. Sorting Data
# -----------------------------------
print("\nStudents sorted by Marks:")
print(df.sort_values("Marks", ascending=False))
# -----------------------------------
# 8. GroupBy Analysis
# -----------------------------------
print("\nAverage marks by Department:")
print(df.groupby("Department")["Marks"].mean())
print("\nMaximum marks by Department:")
print(df.groupby("Department")["Marks"].max())
print("\nMinimum marks by Department:")
print(df.groupby("Department")["Marks"].min())
# -----------------------------------
# 9. Pivot Table
# -----------------------------------
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
print("\nPivot Table:")
print(pivot)
# -----------------------------------
# 10. Useful Insights
# -----------------------------------
average_marks = np.mean(df["Marks"])
highest_marks = np.max(df["Marks"])
lowest_marks = np.min(df["Marks"])
average_attendance = np.mean(df["Attendance"])
print("\n--- KEY INSIGHTS ---")
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Attendance:", average_attendance)
top_student = df.loc[df["Marks"].idxmax(), "Student"]
print("Top Performing Student:", top_student)
best_department = df.groupby("Department")["Marks"].mean().idxmax()
print("Department with highest average marks:", best_department)
# -----------------------------------
# 11. Export Cleaned Dataset
# -----------------------------------
df.to_csv("student_performance_cleaned.csv", index=False)
print("\nCleaned dataset exported successfully!")