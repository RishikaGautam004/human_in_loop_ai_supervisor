# System Design: Human-in-the-Loop AI Supervisor

## **Overview**
This project enables an AI receptionist to handle customer inquiries, escalate unknown queries to a human supervisor, and store learned answers.

## **Architecture**
- **AI Agent** (LiveKit) → Handles customer calls, detects unknown queries.
- **Help Requests DB** (Firebase) → Stores pending supervisor requests.
- **Supervisor UI** (React) → Allows supervisors to resolve queries.
- **Knowledge Base** → Stores resolved answers for future AI use.

## **Workflow**
1️⃣ AI receives customer call → Handles simple queries → Escalates unknowns.  
2️⃣ Supervisor reviews pending requests → Submits an answer.  
3️⃣ AI immediately follows up with the customer and updates the knowledge base.  

## **Scalability Plan**
- **Optimize Firebase queries** for large volumes (10 → 1000 requests/day).  
- **Cache frequent queries** in Redis or an alternative.  
- **Expand supervisor roles** to ensure balanced workload distribution.  

## **Next Steps**
- Implement **live call transfers** during supervisor availability.
- Expand **multi-language AI handling** for diverse customer interactions.