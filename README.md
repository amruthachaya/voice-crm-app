# Voice CRM Logger — Voice‑First PWA with Android APK

A **voice‑first Customer Relationship Management (CRM) logger** that lets sales representatives speak customer interaction details in English and automatically converts them into **structured JSON** ready to be sent to a CRM via APIs.

This solution is built as a **React (Web) Progressive Web Application (PWA)** and packaged into an **Android APK using Trusted Web Activity (TWA)** — **without using React Native**.

---

## 🔗 Live Demo

* **PWA URL:** [https://voice-crm-logger.netlify.app]

> The Android APK opens the hosted PWA using Trusted Web Activity.

---

## 🎯 Objectives

* Reduce manual CRM updates for sales teams
* Capture voice input in English
* Convert speech → text → structured JSON
* Provide installable PWA and Android APK
* Support evaluation & HITL verification

---

## 🧰 Technology Stack

### Frontend

* React (Web)
* Vite
* Web Speech API (Speech‑to‑Text)
* Progressive Web App (Service Worker + Manifest)

### Backend

* Python
* Django
* Django Rest Framework (Class‑Based APIs)

### Android Packaging

* Trusted Web Activity (Bubblewrap)
* Signed APK & AAB
* **No React Native used**

---

## ✨ Core Features

* 🎤 Voice recording (English)
* 📝 Live / final transcription
* 🧠 Structured data extraction
* 📦 Clean JSON output (displayed on UI)
* 🔌 REST API exposure
* 📱 Installable PWA
* 🤖 Android APK generated from PWA
* 📊 Evaluation dashboard (10–20 test cases)
* 🧪 HITL‑friendly outputs for verification

---

## 📄 Data Extracted

### Customer Details

* Full Name
* Phone Number
* Address
* City
* Locality

### Interaction Metadata

* Interaction Summary
* Created At (system timestamp)

### Example Voice Input

> "I spoke with customer Amit Verma today. His phone number is nine nine eight eight seven seven six six five five. He stays at 45 Park Street, Salt Lake, Kolkata. We discussed the demo and next steps."

### Example JSON Output

```json
{
  "customer": {
    "full_name": "Amit Verma",
    "phone": "9988776655",
    "address": "45 Park Street",
    "city": "Kolkata",
    "locality": "Salt Lake"
  },
  "interaction": {
    "summary": "Discussed demo and next steps",
    "created_at": "2026-01-18T11:30:00Z"
  }
}
```

---

## 🔌 API Endpoints (Backend)

| Method | Endpoint         | Description                             |
| ------ | ---------------- | --------------------------------------- |
| POST   | `/api/extract/`  | Extract structured data from transcript |
| POST   | `/api/evals/` | Run evaluation test cases               |

---

## 📊 Evaluation & HITL

* Evaluation dashboard runs **10–20 test cases**
* Displays extracted output for each test
* Results can be exported to **Excel** for HITL verification
* Designed to support future model training and improvement

---

## 📱 PWA & Android APK

### PWA

* Installable from browser
* Offline‑friendly shell
* Icons defined via Web App Manifest

### Android APK

* Generated using **Bubblewrap (Trusted Web Activity)**
* Loads the deployed PWA
* Signed APK provided as a build artifact

> APK and keystore are **not committed** to GitHub (best practice).

---

## 🚀 Running Locally

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📁 Repository Notes

* Source code only (no binaries)
* APK, keystore, database, and build artifacts are excluded
* `.gitignore` configured for clean version control

---

## 🧠 Design Decisions

* **React (Web) + PWA** chosen to meet web + mobile requirement
* **Django Rest Framework** used for robust class‑based APIs
* **Trusted Web Activity** used to generate Android APK without React Native
* Rule‑based + NLP‑assisted extraction for reliability

---

## 👤 Author

**Amrutha Chaya**

---

## 📌 Status

✅ Project complete and frozen for submission
