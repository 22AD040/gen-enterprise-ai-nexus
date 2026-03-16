import streamlit as st
import pandas as pd

from utils.embeddings import generate_embeddings
from utils.cosine_similarity import similarity_search


def semantic_search_page():

    st.title("Semantic Search Engine")

    st.markdown("""
### How Semantic Search Works

Traditional keyword search matches only exact words.  
Semantic search understands **meaning and context**.

Instead of searching for identical keywords, the system converts text into **embeddings** (numerical vectors that represent meaning).

#### Processing Pipeline

• **Step 1 — Upload a dataset (CSV)**  
The dataset may contain multiple columns such as employee attributes, product information, or business metrics.

• **Step 2 — Convert each row into a full text description**  
All columns are merged into a meaningful sentence describing the row.

Example:

Employee from city 21 | Education: Graduate | Experience: 10 years | Training hours: 40

• **Step 3 — Generate embeddings**  
Each row description is converted into a numerical vector using a language model.

• **Step 4 — Convert your question into an embedding**

• **Step 5 — Compute cosine similarity**  
This measures how similar the meanings of the query and each row are.

• **Step 6 — Return the most relevant results**

#### Interpreting Similarity Scores

• **0.80 – 1.00** → Very strong semantic match  
• **0.60 – 0.79** → Relevant result  
• **0.40 – 0.59** → Moderate relevance  
• **Below 0.40** → Weak relation
""")

    file = st.file_uploader("Upload CSV Dataset", type=["csv"])

    if file is not None:

        df = pd.read_csv(file)

        st.success(f"Dataset uploaded successfully: {file.name}")

        st.subheader("Dataset Preview")

        st.dataframe(df.head())



        texts = []

        for _, row in df.iterrows():

            row_description = " | ".join(
                [f"{col}: {row[col]}" for col in df.columns]
            )

            texts.append(row_description)



        embeddings = generate_embeddings(texts)

        query = st.text_input("Ask a question about the dataset")

        if query:

            q_emb = generate_embeddings([query])[0]

            results = similarity_search(q_emb, embeddings, texts)

            st.subheader("Search Results")

            for score, text in results:

                st.markdown(f"""
### Match Found

**Similarity Score:** `{round(score,3)}`

**Row Description**

{text}

---
""")

        st.markdown("""
### Example Queries You Can Ask

• Which employees have more than 5 years experience?  
• Show employees with graduate education  
• Find employees with high training hours  
• Which employees are from city 21?
""")