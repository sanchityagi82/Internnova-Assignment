# Superstore Sales & Profitability Analysis

## Project Overview
An end-to-end data analytics project using the Sample Superstore retail dataset. The project covers data preparation, exploratory data analysis, visualization, Power BI dashboarding, business insights, and Git/GitHub workflow.

## Problem Statement
Analyze sales, profitability, customers, categories, regions and products to identify important trends and areas requiring business attention.

## Dataset Description
- Records: 9,994
- Columns: 21
- Unique Orders: 5,009
- Unique Customers: 793
- Total Sales: $2,297,200.86
- Total Profit: $286,397.02
- Profit Margin: 12.47%

## Tools Used
Python, Pandas, NumPy, Matplotlib, Power BI, DAX, Git and GitHub.

## Data Cleaning
- Converted Order Date and Ship Date to datetime.
- Checked data types.
- Checked missing values.
- Removed duplicate rows where present.
- Verified numeric fields such as Sales, Quantity, Discount and Profit.
- Prepared a cleaned CSV for analysis.

## EDA Findings
- Technology generated the highest category sales ($836,154.03).
- Technology also generated the highest category profit ($145,454.95).
- West had the highest regional sales ($725,457.82).
- Tables had the lowest sub-category profit ($-17,725.48).
- Sales and Profit showed a positive correlation, while Discount and Profit showed a negative correlation.

## Visualizations
See the `visualizations/` folder for five charts covering category sales, category profit, monthly trends, regional sales and top products.

## Power BI Dashboard
Recommended KPI cards:
1. Total Sales
2. Total Profit
3. Total Orders
4. Profit Margin

Recommended slicers: Year, Region, Category, Sub-Category and Segment.

## Business Recommendations
1. Review discounting and pricing strategies for low-profit product groups, especially Tables and Bookcases.
2. Investigate the sales and profitability drivers in high-performing regions and categories and replicate successful practices where appropriate.

## Git Workflow
Example meaningful commits:
- Add dataset and initial project structure
- Complete data cleaning and exploratory analysis
- Add Power BI dashboard and project documentation

## Conclusion
The analysis provides a clear view of sales and profitability performance and identifies product and regional areas that can be investigated further through an interactive Power BI dashboard.
