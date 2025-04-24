# Нийгмийн Сүлжээний Шинжилгээ  
Энэхүү төсөл нь NetworkX, Matplotlib зэрэг Python сангуудыг ашиглан SNA-г хэрэгжүүлсэн жишээг харуулж байна.  

## Орчны тохиргоо  
1. Репозиторийг хуулбарлах:  
   ```bash
   git clone https://github.com/username/social-network-analysis.git
2. Хамааралтай сангуудыг суулгах:
pip install -r requirements.txt
Ашиглах заавар
Шинжилгээний скриптийг ажиллуулах:
python scripts/analyze_network.py
---
## 3. Өгөгдөл нэмэх ба удирдах  
### 3.1. Өгөгдлийн файлуудыг байршуулах  
1. Өгөгдлийн файлуудыг (`CSV` гэх мэт) `data/` фолдерт нэмнэ.  
2. Өөрчлөлтүүдээ commit хийн push хийнэ:  
```bash
git add data/edges.csv
git commit -m "Edge лист өгөгдлийг нэмэв"
git push origin main
