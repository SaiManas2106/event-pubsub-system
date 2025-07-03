
# Event Planning System using Pub/Sub (with Flask API and Dashboard)

## Overview

A simulated event system using RabbitMQ for messaging and Flask + HTML for dashboard. Features:
- Host sends invite
- Coordinator forwards invite and collects responses
- Guests respond randomly
- Summary returned to host and posted to API
- Flask serves summary via REST API
- HTML Dashboard fetches and displays guest responses

## How to Run

### 1. Start RabbitMQ via Docker

```
docker run -d --hostname event-rabbit --name event-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run Flask API

```
cd flask_api
python app.py
```

### 4. Open 5 Terminals

```
python guest.py guest1
python guest.py guest2
python guest.py guest3
python coordinator.py
python host.py
```

### 5. Open Dashboard

Navigate to `static/dashboard.html` in your browser.

## Future Improvements

- Live socket updates
- Dashboard UI upgrade
- Database storage
