# 🌦️ MeghaDrsti

### Conversational AI for Weather Forecasting, Alerts & Climate Intelligence

> **Understand the Sky. Make Better Decisions.**

[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react\&logoColor=black)](#)
[![Node.js](https://img.shields.io/badge/Backend-Node.js-339933?logo=node.js\&logoColor=white)](#)
[![Express.js](https://img.shields.io/badge/API-Express.js-000000?logo=express\&logoColor=white)](#)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb\&logoColor=white)](#)
[![AI](https://img.shields.io/badge/AI-LLM%20Powered-purple)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](#)

---

## 🌐 About MeghaDrsti

**MeghaDrsti** is an AI-powered conversational weather intelligence platform designed to make complex meteorological information **simple, accessible, and actionable**.

Instead of navigating multiple weather portals, forecast charts, technical datasets, and warning bulletins, users can simply ask questions in natural language and receive contextual weather insights.

### 💬 Example

> **User:** Will it rain tomorrow evening in Dhanbad?

> **MeghaDrsti:** 🌧️ Rain is likely tomorrow evening. There is a high probability of precipitation, so carrying an umbrella is recommended.

---

## 🎯 Problem Statement

Weather information is often distributed across multiple platforms, APIs, bulletins, satellite products, and forecasting systems.

For many users, especially farmers and communities in rural areas, interpreting this information can be difficult.

### MeghaDrsti aims to provide:

* 🌡️ Real-time weather information
* 🤖 Conversational AI-based weather queries
* 📍 Location-based forecasting
* 🚨 Extreme weather alerts
* 🌾 Agriculture-focused advisories
* 🌐 Multilingual weather assistance
* 🎙️ Voice-based interaction
* 📊 Historical weather & climate insights

---

# 🚀 Key Features

### 🌤️ Real-Time Weather

Access important weather parameters such as:

* Temperature
* Feels-like temperature
* Humidity
* Wind speed & direction
* Rainfall
* Precipitation probability
* UV index
* Visibility
* Sunrise & sunset

### 🤖 Conversational AI

Users can ask weather-related questions naturally:

```text
"Will it rain tomorrow?"

"How hot will it be this weekend?"

"Should I go outside today?"

"Is there any severe weather near me?"
```

MeghaDrsti interprets the user's intent and retrieves the required weather information to generate a contextual response.

### 📍 Location Intelligence

Weather information can be generated using:

* City
* State
* Country
* GPS coordinates
* User-selected locations

### 🚨 Extreme Weather Alerts

MeghaDrsti can communicate important warnings including:

* Heavy rainfall
* Thunderstorms
* Cyclones
* Strong winds
* Extreme heat


### 🌾 Agricultural Advisory

Weather information can be converted into useful agricultural recommendations related to:

* Irrigation
* Spraying
* Crop planning
* Rainfall
* Temperature
* Wind conditions

### 🌐 Multilingual Support

MeghaDrsti is designed to support multiple Indian languages, making weather intelligence accessible to a wider population.

### 🎙️ Voice Interaction

Voice-based queries can improve accessibility for:

* Rural communities
* Farmers
* Elderly users
* Users with limited literacy
* Hands-free situations

---

# 🏗️ System Architecture

```text
                         ┌─────────────────┐
                         │      USER       │
                         └────────┬────────┘
                                  │
                         Natural Language
                                  │
                                  ▼
                    ┌────────────────────────┐
                    │    React Frontend      │
                    │     Web / Mobile UI    │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │    Node.js + Express   │
                    │       Backend API       │
                    └───────────┬────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
       ┌────────────┐    ┌────────────┐    ┌────────────┐
       │ Weather    │    │ AI / LLM   │    │ Location   │
       │ APIs       │    │ Engine     │    │ Services   │
       └──────┬─────┘    └──────┬─────┘    └────────────┘
              │                 │
              └────────┬────────┘
                       ▼
              ┌──────────────────┐
              │ Data Processing  │
              │ & Validation     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ MeghaDrsti AI    │
              │ Response Engine  │
              └────────┬─────────┘
                       │
                       ▼
                  ┌─────────┐
                  │  USER   │
                  └─────────┘

                       │
                       ▼
              ┌──────────────────┐
              │     MongoDB      │
              │ Users / History  │
              │ Alerts / Data    │
              └──────────────────┘
```

---

# 🛠️ Technology Stack

| Layer          | Technology                         |
| -------------- | ---------------------------------- |
| Frontend       | React + Vite                       |
| Styling        | Tailwind CSS                       |
| Backend        | Node.js + Express.js               |
| AI             | LLM / AI APIs                      |
| Weather Data   | Weather APIs / Meteorological Data |
| Database       | MongoDB                            |
| Authentication | JWT / HTTP Cookies                 |
| Communication  | REST API / WebSocket               |
| Maps           | GIS / Map APIs                     |
| Deployment     | Docker / Cloud                     |

---

# 🔄 How MeghaDrsti Works

```text
User Query
     ↓
Natural Language Processing
     ↓
Intent & Location Detection
     ↓
Weather Data Retrieval
     ↓
Data Validation & Processing
     ↓
AI Response Generation
     ↓
Contextual Weather Advice
     ↓
User
```

### Example

```text
User:
"Will it rain tomorrow in Dhanbad?"

        ↓

Intent:
Weather Forecast

        ↓

Location:
Dhanbad

        ↓

Time:
Tomorrow

        ↓

Weather API

        ↓

AI Processing

        ↓

🌧️ Rain is likely tomorrow.
Carry an umbrella if you are going outside.
```

---

# 📸 Screenshots

> Add application screenshots to the `screenshots/` directory.

### 🏠 Dashboard

![MeghaDrsti Dashboard](./screenshots/dashboard.png)

### 🤖 AI Weather Assistant

![MeghaDrsti AI Assistant](./screenshots/chat.png)

### 🌦️ Weather Forecast

![MeghaDrsti Forecast](./screenshots/forecast.png)

### 🚨 Weather Alerts

![MeghaDrsti Alerts](./screenshots/alerts.png)

### 📱 Mobile Interface

![MeghaDrsti Mobile](./screenshots/mobile.png)

---

# 🔌 API Documentation

### Base URL

```text
/api
```

## 🌤️ Current Weather

```http
GET /api/weather/current?city=Dhanbad
```

### Response

```json
{
  "location": "Dhanbad",
  "temperature": 29,
  "humidity": 72,
  "condition": "Partly Cloudy",
  "windSpeed": 12
}
```

---

## 📅 Forecast

```http
GET /api/weather/forecast?city=Dhanbad&days=5
```

### Response

```json
{
  "location": "Dhanbad",
  "forecast": [
    {
      "date": "2026-09-11",
      "temperature": 30,
      "rainProbability": 65,
      "condition": "Rain"
    }
  ]
}
```

---

## 🤖 AI Chat

```http
POST /api/chat
```

### Request

```json
{
  "message": "Will it rain tomorrow?",
  "location": "Dhanbad"
}
```

### Response

```json
{
  "response": "Rain is likely tomorrow afternoon.",
  "confidence": 0.91
}
```

---

## 🚨 Weather Alerts

```http
GET /api/alerts?location=Dhanbad
```

### Response

```json
{
  "alerts": [
    {
      "type": "Heavy Rainfall",
      "severity": "High",
      "message": "Heavy rainfall is expected."
    }
  ]
}
```

---

# ⚙️ Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/MeghaDrsti.git

cd MeghaDrsti
```

## 2. Install Frontend

```bash
cd frontend
npm install
```

## 3. Install Backend

```bash
cd ../backend
npm install
```

## 4. Configure Environment Variables

Create a `.env` file:

```env
PORT=5000
WEATHER_API_KEY=
AI_API_KEY=
MONGODB_URI=
JWT_SECRET=
```

## 5. Run Backend

```bash
cd backend
npm run dev
```

## 6. Run Frontend

```bash
cd frontend
npm run dev
```

---

# 📁 Project Structure

```text
MeghaDrsti/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── controllers/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   └── server.js
│
├── screenshots/
│   ├── dashboard.png
│   ├── chat.png
│   ├── forecast.png
│   ├── alerts.png
│   └── mobile.png
│
├── .env.example
├── .gitignore
└── README.md
```

---

# 🔮 Future Scope

* [ ] GFS / WRF model integration
* [ ] Satellite imagery integration
* [ ] Advanced GIS visualization
* [ ] Voice assistant
* [ ] Indian regional language support
* [ ] AI-powered agricultural advisory
* [ ] Personalized weather alerts
* [ ] Push notifications
* [ ] SMS / WhatsApp alerts
* [ ] Historical climate analytics
* [ ] Mobile application
* [ ] Disaster-management dashboard

---

# 🏆 Innovation

MeghaDrsti goes beyond conventional weather applications by introducing a **conversational AI layer over meteorological information**.

```text
Meteorological Data
        +
Forecast Models
        +
Real-Time APIs
        +
AI / LLM
        +
Location Intelligence
        ↓
 ┌─────────────────────┐
 │     MEGHADRSTI       │
 │  Conversational AI   │
 └──────────┬──────────┘
            ↓
    Actionable Insights
```

### Core Value Proposition

**Complex Weather Data → Natural Conversation → Actionable Decision**

---

# 📊 Evaluation Focus

| Parameter     | MeghaDrsti Focus                    |
| ------------- | ----------------------------------- |
| Accuracy      | Reliable weather data & responses   |
| Relevance     | Context-aware AI answers            |
| Accessibility | Multilingual & voice interaction    |
| Latency       | Fast real-time responses            |
| Scalability   | Modular backend architecture        |
| Innovation    | Conversational weather intelligence |
| Impact        | Agriculture & disaster preparedness |

---

# 👥 Team MeghaDrsti

| Member        | Role                             |
| ------------- | -------------------------------- |
| **Your Name** | Team Lead / Full Stack Developer |
| **Member 2**  | AI / ML Engineer                 |
| **Member 3**  | Frontend Developer               |
| **Member 4**  | Backend Developer                |
| **Member 5**  | Data / GIS Engineer              |

---

# 🤝 Contributing

Contributions are welcome.

```bash
git checkout -b feature/new-feature

git add .

git commit -m "Add: new feature"

git push origin feature/new-feature
```

Create a Pull Request after pushing your changes.

---

# ⚠️ Disclaimer

MeghaDrsti is designed for **weather information and decision support**.

For critical situations such as cyclones, floods, extreme rainfall, and other disasters, users should always verify information through official meteorological and government authorities.

---

<div align="center">

## 🌦️ MeghaDrsti

### **Understand the Sky. Make Better Decisions.**

⭐ **Star this repository if you find the project interesting.**

</div>
