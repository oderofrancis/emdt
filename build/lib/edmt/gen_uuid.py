
import uuid
import pandas as pd

def generate_uuid(df, index=False):
    """
    Adds a unique 'id' column with UUIDs to the DataFrame if no existing UUID-like column is found.
    Does not generate new UUIDs if UUIDs are already assigned in an 'id' column.

    Args:
        df (pd.DataFrame): The DataFrame to which UUIDs will be added.
        index (bool): If True, sets 'id' as the index and then resets it as a column.

    Returns:
        pd.DataFrame: DataFrame with an 'id' column added if no UUID-like column exists.
    Raises:
        ValueError: If 'df' is not a DataFrame or if it's empty.
    """

    # Validate input DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    if df.empty:
        raise ValueError("DataFrame is empty. Cannot generate UUIDs for an empty DataFrame.")

    # Define UUID pattern
    uuid_pattern = r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'

    # Check if any column contains UUID-like values
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]) and df[col].str.match(uuid_pattern).all():
            print(f"Column '{col}' contains UUID-like values. Skipping UUID generation.")
            return df

    # Add or update 'id' column with UUIDs
    if 'id' not in df.columns:
        df['id'] = [str(uuid.uuid4()).lower() for _ in range(len(df))]
    else:
        df['id'] = df['id'].apply(lambda x: x if pd.notnull(x) else str(uuid.uuid4()).lower())

    # Set 'id' as index if requested
    if index:
        df = df.set_index('id').reset_index()

    return df