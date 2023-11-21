### 安裝套件

```bash
pip3 install -r requirements.txt
```

## 運行專案

提供Dockerfile與docker-compose.yml可供安裝測試，或是透過main.py啟動服務

## 任務：測試資料庫建立

- [x] database/schema.sql已放置table schema
- [x] database/record.sqlite已生成10筆關聯資料

## 任務：實作API Endpoint

- [x] 保戶查詢
```bash
curl http://localhost:5000/api/policyholders?code=0000000001
```
- [x] 保戶上層查詢
```bash
curl http://localhost:5000/api/policyholders/0000000002/top
```

## 資料夾說明

- app - Flask藍圖放置處
- database - 範例資料庫與table schema文件放置處
- lib - python模組放置處
- logs - 運行後生成，放置程式錯誤訊息

## 專案技術

- Flask v2.0.2
- gunicorn v21.2.0(若透過docker運行才會用到)