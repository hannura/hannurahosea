import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import urllib


all_df = pd.read_csv("all_df.csv")


st.header("Produk dengan Penjualan Terbanyak dan Tersedikit di Brazil")

sum_order = all_df.groupby(by='product_category_name_english').order_id.nunique().sort_values(ascending=False).reset_index()
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

colors = ["#008000", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
colors1 = ["#FF0000", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="order_id", y="product_category_name_english", data=sum_order.sort_values(by="order_id", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk Penjualan Terbanyak", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x="order_id", y="product_category_name_english", data=sum_order.sort_values(by="order_id", ascending=True).head(5), palette=colors1, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk Penjualan Tersedikit", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)