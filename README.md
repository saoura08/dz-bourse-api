# DZ Bourse API

واجهة برمجية لاستخراج بيانات سوق الأوراق المالية الجزائرية من موقع [sgbv.dz](https://www.sgbv.dz/).

## Endpoint
`GET /api/stocks` - تُعيد قائمة الشركات والأسهم.

## تشغيل محلي
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
