# Databricks notebook source
# MAGIC %pip install streamlit

# COMMAND ----------

import streamlit as st

st.title("Databricks app")

df = spark.sql("SELECT * FROM  ai.mcp.dim_account")

# Convert to pandas (for display)
pdf = df.toPandas()

# Show in grid
st.dataframe(pdf)
