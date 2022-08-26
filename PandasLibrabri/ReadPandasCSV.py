##Read cvs file using pandas
import pandas as pd

orders_path = "C:\\xerox-machine\\orders.csv"
orders_schema = [
    "order_id",
    "order_date",
    "order_customer_id",
    "order_status"
]

orders = pd.read_csv(orders_path, delimiter=',', header=None, names=orders_schema)
print(orders.head(10))

#read 2nd csv file

order_items_path = "C:\\xerox-machine\\order_items.csv"
order_items_schema = [
    "order_item_id",
    "order_item_order_id",
    "order_item_product_id",
    "order_item_quantity",
    "order_item_subtotal",
    "order_item_product_price"
]
order_items = pd.read_csv(order_items_path,
                          delimiter=',',
                          header=None,
                          names=order_items_schema
                          )
print(order_items.head(10))

# **************************Projecting data **********************************************************

print(orders.order_date)

#Project order_item_order_id and order_item_subtotal

print(order_items[['order_item_order_id', 'order_item_subtotal']])
print(order_items[order_items.order_item_order_id == 2])

# Get all the orders placed by customer_id
print(orders[orders['order_customer_id'] == 12431])

# Get all the orders which are placed by customer with id 12431 in January 2014 and status is in PENDING_PAYMENT or
# PROCESSING
print(orders[(orders.order_customer_id == 12431) &
             (orders.order_date.str.startswith('2014-01')) &
             (orders.order_status.isin(['PROCESSING', 'PENDING_PAYMENT']))
             ])

print(orders.shape)

# *************************************Performing Total Aggregations **************************************************

print(orders.count())
# Use order_items data set and compute total revenue generated for a given product_id.
print(order_items.query('order_item_product_id == 502').order_item_subtotal.sum())

# *************************** Joining data frames***********************************************************
# 1) Join orders and order_items using order_id (order_item_order_id from order_items)
os = orders.set_index('order_id').join(order_items.set_index('order_item_order_id'))
print(os)

# 2)outer join
os1 = orders.set_index('order_id').join(order_items.set_index('order_item_order_id'),how='outer').reset_index()
print(os1)

# 3) Compute Daily Revenue using orders.order_date and order_items.order_item_order_subtotal considering only COMPLETE and CLOSED orders.
orders_considered = orders.query("order_status in ('COMPLETE', 'CLOSED')")
result=orders_considered. \
    set_index('order_id'). \
    join(order_items.set_index('order_item_order_id'), how='inner'). \
    groupby('order_date')['order_item_subtotal']. \
    agg(['sum']). \
    rename(columns={'sum': 'revenue'})

print(result)

# *********************************** Performing Grouped Aggregations**************************************
# 1)Getting number of orders per date
orders_group=orders.groupby(orders['order_date'])['order_id'].count()
print(orders_group)

# 2)Get order_item_count and order_revenue for each order_id.
order_count=order_items.groupby('order_item_order_id')['order_item_subtotal'].agg(['sum','count'])
print(order_count)