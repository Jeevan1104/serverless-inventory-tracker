# 📦 Serverless Inventory Tracker

A fully serverless application using **AWS Lambda**, **DynamoDB**, and **API Gateway** to manage inventory items. Lightweight, fast, and cost-effective for any backendless use case.

---

## 🧠 Architecture

```plaintext
[Client] → [API Gateway] → [Lambda Functions] → [DynamoDB]
```

---

## 🛠️ Tech Stack
- Python 3.10
- AWS Lambda + API Gateway
- DynamoDB
- AWS SAM CLI

---

## 🚀 Deploy with SAM

```bash
sam build
sam deploy --guided
```

---

## 📂 Lambda Functions
- `add_item.py`
- `update_item.py`
- `delete_item.py`
- `get_inventory.py`

---

## 🔬 Sample Test

```bash
sam local invoke AddItemFunction --event events/sample_event.json
```

---

## 📬 API Endpoints

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| POST   | /add                  | Add new item         |
| PUT    | /update/{item_id}     | Update item quantity |
| DELETE | /delete/{item_id}     | Delete item          |
| GET    | /inventory            | List all items       |

---

## 🏷️ Badges

![Serverless](https://img.shields.io/badge/serverless-aws--lambda-green)
![DynamoDB](https://img.shields.io/badge/database-DynamoDB-blue)
