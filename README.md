# Daily Lecture Record System

The Daily Lecture Record System is a web-based application designed to streamline the process of recording and managing lecture-related activities within an educational institution. It caters to three types of users: faculty, Head of Department (HOD), and administrator. This system aims to facilitate efficient tracking of evaluation activities conducted during classes, management of lecture schedules, and generation of comprehensive reports.

## Key Features:

### For Faculty:
- **Record Evaluation Activities:** Faculty members can easily record various evaluation activities conducted during classes, such as assignments given, taken, and distributed.
- **View DLR History:** Faculty members have access to their Daily Lecture Record (DLR) history, allowing them to review past activities and assessments.
- 
### For Head of Department (HOD):
- **Track Reports:** HODs can efficiently track reports submitted by faculty members based on dates and sections. This feature enables effective monitoring of teaching activities across different departments and sections.
- **View Faculty Timetable:** HODs have the ability to view the timetable of individual faculty members by entering their unique ID. This feature assists in scheduling and coordination of faculty activities.
**Download DLR as PDF:** The system provides the option for faculty members to download their Daily Lecture Record in PDF format for documentation and reference purposes.

### For Administrator:
- **Manage Lecture Slots:** Administrators are responsible for managing lecture slots and allocating them to faculty members. This feature ensures proper scheduling of classes and optimal utilization of resources.
- **System Administration:** Administrators have access to system administration functionalities, allowing them to oversee user accounts, permissions, and system settings.

## Technology Stack:

- **Framework:** Django framework for developing web applications using Python.
- **Frontend:** HTML, CSS, and JavaScript for building the user interface and enhancing user experience.
- **Backend:** Python for implementing server-side logic and handling requests/responses.
- **Database:** MySQL Workbench for storing and managing application data efficiently.

## Installation:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Create your virtual environment in your pc.
5. Configure the database settings in `settings.py` file.
6. Run migrations using `python manage.py migrate`.
7. Start the development server using `python manage.py runserver`.

## Usage:

1. Faculty members can log in using their credentials and record evaluation activities during classes.
2. HODs can access reports and timetables to monitor teaching activities across departments.
3. Administrators can manage lecture slots and oversee system administration tasks.

## Support:

For any inquiries or support related to the Daily Lecture Record System, please contact [jamdadeatharva14@gmail.com].

Feel free to customize this readme according to your project's specific details and requirements.

## NOTE:
Create two superusers since the first superuser you created won't have UniqueId.
