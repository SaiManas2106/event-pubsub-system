# 📨 event-pubsub-system

A Pub/Sub-based event planning system in Python using RabbitMQ, Flask, and a simple HTML dashboard. The system emulates a real-world event coordination process between an **Event Host**, **Coordinator**, and multiple **Event Guests** using message queues.

---

## 📌 Project Overview

This system demonstrates a decoupled, asynchronous communication model where:

- **Host** sends an event invitation to a **Coordinator**
- **Coordinator** forwards the invitation to all **Guests**
- Each **Guest** responds with **Yes**, **No**, or **Maybe**
- **Coordinator** collects responses and sends a summary back to the **Host**
- The **Host** prints the final guest list, and the **Dashboard** displays it via Flask API

---

## ⚙️ Technologies Used

- 🐍 Python 3
- 🐇 RabbitMQ (via Docker)
- 📦 `pika` for RabbitMQ communication
- 🌐 Flask (for summary API)
- 🖥 HTML + JavaScript (for live dashboard)
- 🔄 JSON (for summary storage)
- 🎨 Styled Dashboard with vanilla CSS

---

## 🏗️ Architecture

```
+-------+        +-------------+        +--------+
| Host  | -----> | Coordinator | -----> | Guests |
+-------+        +-------------+        +--------+
     ^                  |                    |
     |                  v                    |
     +----------- Summary <------------------+
                        |
                 Flask REST API
                        |
                  HTML Dashboard
```

---

## 🧪 How to Run

### 1. 🐳 Start RabbitMQ via Docker

```bash
docker run -d --hostname event-rabbit --name event-broker \
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

> Access RabbitMQ dashboard at: [http://localhost:15672](http://localhost:15672)  
> Default user/pass: `guest` / `guest`

---

### 2. 📦 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. 🧩 Start the System (Each in a New Terminal)

```bash
# Terminal 1: Flask API
cd flask_api
python app.py
```

```bash
# Terminal 2: Coordinator
python coordinator.py
```

```bash
# Terminal 3–5: Guests
python guest.py guest1
python guest.py guest2
python guest.py guest3
```

```bash
# Terminal 6: Host
python host.py
```

---

### 4. 🖥️ View the Dashboard

```bash
cd static
python -m http.server 8000
```

Then open: [http://localhost:8000/dashboard.html](http://localhost:8000/dashboard.html)

---

## 🎯 Features

- ✅ Fully decoupled actors (Host, Coordinator, Guest)
- ✅ Uses RabbitMQ queues to simulate cloud Pub/Sub
- ✅ Randomized guest responses (Yes/No/Maybe)
- ✅ Summary saved as JSON and served via REST
- ✅ Live-updating, styled frontend dashboard

---

## 🎥 Demo Instructions (for video)

1. Show all terminal windows running (host, coordinator, 3 guests, flask)
2. Run `host.py` → observe logs and guest responses
3. Open `localhost:8000/dashboard.html` to show live summary
4. Explain message flow: Host → Coordinator → Guests → Coordinator → Host
5. Show JSON at `/summary` and explain REST/API link to frontend

---

## 💡 Design Decisions

- **RabbitMQ** was chosen for its popularity and ease of use with `pika`
- **Flask** provides a lightweight REST API for frontend access
- **Vanilla JS** keeps the frontend simple and dependency-free
- **JSON** storage ensures easy reading, writing, and parsing of summaries

---

## 🚀 Possible Future Enhancements

- 🗂 Use a database (SQLite/Postgres) instead of `summary.json`
- 📦 Package each actor as a Docker container with Docker Compose
- 🛡️ Add user authentication for Host and Guests
- 📈 Enhance dashboard with charts (e.g., Pie chart of responses)
- ☁️ Use Redis Streams, Google Pub/Sub, or AWS SNS for cloud-native version

---

## 📁 Project Structure

```
event-pubsub-system/
│
├── flask_api/
│   └── app.py              # Serves summary API
│
├── static/
│   └── dashboard.html      # Frontend dashboard
│
├── host.py                 # Publishes invitation and prints summary
├── coordinator.py          # Forwards invites & collects responses
├── guest.py                # Simulated guests (use name arg)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 📬 Contact

For questions or collaboration:  
**Masetty Sai Manas**  
📧 https://github.com/SaiManas2106

---

> _Built as part of a Full Stack Systems Programming assignment using message queues, REST APIs, and frontend integration._
