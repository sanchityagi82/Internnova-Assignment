import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset_before_cleaning.csv")
print(df.shape, df.columns.tolist(), df.dtypes)
print(df.describe())
print(df.isnull().sum(), "duplicates:", df.duplicated().sum())

# Statistics
print("Mean:", df["Sales"].mean())
print("Median:", df["Sales"].median())
print("Mode:", df["Sales"].mode()[0])
print("Variance:", df["Sales"].var(ddof=0))
print("Standard Deviation:", df["Sales"].std(ddof=0))
print("Correlation:", df["Sales"].corr(df["Units"]))
print("Laptop probability:", (df["Product"].str.title()=="Laptop").mean())

# Cleaning
df["Region"]=df["Region"].astype(str).str.strip().str.title()
df["Product"]=df["Product"].astype(str).str.strip().str.title()
df["Customer_Rating"]=df["Customer_Rating"].fillna(df["Customer_Rating"].median())
df=df.drop_duplicates()
df=df[(df["Sales"]>0)&(df["Units"]>0)&df["Customer_Rating"].between(1,5)]
df.to_csv("dataset_after_cleaning.csv",index=False)

# IQR outliers
q1,q3=df["Sales"].quantile([.25,.75]); iqr=q3-q1
print(df[(df["Sales"]<q1-1.5*iqr)|(df["Sales"]>q3+1.5*iqr)])

# Matplotlib
plt.plot(df["Order_ID"],df["Sales"]); plt.title("Sales Trend"); plt.show()
df.groupby("Product")["Sales"].sum().plot(kind="bar"); plt.title("Sales by Product"); plt.show()
df.groupby("Product")["Sales"].sum().plot(kind="pie",autopct="%1.1f%%"); plt.title("Sales Share"); plt.ylabel(""); plt.show()
plt.hist(df["Sales"],bins=8); plt.title("Sales Distribution"); plt.show()
plt.scatter(df["Units"],df["Sales"]); plt.title("Sales vs Units"); plt.show()

# Seaborn
sns.countplot(data=df,x="Product"); plt.title("Order Count by Product"); plt.show()
sns.boxplot(data=df,x="Product",y="Sales"); plt.title("Sales by Product"); plt.show()
sns.heatmap(df[["Sales","Units","Customer_Rating","Satisfaction"]].corr(),annot=True); plt.title("Correlation Heatmap"); plt.show()
sns.pairplot(df[["Sales","Units","Customer_Rating","Satisfaction"]]); plt.show()
