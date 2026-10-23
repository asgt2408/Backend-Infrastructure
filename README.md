# 🚗 Uber Backend Infrastructure — FastAPI

A microservices-based ride-sharing backend inspired by Uber, built using **FastAPI, Python, MySQL, SQLAlchemy, and JWT authentication**.

The project focuses on advanced backend engineering concepts, including service-to-service communication, database transaction management, concurrency control, authentication, and scalable infrastructure design.

The system is organized into independent backend services, each responsible for a specific domain. Services communicate through REST APIs, keeping business logic modular and service responsibilities clearly separated.

## 🚀 Features

### 👤 User Service
- User registration and login
- JWT-based authentication and authorization
- Secure password hashing using bcrypt
- User profile management
- Protected API endpoints

### 🚖 Driver Service
- Driver registration and management
- Driver availability tracking
- Online/offline status management
- Driver status retrieval
- Driver availability updates during ride assignment and completion

### 🛣️ Ride Service
- Ride creation and request management
- Ride acceptance by drivers
- Ride lifecycle management
- Ride status transitions: `REQUESTED → ACCEPTED → STARTED → COMPLETED`
- Driver assignment and ride tracking
- Ride completion and ride history management
- Conditional database updates to prevent multiple drivers from accepting the same ride

### 🌐 API Gateway
- Centralized entry point for client requests
- Request forwarding to backend microservices
- HTTP-based service communication
- Centralized routing across service endpoints

### 💳 Payment Service
- Payment service module planned for payment processing
- Payment history management planned

## 🏗️ Architecture

The backend follows a service-oriented architecture with separate FastAPI applications.

| Component | Port | Responsibility |
|---|---:|---|
| API Gateway | 8000 | Routes client requests to backend services |
| Driver Service | 8002 | Driver data and availability management |
| Ride Service | Configurable | Ride requests, assignment, and lifecycle |
| User Service | Configurable | Authentication, profiles, and user management |
| Payment Service | Configurable | Payment processing and payment records |

*Note: Configure ports according to the actual service startup commands. If port 8000 currently runs the ride service directly, update the table when the API Gateway is deployed separately.*

## 🧰 Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Password Security:** bcrypt
- **Inter-service Communication:** HTTPX
- **API Documentation:** Swagger UI / OpenAPI
- **Server:** Uvicorn
- **Version Control:** Git and GitHub

## 🔄 Ride Lifecycle

1. A user requests a ride.
2. The ride service creates a ride with `REQUESTED` status.
3. A driver attempts to accept the ride.
4. The ride service checks driver availability through the driver service.
5. The ride is assigned and its status changes to `ACCEPTED`.
6. The ride starts and its status changes to `STARTED`.
7. When the trip ends, the ride status changes to `COMPLETED`.
8. The driver service updates the driver's availability.

## 🧠 Backend Engineering Focus

The project is also a practical environment for exploring production-oriented backend concepts:

- **Microservices:** Service boundaries and independent responsibilities
- **Concurrency:** Preventing duplicate ride assignments
- **Consistency:** Handling failures across the ride and driver services
- **Resilience:** HTTP timeouts and service error handling
- **Security:** Token validation and protected endpoints
- **Observability:** Structured logging and request tracing
- **Scalability:** Stateless APIs, database optimization, and service deployment
- **Cloud and DevOps:** Containerization, CI/CD, infrastructure automation, and cloud deployment

## 📁 Project Structure

```text
app1/
├── user_service/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes/
├── driver_service/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes/
├── ride_service/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes/
├── api_gateway/
│   └── main.py
└── README.md
```



## 🎯 Project Goal

The goal is to evolve this backend beyond basic CRUD APIs into a reliable, observable, and scalable microservices system.

The emphasis is on understanding **why architectural decisions matter, how services behave under failure, how concurrent requests are handled, and how backend systems are deployed and operated in cloud environments.**
