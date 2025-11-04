# 🧠 Smart Classroom and Timetable Scheduler

**Team Name:** TENSORS  
**Hackathon:** Smart India Hackathon 2025  
**Problem Statement ID:** 25028  
**Theme:** Smart Education  
**Category:** Software  

---

## 📌 Overview

> _Briefly describe the project and its purpose._  
This project aims to automate and optimize the timetable scheduling process in higher education institutions using AI and constraint satisfaction algorithms. It minimizes clashes, balances faculty workload, and maximizes classroom utilization — aligning with NEP 2020’s multidisciplinary framework.

---

## 🎯 Problem Statement

> _Explain the challenges faced by institutions that your system solves._

- Limited classrooms and overlapping schedules  
- Faculty constraints and uneven workload  
- Complex elective and multidisciplinary structures  
- Static timetables that ignore real-time changes  
- Manual, error-prone scheduling using spreadsheets  

---

## 💡 Proposed Solution

> _Summarize your approach and what makes it unique._

A **web-based platform** that:

- Collects institutional data (faculty, classrooms, subjects, student groups)  
- Generates optimized, conflict-free timetables using AI  
- Dynamically adjusts schedules based on real-time changes (faculty leave, room unavailability)  
- Provides role-based dashboards and approval workflows  

---

## 🧭 Key Features

- 🔐 Role-based Authentication (Admin, HOD, Faculty, Student)  
- 🧩 Dynamic AI-based Scheduling (Google OR-Tools / OptaPlanner)  
- 🏫 Multi-department & Multi-shift support  
- 📊 Analytics Dashboard (faculty workload, classroom utilization)  
- 🔄 Real-time timetable updates & conflict resolution  
- 📥 Export options (PDF/Excel) + Website embedding  
- 📅 Policy-compliant scheduling (AICTE norms, NEP 2020 ready)

---

## 🏗️ System Architecture

> _Describe or include an image/diagram of your architecture._

**Core Modules:**

1. Authentication & Role Management  
2. Data Management (Courses, Faculty, Students, Infra)  
3. Scheduling Engine (CSP / Genetic Algorithm)  
4. Approval Workflow  
5. Visualization & Analytics  
6. Notifications and Reports  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Tailwind CSS / Material UI, FullCalendar.js |
| **Backend** | Django / FastAPI (Python) or Node.js (Express) |
| **Database** | PostgreSQL / MySQL |
| **Scheduling Engine** | Google OR-Tools, OptaPlanner, Rule-based Logic |
| **APIs** | RESTful / GraphQL |
| **Hosting** | AWS / GCP / Azure |
| **Version Control** | Git + GitHub |

---

## 🧮 Database Schema (Simplified)

> _Add ER diagram or main tables here._

**Core Tables:**

- `login_credential`
- `institute`
- `institute_access`
- `department`
- `faculty`
- `course`
- `subject`
- `infra`
- `timeslot`
- `occupancy` (actual timetable)

**Key Constraints:**

- No duplicate `(room_id, timeslot_id)`  
- Faculty/student cannot have overlapping slots  
- Faculty ↔ subject ↔ student linkage must hold  

---

## 🔄 User Workflow

1. **Institute Registration** → Admin verification → `institute_id` generated  
2. **Admin Setup** → Departments, Infrastructure, Time Slots  
3. **HOD Setup** → Courses, Faculty, Students  
4. **AI Scheduler** → Generates base timetable (department-wise)  
5. **Review & Approval** → Admin/HOD finalize  
6. **Publication** → Embed timetable on website  
7. **Dynamic Updates** → Adjust for faculty/room changes in real-time  

---

## 🧰 Installation & Setup

> _Provide setup instructions once your repo is ready._

```bash
# Clone repository
git clone https://github.com/<your-repo>/smart-scheduler.git

# Navigate to project folder
cd smart-scheduler

# Backend setup (example: Django)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup
cd frontend
npm install
npm start
```

---

## AI / Optimization Workflow

> Describe how your scheduler logic works (briefly).

1. Base Generation: Constraint Satisfaction (Google OR-Tools)
2. Incremental Updates: OptaPlanner for localized changes
3. Minor Adjustments: Rule-based swapping system
4. Optional Learning: Reinforcement Learning for adaptive optimization

---

## 🧩 Roles & Permissions

| Role | Capabilities |
|------|--------------|
| Admin | Manage institute, approve timetables, monitor analytics |
| HOD | Enter course/faculty/student data, review timetables |
| Faculty | Update availability, view personal schedule |
| Student | View timetable, select electives (optional) |

---

## 🚀 Deployment

1. Add deployment instructions (college server or cloud).
2. Supports both local hosting (college servers) and cloud deployment (AWS/GCP/Azure).
3. The timetable can be embedded via \<iframe\> or integrated using APIs.

---

## 📊 Analytics & Reports

Classroom utilization %

Faculty workload distribution

Clash detection reports

Export as PDF/Excel

Historical version tracking

---

## ⚠️ Risks & Mitigation

| Risk | Mitigation |
|------|------------|
| Data inaccuracy | Validation & approval workflow |
| Scheduling complexity | CSP + modular rules |
| Scalability | Cloud hosting + caching |
| User resistance | Simple UI + manual override option |
| Downtime | Auto backups + redundancy |

---

## 🌍 Impact

| Stakeholder | Impact |
|-------------|--------|
| Institutions | Efficient scheduling, better infrastructure use |
| Faculty | Balanced workload, real-time updates |
| Students | Clash-free, flexible timetables |
| System | Transparent, policy-compliant, scalable |

---

## 🧪 Research & References

1. List the studies, papers, or datasets you based your work on.
2. AICTE Faculty Workload Regulations
3. Case Study: IIM Calcutta Timetabling System
4. Research: CSP & Integer Programming-based scheduling optimization
5. Tools Compared: UniTime, FET, OptaPlanner, Google OR-Tools

---

## 🧩 Future Scope

1. Integration with LMS (Moodle, Google Classroom)
2. AI-based faculty recommendation system
3. Predictive analytics for infrastructure planning
4. Mobile app version for faculty and students

---

## 🏁 Conclusion

This system offers a smart, adaptive, and scalable approach to timetable scheduling that reduces human error, optimizes resources, and supports the NEP 2020 framework of flexible multidisciplinary learning.

---

## 📜 License

This project is licensed under the **Apache License 2.0**.

You are free to:

- Use, modify, and distribute this code for personal or academic purposes
- Reference or build upon it, provided proper credit is given.

Commercial use of this software or deployment for institutional purposes requires explicit written permission from the project owner/team TENSORS.

For commercial inquiries or collaboration, contact: [your email]
