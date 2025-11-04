# 🧭 User Workflow - Smart Classroom and Timetable Scheduler

## **1️⃣ Institute Onboarding (One-Time)**

**Actor:** Institute Management  
**Goal:** Register college and create system anchor  

### Flow

1. Management visits platform → fills out `Institute Name, Location, Affiliations, Contact Info, College Email Domain`  
2. Verification (manual or automated via admin panel or email domain match)  
3. On approval → system generates:  
   - `institute_id`  
   - `institute_access_table`  
   - Default **Admin user (management email)** → `user_id`, password setup  
4. Admin logs in → proceeds to setup dashboard.  

---

## **2️⃣ Admin Setup (Institute-Level Configuration)**

**Actor:** Admin (Institute-Level)  
**Goal:** Define foundation for scheduling  

### Flow

1. **Add Departments**  
   - Creates entry in `department_table`  
   - Auto-generates `department_id` + default `HOD login credentials`  
2. **Add Infrastructure (infra_table)**  
   - Classrooms + Labs → number, capacity, department, special features (smart class/lab type)  
3. **Set Time Policies**  
   - Time slots, recess breaks, working days, start/end time  
4. **Define Academic Parameters**  
   - Allowed majors, minors, electives  
   - Workload rules (e.g., max classes/day, hours/week)  
5. **Activate Departments**  
   - HOD credentials shared securely for first login  

---

## **3️⃣ Department Setup (HOD-Level Configuration)**

**Actor:** HOD / Department Admin  
**Goal:** Enter course and faculty-specific constraints  

### **Flow:**

1. **Login using department credentials**  
   - Change password (first-time)  
2. **Provide Department Info:**  
   - Course list (major, minor, elective)  
   - Subject list per course + theory/lab hours  
   - Number of enrolled students per course  
3. **Add Faculty**  
   - Faculty name, designation, primary/secondary subjects  
   - Availability (days/time slots)  
4. **Add Students**  
   - Enrollment no, opted major/minor/electives  
5. **Submit data for scheduling**  

---

## **4️⃣ Schedule Generation (AI/Constraint Engine)**

**Actor:** Scheduler (Authorized Staff or System AI)  
**Goal:** Generate optimized timetable per department  

### **Flow:**

1. Collects all constraints:  
   - Infrastructure, faculty, subjects, student data, institute rules  
2. Runs optimization algorithm (CSP / OR-Tools / GA)  
3. Generates:  
   - Base **department-wise timetable**  
   - Classroom allocations  
   - Faculty load summary  
4. Admin/HOD review → approve or regenerate alternate timetables.  

---

## **5️⃣ Publication & Integration**

**Actor:** Admin / IT Cell  
**Goal:** Share approved timetables  

### **Flow:**

- Approved timetable pushed to institute website (embed / iframe)  
- Optional: auto-export to PDF or Excel for notice boards  
- Static timetable available publicly  

---

## **6️⃣ Dynamic Update (AI/Real-time Adjustment)**

**Actor:** Faculty / Admin  
**Goal:** Handle absences or classroom unavailability  

### **Flow:**

- Faculty marks **leave/unavailability** (or detected from attendance)  
- Admin marks **room/lab unavailable**  
- AI engine suggests **rearranged timetable or swaps** (faculty substitution / class move / reschedule)  

---

## **7️⃣ Reporting & Audit**

**Actor:** Admin, HOD, Authorities  
**Goal:** Insights & compliance  

### **Flow:**

- View classroom utilization %  
- Faculty load distribution  
- Clash frequency reports  
- Export audit logs (approvals, updates)  
