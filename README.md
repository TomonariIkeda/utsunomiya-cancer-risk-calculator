# がんリスク診断アプリ

このリポジトリは、Streamlit を使用して開発された **がんリスク診断アプリ** です。性別と年齢を入力すると、がん罹患率や5年・10年累積リスクを計算し、視覚化します。

## 🚀 特徴
- **性別・年齢ごとのがんリスクを計算**
- **5年・10年累積リスクの算出**
- **グラフを用いた視覚化**
- **Streamlit Community Cloud での簡単なデプロイ**

## 📂 ファイル構成
```
📦 cancer-risk-app
 ┣ 📄 app.py                  # Streamlit アプリ本体
 ┣ 📄 requirements.txt        # 必要なPythonパッケージ
 ┣ 📄 man.csv                 # 男性のがん罹患率データ
 ┣ 📄 woman.csv               # 女性のがん罹患率データ
 ┣ 📄 .gitignore              # Gitで管理しないファイル
 ┣ 📄 README.md               # このファイル
```

## 🔧 必要な環境
- Python 3.10
- 必要なライブラリは `requirements.txt` に記載

## 🛠 インストール方法
### 1️⃣ 仮想環境の作成（推奨）
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 2️⃣ 必要なパッケージのインストール
```sh
pip install -r requirements.txt
```

### 3️⃣ アプリの実行
```sh
streamlit run app.py
```

➡ ブラウザで `http://localhost:8501` にアクセス！

## 🎯 使い方
1. **年齢を入力**
2. **性別を選択**
3. **がん罹患率と5年・10年累積リスクが表示される**
4. **グラフでリスクを視覚化**

## 📤 デプロイ（Streamlit Community Cloud）
1. **GitHubにリポジトリをプッシュ**
2. **[Streamlit Community Cloud](https://share.streamlit.io/) にログイン**
3. **「New App」からGitHubリポジトリを選択**
4. **デプロイボタンを押すだけ！**

## 📜 ライセンス
MIT License のもとで公開されています。自由にご利用ください。

## 🤝 貢献方法
Pull Request や Issue を歓迎します！

---
✉️ お問い合わせ: [tomonari.ikeda@gmail.com]

