# Databricks notebook source
# MAGIC %pip install pyspark

# COMMAND ----------

# MAGIC %pip install streamlit

# COMMAND ----------

import streamlit as st
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("test") \
    .getOrCreate()

    
st.title("Databricks app")

df = spark.sql("SELECT * FROM  ai.mcp.dim_account")

# Convert to pandas (for display)
pdf = df.toPandas()

# Show in grid
st.dataframe(pdf)
