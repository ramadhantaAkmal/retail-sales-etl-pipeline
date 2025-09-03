import pandas as pd

def transform_data(products_df: pd.DataFrame, transaction_df: pd.DataFrame, users_df: pd.DataFrame):
    # Dataframe Product
    products_df['currency'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int)
    
    # Dataframe Transactions
    transaction_df['transaction_date'] = pd.to_datetime(transaction_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    
    # Dataframe Users
    users_df['email'] = users_df['email'].replace("",None)
    
    # Dataframe Merge
    merge_df = transaction_df.merge(users_df, on='user_id', how='left') \
                                .merge(products_df, on='product_id', how='left')
    
    merge_df['amount'] = merge_df['quantity'] * merge_df['price']
    
    return merge_df