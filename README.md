# Get started

`pip install git+https://github.com/IzumiSatoshi/scraping-toolkit.git@release`

# 概要

スクレイピングツールを作るときに、同じような部分を抽象化していきたくなったので作った。  
目標は、できるだけ頭を使わずにコーディングできるようにすること。  
{「スクレイピングツール」- 「スクレイピング」}の部分をさくっと作り、「スクレピング」の部分に注力できるようにしたい。

# 共通

- HTML 要素の指定は、xpath で統一する。
- データの受け渡しは、dataframe で統一する。
