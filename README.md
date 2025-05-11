
---

## **`README.md`** (Project-wide Overview)
```md
# Human-in-the-Loop AI Supervisor

## **Project Summary**
A modular AI-powered receptionist that escalates unknown queries to a human supervisor, learns responses, and improves customer interactions.

## **Tech Stack**
- **Backend:** Flask, Firebase, LiveKit
- **Frontend:** React, TailwindCSS, Framer Motion
- **Database:** Firestore (Firebase)

## **How It Works**
1. **AI answers** known questions using pre-fed business knowledge.
2. **Unanswered queries** trigger a supervisor request.
3. **Supervisors respond** via the dashboard.
4. **AI learns** from human responses and updates its knowledge base.
5. **System improves over time** with automated learning.

## **Setup Instructions**
### 1. Install Backend Dependencies
```bash
pip install -r backend/requirements.txt