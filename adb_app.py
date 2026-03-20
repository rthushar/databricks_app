# Databricks notebook source
# MAGIC %pip install pyspark

# COMMAND ----------

# MAGIC %pip install streamlit

# COMMAND ----------

import streamlit as st
 
st.title("Databricks app")
 


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  *
# MAGIC FROM  ai.mcp.dim_account

# COMMAND ----------

pdf = _sqldf.toPandas()

st.dataframe(pdf)
