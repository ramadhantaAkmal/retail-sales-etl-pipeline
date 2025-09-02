from config.settings import PRODUCTS_PATH,USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
from scripts.extract import extract_csv, extract_json
from scripts.transform import transform_data

if __name__ == "__main__":
    # Extract
    products_df = extract_csv(PRODUCTS_PATH)
    transactions_df = extract_csv(TRANSACTIONS_PATH)
    users_df = extract_json(USERS_PATH)
    
    #Transform
    transform_df = transform_data(products_df,transactions_df,users_df)
    print(transform_df)
    