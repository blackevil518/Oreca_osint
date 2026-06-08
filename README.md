# 🔧 دليل استكشاف الأخطاء والمشاكل

## المشاكل الشائعة والحلول

---

## 1️⃣ مشاكل التثبيت

### الخطأ: "Command not found: python3"

**الحل:**
```bash
# تثبيت Python 3
# على Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# على Fedora/RHEL
sudo dnf install python3 python3-pip

# على macOS
brew install python3

# على Windows
# حمل من: https://www.python.org/downloads/
# وتأكد من تفعيل "Add Python to PATH"
```

---

### الخطأ: "ModuleNotFoundError: No module named 'requests'"

**الحل:**
```bash
# تثبيت المتطلبات
pip3 install -r requirements.txt

# أو تثبيت يدويًا
pip3 install requests phonenumbers
```

---

### الخطأ: "Permission denied"

**الحل:**
```bash
# إعطاء صلاحيات التنفيذ
chmod +x oreca.py

# ثم التشغيل
python3 oreca.py
```

---

## 2️⃣ مشاكل التشغيل

### الخطأ: "Connection timeout"

**السبب:** اتصال الإنترنت ضعيف أو خادم العميل غير متاح

**الحل:**
```bash
# تحقق من الاتصال بالإنترنت
ping google.com

# جرب مرة أخرى بعد بضع ثوان
python3 oreca.py

# أو استخدم VPN
```

---

### الخطأ: "Certificate verification failed"

**السبب:** مشكلة في شهادات SSL

**الحل:**
```bash
# على macOS
/Applications/Python\ 3.x/Install\ Certificates.command

# على Windows
# أعد تثبيت Python وتأكد من تفعيل
# "Install certificates.command"
```

---

### الخطأ: "Invalid URL"

**السبب:** صيغة URL خاطئة

**الحل:**
```bash
# استخدم الصيغة الصحيحة:
# ✅ www.example.com
# ✅ example.com
# ✅ https://www.example.com
# ❌ example (بدون .com)
# ❌ https:// فقط
```

---

## 3️⃣ مشاكل Termux

### الخطأ: "Termux not recognized"

**الحل:**
```bash
# تحديث Termux
apt update && apt upgrade -y

# تثبيت Python
apt install python3 python3-dev

# تثبيت git
apt install git
```

---

### الخطأ: "pip3: command not found"

**الحل:**
```bash
# تثبيت pip
apt install python3-pip

# أو
python3 -m pip install --upgrade pip
```

---

### الخطأ: "Storage permission denied"

**الحل:**
```bash
# منح الصلاحيات
termux-setup-storage

# ثم استخدم المسار
/sdcard/Download/
```

---

## 4️⃣ مشاكل Windows

### الخطأ: "Python not in PATH"

**الحل:**
```bash
# إضافة Python إلى PATH يدويًا:
# 1. اضغط Win + X → System
# 2. Advanced System Settings
# 3. Environment Variables
# 4. أضف مسار Python (C:\Users\YourName\AppData\Local\Programs\Python\Python39\)
# 5. أعد تشغيل الكمبيوتر

# أو إعادة تثبيت Python
# وتأكد من تفعيل "Add Python to PATH"
```

---

### الخطأ: "Firewall blocking"

**الحل:**
```bash
# السماح للتطبيق في جدار الحماية
# Windows Defender Firewall → Allow an app
# ابحث عن python.exe وفعّله
```

---

## 5️⃣ مشاكل الأداء

### البرنامج بطيء جدًا

**الحل:**
```bash
# تحقق من الاتصال
ping 8.8.8.8

# أغلق التطبيقات الأخرى
# قد تكون الخوادم بطيئة الآن

# جرب proxy أو VPN
```

---

### استخدام CPU عالي جدًا

**الحل:**
```bash
# هذا طبيعي أثناء ماسح المنافذ
# يمكنك إيقافه بـ Ctrl + C

# أو استخدم موارد أقل بتقليل نطاق المنافذ
```

---

## 6️⃣ مشاكل البيانات

### عدم العثور على نتائج

**السبب:** قد لا تكون البيانات موجودة

**الحل:**
```bash
# تأكد من صحة البيانات المدخلة
# استخدم بيانات حقيقية للاختبار
# جرب بريد إلكتروني معروف
```

---

### نتائج غير صحيحة

**السبب:** تحديث خوادم الخدمات أو تغيير APIs

**الحل:**
```bash
# أبلغ عن المشكلة:
# GitHub Issues
# أو Telegram: @blackevil518

# جرب مرة أخرى في وقت لاحق
```

---

## 7️⃣ مشاكل الألوان

### الألوان لا تظهر على Windows

**الحل:**
```bash
# تفعيل ANSI colors
# البرنامج يقوم بذلك تلقائيًا
# لكن إذا استمرت المشكلة:

# اذهب إلى Settings → Colors
# وفعّل "True Color (24-bit)"
```

---

## 8️⃣ طلب مساعدة إضافية

إذا لم تحل المشكلة:

1. **قدم تقرير مفصل يتضمن:**
   - نوع النظام الخاص بك
   - إصدار Python
   - الرسالة الدقيقة للخطأ
   - الخطوات التي فعلتها

2. **تواصل عبر:**
   - 📱 Telegram: [@blackevil518](https://t.me/blackevil518)
   - 🐛 GitHub Issues: [اضغط هنا](https://github.com/blackevil518/Oreca_osint/issues)

3. **معلومات مفيدة:**
   ```bash
   # احصل على معلومات النظام
   python3 -c "import platform; print(platform.platform())"
   python3 --version
   pip3 --version
   ```

---

## ℹ️ نصائح عامة

✅ تحقق دائمًا من الاتصال بالإنترنت  
✅ استخدم أحدث إصدار من البرنامج  
✅ حدّث Python والمكتبات بانتظام  
✅ جرّب على جهاز مختلف إن أمكن  
✅ اقرأ رسائل الخطأ بعناية  
✅ أغلق VPN إذا كان يسبب مشاكل  
✅ استخدم DNS عام (8.8.8.8 أو 1.1.1.1)  

---

**آخر تحديث:** 2024-06-08
