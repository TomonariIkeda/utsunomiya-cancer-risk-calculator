import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm
import japanize_matplotlib  # 日本語化ライブラリ:w

# データの読み込み（CSVファイルを使用）
male_cancer_data_path = "man.csv"
female_cancer_data_path = "woman.csv"

# ファイルの存在チェック
if os.path.exists(male_cancer_data_path) and os.path.exists(female_cancer_data_path):
    male_df = pd.read_csv(male_cancer_data_path, encoding="utf-8")
    female_df = pd.read_csv(female_cancer_data_path, encoding="utf-8")
else:
    st.error("データファイルが見つかりません。")
    st.stop()

# 年齢階級を特定する関数
def get_age_group(age):
    age_groups = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 24), (25, 29), (30, 34),
                  (35, 39), (40, 44), (45, 49), (50, 54), (55, 59), (60, 64),
                  (65, 69), (70, 74), (75, 79), (80, 84), (85, 999)]
    for group in age_groups:
        if group[0] <= age <= group[1]:
            return f"{group[0]}-{group[1]}歳"
    return "不明"

# 累積罹患リスクの計算
def calculate_cumulative_risk(df, start_age_group, years):
    if start_age_group not in df.columns:
        return np.nan  # データがない場合はNaNを返す
    
    age_group_index = df.columns.get_loc(start_age_group)
    max_index = min(age_group_index + (years // 5), len(df.columns) - 1)
    risk_values = df.iloc[:, age_group_index:max_index].values
    cumulative_risk = 1 - np.prod(1 - risk_values / 100000, axis=1)
    return cumulative_risk * 100

# ユーザー入力
title = "がんリスク診断アプリ"
st.title(title)

# 年齢と性別の入力
age = st.number_input("年齢を入力してください", min_value=0, max_value=100, value=0, step=1)
gender = st.selectbox("性別を選択してください", ["選択してください", "男性", "女性"])

# 年齢階級の特定
age_group = get_age_group(age)

# 該当するデータを取得
selected_data = None
if gender == "男性" and age_group in male_df.columns:
    selected_data = male_df[["Unnamed: 0", age_group]].copy()
    selected_data["5年累積リスク（%）"] = calculate_cumulative_risk(male_df, age_group, 5)
    selected_data["10年累積リスク（%）"] = calculate_cumulative_risk(male_df, age_group, 10)
elif gender == "女性" and age_group in female_df.columns:
    selected_data = female_df[["Unnamed: 0", age_group]].copy()
    selected_data["5年累積リスク（%）"] = calculate_cumulative_risk(female_df, age_group, 5)
    selected_data["10年累積リスク（%）"] = calculate_cumulative_risk(female_df, age_group, 10)

# データの整形と表示
if selected_data is not None:
    selected_data.columns = ["がんの種類", "罹患率（人口10万対）", "5年累積リスク（%）", "10年累積リスク（%）"]
    st.write(f"{age_group}の{gender}のがん罹患率と累積リスク（人口10万対）:")
    st.dataframe(selected_data)
    
    # グラフの作成
    fig, ax = plt.subplots()
    selected_data.set_index("がんの種類")[["5年累積リスク（%）", "10年累積リスク（%）"]].plot(kind="bar", ax=ax)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("リスク（%）")
    plt.title(f"{age_group}の{gender}のがんリスク可視化")
    
    # ラベルの追加
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}%', (p.get_x() * 1.005, p.get_height() * 1.005))

    st.pyplot(fig)
else:
    st.write("該当するデータがありません。")

