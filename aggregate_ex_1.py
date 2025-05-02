import pandas as pd
import os

def aggregate_data(region_file, transaction_file, output_file):
    """
    Aggregates transaction data by city, state, and region code using reference region data.

    Args:
        region_file (str): Path to the region dimension CSV file.
        transaction_file (str): Path to the transaction fact CSV file.
        output_file (str): Path to save the aggregated output CSV file.

    Returns:
        None
    """
    try:
        # Load region dimension data
        if not os.path.exists(region_file):
            raise FileNotFoundError(f"Region file not found: {region_file}")
        region_df = pd.read_csv(region_file)
        if region_df.empty:
            raise ValueError("Region file is empty.")
        
        # Load transaction fact data
        if not os.path.exists(transaction_file):
            raise FileNotFoundError(f"Transaction file not found: {transaction_file}")
        transaction_df = pd.read_csv(transaction_file)
        if transaction_df.empty:
            raise ValueError("Transaction file is empty.")
        
        # Merge the two datasets on city_cd
        merged_df = pd.merge(transaction_df, region_df, on="city_cd", how="inner")
        
        # Perform aggregation
        aggregated_df = merged_df.groupby(['city_cd', 'state_cd', 'Reg_cd'], as_index=False).agg({
            'trans_amt': 'sum'
        })
        
        # Save the aggregated data to a CSV file
        aggregated_df.to_csv(output_file, index=False)
        print(f"Aggregated data saved to {output_file}")
    
    except FileNotFoundError as fnf_error:
        print(f"File error: {fnf_error}")
    except ValueError as val_error:
        print(f"Value error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    region_file = "region_dimension.csv"
    transaction_file = "daits_trans_fact.csv"
    output_file = "aggregated_output.csv"
    aggregate_data(region_file, transaction_file, output_file)