# Biomedicine

使用閱讀理解模型來對現有生醫文獻做問答，以達到檢索的目的
架構是會先將問題輸入至模型當中，接下來模型會對現有的文獻進行QA問答，最後將獲得最高的3項會傳給使用者

## Literature

現有的生醫文獻資料集
![image](https://user-images.githubusercontent.com/32485240/151514013-2b174049-f613-4d97-bd75-a8ec43d12d06.png)


## QA model

使用現有的QA model(roberta-base-squad2)來當我們的架構核心
![image](https://user-images.githubusercontent.com/32485240/151507995-0a5c9849-f009-49bc-b658-5c4c04d007b7.png)


## Interface

輸入Question以及篩選文獻的Key(避免出現無意義的QA result)，接下來就可以得到檢索結果
下面的例子的問題為＂愛滋病的療法是什麼？＂，結果回傳了最常出現的前3項
![speedup](https://user-images.githubusercontent.com/32485240/151507844-40ff2205-923b-407e-9e5c-04f2d4501b92.gif)


## Development
+ Setup virtual environment

```
python -m venv your-awesome-venv-name
source your-awesome-venv-name/bin/activate
pip install -r requirements.txt
```

+ Start Dev Server
```
uvicorn app:app --reload
```
# File Description
```
.
├── requirements.txt 
├── app.py  // 專案中的主要組件，所有頁面都在app.py下執行
├── static\js
│   └── demo.js
├── templates
│   └── demo.html  // 使用介面   
├── biomedicine.csv  // 生醫文獻(已處理)
├── train.txt  // 生醫文獻(未處理)
└── test1.py // 資料清洗
```

