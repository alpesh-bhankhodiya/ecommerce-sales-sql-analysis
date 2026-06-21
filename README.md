# E-Commerce Sales Analysis using SQL

## Project Overview

This project analyzes an E-Commerce dataset using SQL. The objective is to extract business insights related to sales performance, customer behavior, product performance, delivery efficiency, and revenue trends.

The project uses three tables:

* Customers
* Products
* Orders

## Database 

### Customers

* CustomerID
* FirstName
* LastName
* Phone
* City
* State
* PhoneBrand
* OperatingSystem

### Products

* ProductID
* ProductName
* Category
* Price
* Rating
* NumberOfPeopleRated

### Orders

* OrderID
* CustomerID
* ProductID
* Quantity
* OrderDate
* DeliveryDate
* DeliveryStatus

## SQL Concepts Used

* Joins
* Aggregate Functions
* GROUP BY
* HAVING
* Common Table Expressions (CTEs)
* Window Functions
* Subqueries
* Date Functions
* Ranking Functions
* Business KPI Analysis

## Business Questions Solved

### Sales Analysis

* Total Revenue
* Total Orders
* Average Order Value (AOV)
* Revenue by Category
* Top 5 Products by Revenue
* Bottom 5 Products by Revenue
* Category Revenue Contribution %

### Customer Analysis

* Total Customers
* Top 10 Customers by Spending
* Customer Count by State
* Customer Count by City
* Repeat Customers
* Revenue by State
* Revenue by Operating System (Android vs iOS)

### Product Analysis

* Revenue by Product
* Highest Rated Products
* Products Above Average Revenue
* Product Revenue Ranking
* Top 3 Products within Each Category

### Time Analysis

* Monthly Revenue Trend
* Busiest Month
* Busiest Day of Week
* Peak Revenue Hour

### Delivery Analysis

* Average Delivery Time
* Cancellation Rate
* Revenue Lost Due to Cancelled Orders

## Tools Used

* PostgreSQL
* SQL


