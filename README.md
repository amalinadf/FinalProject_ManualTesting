# 🧪 Final Project - API Testing Script Labs (Postman + Newman + GitHub Actions)

Automation API testing untuk Script Labs API (https://api-script-labs.hendri.me) menggunakan Postman Collection, dijalankan otomatis lewat Newman (CLI) dan GitHub Actions CI/CD. 🚀

## 📁 Struktur Folder
FinalProject_ManualTesting/
├── .github/
│ └── workflows/
│ └── api-test.yml # ⚙️ Workflow GitHub Actions (trigger otomatis on push/PR ke main)
├── postman/
│ ├── Assignment4_AmalinaDwiFirzanah.postman_collection.json # 📬 Postman Collection (Auth, CRUD, Data-Driven)
│ └── create_lab_test_data.csv # 📊 Data CSV untuk data-driven testing (valid, invalid, edge case)
└── README.md


## ✅ Cakupan Testing

- 🔐 **Auth**: Login valid (200) & login invalid password (401)
- 🔄 **CRUD**: Create (valid & invalid), Get All, Get By ID, Search, Update, Delete
- 🚧 **Gatekeeper check**: Get lab yang udah dihapus → 404 (membuktikan data benar-benar terhapus)
- 📈 **Data-driven testing**: 3 skenario dari CSV (valid → 201, invalid → 400, edge case 255 karakter → 201)
- ⏱️ Setiap request punya assertion: status code, response body, dan response time (< 2000ms)

## 💻 Cara Run Lokal

1. Install Node.js dan Newman:
    npm install -g newman
2. Clone repo ini, masuk ke foldernya
3. Jalankan functional test (Auth + CRUD):
   newman run postman/Assignment4_AmalinaDwiFirzanah.postman_collection.json
    --folder Auth --folder CRUD
    --env-var "demoEmail=YOUR_EMAIL"
    --env-var "demoPassword=YOUR_PASSWORD"
4. Jalankan data-driven test (CSV):
   newman run postman/Assignment4_AmalinaDwiFirzanah.postman_collection.json
    -d postman/create_lab_test_data.csv
    --folder Auth --folder DataDrivenTest
    --env-var "demoEmail=YOUR_EMAIL"
    --env-var "demoPassword=YOUR_PASSWORD"

   
## 🤖 CI/CD (GitHub Actions)

Workflow di `.github/workflows/api-test.yml` otomatis jalan setiap ada **push** atau **pull request** ke branch `main`. Credentials (`DEMO_EMAIL`, `DEMO_PASSWORD`) disimpan sebagai **GitHub Secrets** 🔒, tidak di-hardcode di file manapun.

Hasil run bisa dilihat di tab **Actions** ✅ pada repository ini.
