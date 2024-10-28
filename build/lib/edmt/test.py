
import uuid
import pandas as pd

def generate_uuid(df, index=False, **addl_kwargs):
    """
    Adds a unique 'id' column with UUIDs to the DataFrame if there is no existing UUID-like column,
    and does not generate new UUIDs if UUIDs are already assigned.

    Parameters:
    - df (pd.DataFrame): Input DataFrame to add UUIDs to.
    - index (bool): If True, sets 'id' as the index and then resets it.

    Returns:
    - pd.DataFrame: DataFrame with the 'id' column added if no UUID-like column exists.
    """

    # Check if any column contains UUID-like values
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            if df[col].str.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$').all():
                # UUID column detected, skip creation
                print(f"Column '{col}' contains UUID-like values. Skipping UUID generation.")
                return df

    # If no UUID-like column is found, create or complete 'id' column
    if 'id' not in df.columns:
        # Generate UUIDs for all rows
        df['id'] = [str(uuid.uuid4()).lower() for _ in range(len(df))]
    else:
        # Generate UUIDs only for rows with null values in the 'id' column
        df['id'] = df['id'].apply(lambda x: x if pd.notnull(x) else str(uuid.uuid4()).lower())

    # Set index if requested
    if index:
        return df.set_index('id').reset_index()
    
    return df