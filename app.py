import streamlit as st
import pandas as pd

st.title("がんリスク計算ツール")

# CSVデータの読み込み
df = pd.read_csv("cancer_risk_utsunomiya.csv")

# ユーザー入力
sex = st.selectbox("性別", ["男性", "女性"])
age_group = st.selectbox("年齢層", df["年代"].unique())

# 該当データの抽出
risk_data = df[(df["性別"] == sex) & (df["年代"] == age_group)]

if not risk_data.empty:
    risk = risk_data["罹患率 (%)"].values[0]
    st.write(f"あなたのがんリスクは {risk}% です。")
else:
    st.write("データが見つかりません。")

