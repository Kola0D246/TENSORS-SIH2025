# 🧾 User Input Specification - Smart Classroom and Timetable Scheduler

## 1️⃣ Institute Registration (by Management)

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Institute Name | String | ✅ | Name of the college |
| Affiliation | String | ✅ | University or governing body |
| Location | String | ✅ | City, state |
| Institute Contact Info | String | ✅ | Official contact number/email |
| College Email Domain | String | ✅ | Used for admin verification |

---

## 2️⃣ Admin Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Department Name | String | ✅ | Name of department |
| Classroom/Lab Info | Object | ✅ | Room number, type, capacity, smart class, department |
| Time Slots | Object | ✅ | Periods, start time, end time, recess |
| Working Days | List | ✅ | e.g. Mon–Sat |
| Academic Policies | Object | ✅ | Majors, minors, electives per semester |
| Unavailability Updates | Object | ❌ | Maintenance or blocked slots |

---

## 3️⃣ HOD Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Course Name | String | ✅ | e.g., B.Tech CSE Sem 3 |
| Course Type | Enum | ✅ | Major / Minor / Elective |
| Subjects | List | ✅ | Subject name, theory/practical hours |
| Faculty Info | List | ✅ | Name, designation, primary/secondary subjects |
| Student Info | List | ✅ | Enrollment no, opted major/minor/electives |

---

## 4️⃣ Faculty Inputs

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Availability | Schedule | ✅ | Days and times faculty is available |
| Leave Information | DateRange | ❌ | Planned leave days |
| Preferred Subjects | List | ❌ | Subject preference order |

---

## 5️⃣ Student Inputs (by institute)

| Field | Type | Required | Description |
|--------|------|-----------|-------------|
| Enrollment Number | String | ✅ | Unique ID |
| Chosen Majors/Minors | List | ✅ | As per NEP 2020 flexibility |
| Elective Preferences | List | ✅ | Ranked elective choices |

---

## 🧠 Additional Inputs for Optimization

| Parameter | Description |
|------------|-------------|
| Maximum teaching hours/week | AICTE workload limit |
| Minimum gap between classes | Faculty relaxation constraint |
| Preferred Lab Times | Department-level rules |
| Weightage Settings | Admin chooses optimization priorities (faculty balance vs. room use) |
