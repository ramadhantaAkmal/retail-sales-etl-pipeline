from config.settings import PRODUCTS_PATH,USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
from scripts.extract import extract_csv, extract_json
from scripts.transform import transform_data
from scripts.load import save_to_csv

if __name__ == "__main__":
    # Extract
    products_df = extract_csv(PRODUCTS_PATH)
    transactions_df = extract_csv(TRANSACTIONS_PATH)
    users_df = extract_json(USERS_PATH)
    
    #Transform
    transform_df = transform_data(products_df,transactions_df,users_df)
    
    #Load
    save_to_csv(transform_df,OUTPUT_PATH)
    print(f"ETL process is completed and file saved in {OUTPUT_PATH}")
    