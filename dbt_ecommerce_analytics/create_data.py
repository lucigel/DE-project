import pandas as pd 

df = pd.read_csv('./data.csv', encoding='ISO-8859-1')

# orders 
orders = df[['InvoiceNo', 'InvoiceDate', 'CustomerID', 'Country']].drop_duplicates()
orders = orders.rename(columns={
    'InvoiceNo': 'order_id',
    'InvoiceDate': 'order_date',
    'CustomerID': 'customer_id'
})

orders.to_csv('data/orders.csv', index=False)

# order_items
order_items = df[['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice']].copy()
order_items = order_items.rename(columns={
    'InvoiceNo': 'order_id',
    'StockCode': 'product_id'
})
order_items.to_csv('data/order_items.csv', index=False)

# products
products = df[['StockCode', 'Description']].drop_duplicates()
products = products.rename(columns={
    'StockCode': 'product_id',
    'Description': 'product_name'
})
products.to_csv('data/products.csv', index=False)

# customers
customers = df[['CustomerID', 'Country']].drop_duplicates()
customers = customers.rename(columns={
    'CustomerID': 'customer_id'
})
customers.to_csv('data/customers.csv', index=False)