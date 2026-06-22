import pandas as pd

customers = pd.read_csv("C:/Users/hp/Videos/POWER BI PROJECTS/ecom powerbi dashbprad/ecommerce dataset/Customers1.csv")
orders = pd.read_csv("C:/Users/hp/Videos/POWER BI PROJECTS/ecom powerbi dashbprad/ecommerce dataset/Orders1.csv")
products = pd.read_csv("C:/Users/hp/Videos/POWER BI PROJECTS/ecom powerbi dashbprad/ecommerce dataset/Product1.csv")

# Dataset Understanding for customers
print(customers.head(5))
customers.info()
print(customers.shape)
print(customers.describe())
print(customers.isnull().sum())
print(customers.duplicated().sum())



# Dataset Understanding for Products
print(products.head(5))
products.info()
print(products.shape)
print(products.describe())
print(products.isnull().sum())
print(products.duplicated().sum())



# Dataset Understanding for Orders
print(orders.head(5))
orders.info()
print(orders.shape)
print(orders.describe())
print(orders.isnull().sum())
print(orders.duplicated().sum())



# Data Cleaning
orders = (
    orders
    .rename(
        columns={
            "Date and time of purchase":"OrderDate",
            "Delivery time":"DeliveryDate"
        }
    )
)                                


# ---Date Conversion
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

orders["DeliveryDate"] = pd.to_datetime(orders["DeliveryDate"])


# Delivery Days
orders["delivery_days"] = (
    orders["DeliveryDate"] - orders["OrderDate"]  
).dt.days    
print(orders.head(5))



# Data Merging
ecomm_df = (
    orders
    .merge(customers,on="CustomerID",how="inner")
    .merge(products,on="ProductID",how="inner")
)


# Revenue Column
ecomm_df["total_price"] = (
    ecomm_df["Quantity"] * ecomm_df["Price"]
)
# 



# Month
ecomm_df["Month"] = (
    ecomm_df["OrderDate"]
    .dt.month_name()
)


# Weekday
ecomm_df["WeekDay"] = (
    ecomm_df["OrderDate"]
    .dt.day_name()
)


# Hour
ecomm_df["Hour"] = (
    ecomm_df["OrderDate"]
    .dt.hour
)

print(ecomm_df.head(5))




# KPI Analysis

# Total Revenue
total_revenue = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    ["total_price"].sum()
)
print(f"Total Revenue: {total_revenue}")


# Total Orders
total_orders = (
    ecomm_df["OrderID"]
    .nunique()
)
print(f"Total Orders: {total_orders}")



# Total Customers
total_customers = (
    ecomm_df["CustomerID"]
    .nunique()
)
print(f"Total Customers: {total_customers}")



# Average Order Value
delivered_orders = (
    ecomm_df[ecomm_df["Delivery Status"]=="Delivered"]
    ["OrderID"]
    .nunique()
)

avg_order_value = (
    total_revenue 
    /
    delivered_orders
)
print(f"Average Order Value: {avg_order_value}")



# Average Delivery Days
avg_delivery_days = (
    ecomm_df["delivery_days"]
    .mean()
)
print(f"Average Delivery Days: {avg_delivery_days}")


# Cancellation Rate
cancelled_orders = (
    ecomm_df[ecomm_df["Delivery Status"] == "Cancelled"]
    ["OrderID"].nunique()
)

cancellation_rate = round((cancelled_orders * 100 / total_orders),2)

print(f"Cancellation Rate: {cancellation_rate}")



# Product Analysis
# Top 10 Revenue Products
top_10_revenue_products = (
    ecomm_df[ecomm_df["Delivery Status"]=="Delivered"]
    .groupby(["ProductID","Product Name"])
    .agg(total_revenue=("total_price","sum"))
    .reset_index()
    .sort_values("total_revenue",ascending=False)
    .head(10)
)

print(f"<---Top 10 Revenue Products---> \n{top_10_revenue_products}")



# Bottom 10 Revenue Products
bottom_10_revenue_products = (
    ecomm_df[ecomm_df["Delivery Status"]=="Delivered"]
    .groupby(["ProductID","Product Name"])
    .agg(total_revenue=("total_price","sum"))
    .reset_index()
    .sort_values("total_revenue",ascending=True)
    .head(10)
)

print(f"<---Bottom 10 Revenue Products---> \n{bottom_10_revenue_products}")



# Revenue by Category
revenue_by_category = (
    ecomm_df[ecomm_df["Delivery Status"]=="Delivered"]
    .groupby("Category")
    .agg(total_revenue=("total_price","sum"))
    .reset_index()
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Revenue by Category---> \n{revenue_by_category}")



# Highest Rated Products
highest_rated_product = (
    products
    .sort_values("Rating",ascending=False)
    .head(10)
)

print(f"<---Highest Rated Products---> \n{highest_rated_product}")


# Revenue vs Rating
revenue_vs_rating = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby(["ProductID","Product Name"],as_index=False)
    .agg(total_revenue=("total_price","sum"),avg=("Rating","mean"))
    .sort_values("total_revenue",ascending=False)
    .head(10)
)

print(f"<---Revenue vs Rating---> \n{revenue_vs_rating}")


# Customer Analysis
# Top Customers
top_customer = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby(["CustomerID","First Name","Last Name"],as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
    .head(10)
)

print(f"<---Top Customers---> \n{top_customer}")



# Revenue by State
revenue_by_state = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("State",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Revenue by State---> \n{revenue_by_state}")


# Revenue by City
revenue_by_city = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("City",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Revenue by City---> \n{revenue_by_city}")



# Android vs iOS Revenue
android_vs_ios_revenue = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("Operating System",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Android vs iOS Revenue---> \n{android_vs_ios_revenue}")


# Phone Brand Analysis
phone_brand_analysis = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("Phone Brand",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Phone Brand Analysis---> \n{phone_brand_analysis}")



# Time Analysis
# Monthly Revenue Trend
ecomm_df["Month_num"] = ecomm_df["OrderDate"].dt.month

monthly_revenue_trend = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("Month_num",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("Month_num")
)

print(f"<---Monthly Revenue Trend---> \n{monthly_revenue_trend}")

# OR

ecomm_df["YearMonth"] = ecomm_df["OrderDate"].dt.to_period("M")

monthly_revenue_trend1 = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("YearMonth",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("YearMonth")
)

print(f"<---Monthly Revenue Trend---> \n{monthly_revenue_trend1}")




# Orders by Month
orders_by_month = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("YearMonth",as_index=False)
    .agg(total_orders=("OrderID","nunique"))
    .sort_values("YearMonth")
)

print(f"<---Orders by Month---> \n{orders_by_month}")


# Revenue by Weekday
revenue_by_weekday = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("WeekDay",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
)

print(f"<---Revenue by Weekday---> \n{revenue_by_weekday}")



# Revenue by Hour
revenue_by_hour = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("Hour",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("Hour")
)

print(f"<---Revenue by Hour---> \n{revenue_by_hour}")



# Peak Revenue Hour
peak_revenue_hour = (
    ecomm_df[ecomm_df["Delivery Status"] == "Delivered"]
    .groupby("Hour",as_index=False)
    .agg(total_revenue=("total_price","sum"))
    .sort_values("total_revenue",ascending=False)
    .head(1)
)

print(f"<---Peak Revenue Hour---> \n{peak_revenue_hour}")



# Monthly Growth Analysis
monthly_revenue_trend1["previous_revenue"] = (
    monthly_revenue_trend1["total_revenue"]
    .shift(1)
)

monthly_revenue_trend1["growth_pct"] = (
    monthly_revenue_trend1["total_revenue"]
    .pct_change() * 100
).round(2)

print(f"<---Monthly Growth Analysis---> \n{monthly_revenue_trend1}")



# Delivery Analysis
# Revenue Lost Due To Cancellation
revenue_lost_by_cancel_order = (
    ecomm_df[ecomm_df["Delivery Status"] == "Cancelled"]
    ["total_price"].sum()
)

print(f"Revenue Lost Due To Cancellation: {revenue_lost_by_cancel_order}")



# State-wise Cancellation Rate
state_cancellation = (
    ecomm_df[ecomm_df["Delivery Status"] == "Cancelled"]
    .groupby("State",as_index=False)
    .agg(cancel_orders=("OrderID","nunique"))
    )

total_orders = (
    ecomm_df
    .groupby("State", as_index=False)
    .agg(total_orders=("OrderID", "nunique"))
)

state_cancellation = state_cancellation.merge(
    total_orders,
    on="State",
    how="left"
)

state_cancellation["cancellation_rate"] = (
    state_cancellation["cancel_orders"] * 100
    / state_cancellation["total_orders"]
).round(2)

print(f"<---Cancellation Rate---> \n{state_cancellation}")



