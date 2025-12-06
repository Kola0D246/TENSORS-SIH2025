# Roadmap-frontend

## Frontend Folder Structure

```text
frontend/
│
├── public/                         # Static files
│   ├── index.html                  # Main entry point
│   ├── favicon.ico
│   └── assets/
│       ├── images/
│       ├── icons/
│       └── logos/
│
├── src/
│   ├── api/                        # API service calls
│   │   ├── instituteApi.js
│   │   ├── departmentApi.js
│   │   ├── courseApi.js
│   │   ├── facultyApi.js
│   │   ├── studentApi.js
│   │   ├── timetableApi.js
│   │   └── authApi.js
│   │
│   ├── components/                 # Reusable UI components
│   │   ├── forms/
│   │   │   ├── InstituteForm.jsx
│   │   │   ├── DepartmentForm.jsx
│   │   │   ├── CourseForm.jsx
│   │   │   ├── FacultyForm.jsx
│   │   │   ├── StudentForm.jsx
│   │   │   └── UnavailabilityForm.jsx
│   │   │
│   │   ├── tables/
│   │   │   ├── TimetableTable.jsx
│   │   │   ├── FacultyLoadTable.jsx
│   │   │   └── RoomUtilizationTable.jsx
│   │   │
│   │   ├── dialogs/
│   │   │   ├── AutofillDialog.jsx
│   │   │   └── ApprovalDialog.jsx
│   │   │
│   │   ├── inputs/
│   │   │   ├── TimePicker.jsx
│   │   │   ├── MultiSelectDropdown.jsx
│   │   │   └── CheckboxGroup.jsx
│   │   │
│   │   ├── notifications/
│   │   │   ├── Toast.jsx
│   │   │   └── Snackbar.jsx
│   │   │
│   │   └── layout/
│   │       ├── Header.jsx
│   │       ├── Sidebar.jsx
│   │       ├── Footer.jsx
│   │       └── DashboardLayout.jsx
│   │
│   ├── pages/                      # Role-based pages
│   │   ├── auth/
│   │   │   ├── LoginPage.jsx
│   │   │   └── ForgotPassword.jsx
│   │   │
│   │   ├── admin/
│   │   │   ├── AdminDashboard.jsx
│   │   │   ├── InstituteSetup.jsx
│   │   │   ├── DepartmentSetup.jsx
│   │   │   ├── InfrastructureSetup.jsx
│   │   │   └── AcademicPolicy.jsx
│   │   │
│   │   ├── hod/
│   │   │   ├── HODDashboard.jsx
│   │   │   ├── CourseSetup.jsx
│   │   │   ├── SubjectSetup.jsx
│   │   │   ├── FacultyManagement.jsx
│   │   │   ├── StudentManagement.jsx
│   │   │   └── ReviewTimetable.jsx
│   │   │
│   │   ├── faculty/
│   │   │   ├── FacultyDashboard.jsx
│   │   │   ├── MySchedule.jsx
│   │   │   ├── MarkUnavailability.jsx
│   │   │   └── PreferenceForm.jsx
│   │   │
│   │   └── student/
│   │       ├── StudentDashboard.jsx
│   │       ├── MyTimetable.jsx
│   │       └── ElectivePreferences.jsx
│   │
│   ├── context/                    # React Context / State management
│   │   ├── AuthContext.jsx
│   │   ├── TimetableContext.jsx
│   │   └── NotificationContext.jsx
│   │
│   ├── hooks/                       # Custom hooks
│   │   ├── useFetch.js
│   │   ├── useForm.js
│   │   └── useAutofill.js
│   │
│   ├── utils/                       # Utility functions
│   │   ├── validations.js
│   │   ├── constants.js
│   │   └── helpers.js
│   │
│   ├── routes/
│   │   └── AppRoutes.jsx
│   │
│   ├── styles/
│   │   ├── base.css
│   │   ├── theme.css
│   │   └── components.css
│   │
│   └── App.jsx
│
└── package.json
```

## Key Notes on This Layout

1. Role-Based Separation: Admin, HOD, Faculty, Student each has a dedicated page folder to manage complexity and permissions.
2. Forms: All entity forms (institute, department, course, faculty, student, unavailability) are in `components/forms`. These connect to API services and support validation & autofill.
3. Timetable Management: `TimetableTable.jsx` shows schedules dynamically.
4. `AutofillDialog.jsx` handles your requested “from–to” range autofill with non-working day exclusions.
5. Faculty leave & room unavailability integrate into the timetable dynamically.
6. State Management: React Context to handle login sessions, timetable data, and notifications.
7. Utilities: Validation functions, constants, and helper functions for repeated logic (e.g., day calculations, AI weight settings).
8. Reusable Components: Inputs like time pickers, multiselects, and checkboxes are standardized to maintain consistency.
9. Notifications & Dialogs: For transactional saves, approvals, and alerts.
10. Styling: Global theme + base styles, plus component-level CSS.

## Daigram