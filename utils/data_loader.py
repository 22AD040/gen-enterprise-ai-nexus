import pandas as pd

def load_data(file):

    df = pd.read_csv(file)

    text_columns = df.select_dtypes(include=["object"])

    texts = []

    for col in text_columns:
        texts.extend(df[col].dropna().astype(str).tolist())

    if len(texts) == 0:
        texts = df.astype(str).values.flatten().tolist()

    return texts, df