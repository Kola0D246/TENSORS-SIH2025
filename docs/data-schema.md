# 🗄️ Data Schema

## 🌐 Universal Constraint

> All user-defined fields of two distinct rows in a table **cannot have the same value simultaneously**.

## 🌐 Data type used

1. key -> datatype for primary and foreign key. can be int or hexdec, but must be same across database
2. int -> integer
3. String -> string
4. encrypted -> password, sensitive data
5. dropdown -> has selected values only
6. timestamp -> full date time YYYY-MM-DD HH:MM:SS
7. time (hh:mm) -> hour:min

---

## 🏢 Site Data — Global

### 1. Login Credential

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| user_id | int | not null | System | Primary key, random, fixed size |
| login_id | String | not null | User | Email or username for login |
| password | encrypted | not null | User | Hashed + Salted |
| institute_id | int | not null | — | Foreign key, fixed size |
| status | dropdown | not null | System | Active / Disabled / Locked |
| created_at | timestamp | not null; constant | System | Time of account creation |
| last_login | timestamp | not null | System | Updated every login (for audit/security) |

---

### 2. Institute Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| institute_id | int | not null | System | Primary key, random, fixed size |
| name | String | not null | User | — |
| affiliation | String | not null | User | — |
| location | String | not null | User | — |
| official_communication | String | not null | User | Contact method for institute |
| institute_access_table_id | int | not null | User | — |

---

## 🏫 Data Given by College Management (Admin) — Institute Specific

### 1. Institute Access Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| user_id | int | not null | System | Foreign key, redex |
| role | dropdown | not null | User | `Admin`, `HOD`, `Faculty` |
| department_id | int | if role != (HOD or Faculty) → all or null based on institute policy | System / User | Foreign key |

---

### 2. TimeSlot

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| timeslot_id | int | not null | System | Primary key |
| day | String | not null | User | — |
| period_num | int | not null | User | — |
| start_time | time (hh:mm) | not null | User | — |
| end_time | time (hh:mm) | not null | User | — |

---

### 3. Departments Information

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| department_id | int | not null | System | Primary key, redex |
| department_name | String | not null | User | — |
| courses_table_id | int | not null | System | Auto-generate course table when department is created; foreign key |
| faculty_table_id | int | not null | System | Auto-generate faculty table when department is created; foreign key |

---

### 4. Infra Table (Classrooms / Labs)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| room_id | int | not null | System | Primary key, redex |
| department_id | String | not null | - | Foreign key, null if common use |
| type | dropdown | not null | User | `Class` (theory), `Lab` (practical) |
| capacity | int | not null | User | Maximum seating capacity |
| subject_ids | int | not null | — | For labs: related subjects |

---

### 5. Occupancy Table (Actual Timetable)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| event_id | int | not null | System | Primary key, count |
| room_id | int | not null | AI | Foreign key, default primary sorting |
| timeslot_id | int | not null | AI | Foreign key, default secondary sorting |
| subject_id | int | not null | AI | Foreign key |
| faculty_id | int | not null | AI | Foreign key |
| student_group_id | int | not null | AI | Foreign key |
| status | dropdown | not null | System | `available` / `booked` / `blocked` (e.g., maintenance) |

#### 🔒 Constraints

1. `room_id` and `timeslot_id` cannot both be identical for two rows → no duplicate slot-room entries.  
2. If two rows have the same `faculty_id` but different `room_id`, their `timeslot_id` must differ (faculty cannot be in two rooms at once).  
3. Rule #2 also applies to `student_group_id` (a student group can’t attend two classes at once).  
4. `faculty_id` and `student_group_id` must correspond to the same `subject_id`.  
5. If status is `available`, assigning valid `faculty_id`, `student_group_id`, and `subject_id` updates status → `booked`.  
   - Do not update if status is `booked` or `blocked`.  
   - When backtracking = true → reset these fields and revert status to `available`.

---

## 🧑‍🏫 Data Given by Department (HOD) — Department Specific

### 1. Course Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| course_id | int | not null | System | Primary key, redex |
| course_name | String | not null | User | — |
| course_type | dropdown | not null | User | `major` / `minor` / `elective` |
| enrolled_students | int | not null | User | — |
| subject_table_id | int | null if course_type is elective | System | Auto-generate subject table; foreign key |

---

### 2. Subject Table (One for Each Major/Minor Course)

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| subject_id | int | not null | System | Primary key, redex |
| subject_name | String | not null | User | — |
| total_theory_hours | int | not null | User | — |
| total_practical_hour | int | not null | User | — |

---

### 3. Faculty Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | System | Primary key, redex |
| faculty_name | String | not null | User | — |
| primary_subject_ids | int[] | not null | User | Main subjects taught; foreign key |
| secondary_subject_ids | int[] | not null | User | Backup subjects (temporary replacement) |
| unavailability_table_id | timestamp[] | not null | System | Linked to faculty unavailability periods |

---

### 4. Faculty Unavailability Table

| Field | Data Type | Constraint | Value By | Remark |
|-------|------------|-------------|-----------|---------|
| faculty_id | int | not null | System | Foreign key |
| timeslot_id | int | not null | User | — |
| reason | String | — | User | Reason for unavailability |

---

## 🧩 Notes

- All IDs marked as *System* generated are unique and indexed.
- dropdown values must be validated at insertion.
- Foreign keys maintain referential integrity across tables.
- Time-related fields use UTC timestamps for consistency.
