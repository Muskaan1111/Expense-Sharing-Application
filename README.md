Expense Sharing Backend (Splitwise Lite)

A lightweight backend system inspired by Splitwise that allows users to share group expenses, track balances, and simplify debts efficiently.  
The application is built using **Python** and **Flask**, following clean backend design principles.



## 📌 Overview

This project provides a RESTful backend for managing shared expenses among multiple users.  
It supports multiple splitting strategies, cumulative balance tracking, and automatic debt simplification using a greedy algorithm.

---

## ✨ Features Implemented

### 👤 User Management
- Create and store users in an in-memory database.
- Each user has a unique ID, name, and email.

### 💰 Flexible Expense Splitting
Supports three split types:
- **EQUAL** – Amount is divided equally among all participants.
- **EXACT** – Exact amounts are specified for each user.
- **PERCENT** – Amount is split based on percentage contribution.

### 🔄 Debt Simplification (Greedy Algorithm)
- Automatically reduces the number of transactions needed to settle balances.
- **Example:**  
  If A owes B ₹100 and B owes C ₹100 → simplified to A owes C ₹100.

### 📊 Cumulative Balance Tracking
- New expenses are aggregated with previous balances.
- Maintains net balances between all users.

### 🧾 Activity Log
- Keeps a detailed history of all expenses and settlements.

---

## 🛠 Tech Stack

- **Language:** Python 3.9+
- **Framework:** Flask (REST API)
- **Architecture:** MVC-style separation
  - `models.py` → Business logic & algorithms
  - `app.py` → API routes and controllers

---

## 📂 Project Structure

```

Expense-Sharing-Application/
│── app.py        # API routes (Controller)
│── models.py     # Business logic & algorithms
│── README.md     # Project documentation
│── .gitignore

````

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Muskaan1111/Expense-Sharing-Application.git
cd Expense-Sharing-Application
````

### 2️⃣ Run the Server

```bash
python app.py
```

📍 Server runs at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 API Endpoints & Usage

You can test the APIs using **Postman** or cURL

### 1️⃣ Create Users

POST `/user`

```bash
curl -X POST http://127.0.0.1:5000/user \
-H "Content-Type: application/json" \
-d '{"user_id":"u1","name":"Muskaan","email":"m@test.com"}'
```

```bash
curl -X POST http://127.0.0.1:5000/user \
-H "Content-Type: application/json" \
-d '{"user_id":"u2","name":"Aditya","email":"a@test.com"}'
```

```bash
curl -X POST http://127.0.0.1:5000/user \
-H "Content-Type: application/json" \
-d '{"user_id":"u3","name":"Sneha","email":"s@test.com"}'
```

### 2️⃣ Add Expense – Exact Split

**POST** `/expense`

```bash
curl -X POST http://127.0.0.1:5000/expense \
-H "Content-Type: application/json" \
-d '{
  "payer_id": "u1",
  "amount": 3000,
  "split_type": "EXACT",
  "category": "Past Debt",
  "splits": [
    {"user_id": "u2", "amount": 3000}
  ]
}'
```

---

### 3️⃣ Add Expense – Equal Split

```bash
curl -X POST http://127.0.0.1:5000/expense \
-H "Content-Type: application/json" \
-d '{
  "payer_id": "u1",
  "amount": 1500,
  "split_type": "EQUAL",
  "category": "Dinner",
  "splits": [
    {"user_id": "u1"},
    {"user_id": "u2"},
    {"user_id": "u3"}
  ]
}'
```

---

### 4️⃣ Add Expense – Percentage Split

```bash
curl -X POST http://127.0.0.1:5000/expense \
-H "Content-Type: application/json" \
-d '{
  "payer_id": "u1",
  "amount": 1000,
  "split_type": "PERCENT",
  "category": "Party",
  "splits": [
    {"user_id": "u2", "percent": 50},
    {"user_id": "u3", "percent": 50}
  ]
}'
```

---

### 5️⃣ Simplify Debts

**GET** `/simplify`

```bash
curl -X GET http://127.0.0.1:5000/simplify
```

---

### 6️⃣ View Transaction History

**GET** `/history`

```bash
curl -X GET http://127.0.0.1:5000/history
```

---

## 👩‍💻 Author

**Muskaan Choudhary**

