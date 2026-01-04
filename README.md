# HireChain - Job Portal Platform

**Connect. Grow. Succeed.**

HireChain is a modern job portal that bridges the gap between HR professionals and job seekers. Built with Django following SOLID principles and best practices.

## 🚀 Features

### For Job Seekers
- Browse available job postings
- View detailed job descriptions
- Apply for jobs with resume upload
- User authentication and profiles
- Light/Dark mode toggle

### For Admins/HR
- Post new job openings
- View all applications in one place
- Update application statuses
- Manage applicant details
- Download resumes

## 🛠️ Technology Stack

- **Backend**: Django 6.0
- **Frontend**: HTML5, CSS3 (with CSS Variables for theming), JavaScript (ES6+)
- **Database**: SQLite (development) - easily switchable to PostgreSQL/MySQL
- **Architecture**: SOLID principles, MVT pattern

## 📁 Project Structure

```
HireChain/
├── accounts/          # User authentication & management
├── jobs/             # Job postings management
├── applications/     # Job applications handling
├── static/           # CSS, JavaScript, Images
│   ├── css/
│   │   ├── style.css      # Main styles with light/dark mode
│   │   └── admin.css      # Admin panel styles
│   ├── js/
│   │   ├── main.js        # Theme toggle, alerts, navigation
│   │   ├── jobs.js        # Job modals and applications
│   │   └── admin.js       # Admin panel functionality
│   └── images/
│       └── logo.png       # HireChain logo
├── templates/        # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── accounts/
│   ├── applications/
│   └── jobs/
└── media/           # User uploads (resumes, etc.)
```

## 🔧 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation

```powershell
# Navigate to project directory
cd D:\FriendsProjects\HireChain\HireChain

# Activate virtual environment
..\..\.vemv\Scripts\Activate.ps1

# Install dependencies (if not already done)
pip install django pillow

# Database is already migrated, but if needed:
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 4. Create Sample Data (Optional)

You can create sample jobs through the admin interface or programmatically.

### 5. Run the Server

```powershell
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## 📱 Usage Guide

### For Job Seekers:

1. **Register**: Click "Sign Up" to create an account
2. **Browse Jobs**: View available positions on the home page
3. **View Details**: Click "View Details" on any job card
4. **Apply**: Click "Apply" button (requires login)
5. **Fill Application**: Complete the form with your details and upload resume

### For Admins:

1. **Access Admin Panel**: 
   - Create admin user with `user_type='admin'` or use superuser
   - Click profile icon → "Admin Panel"
   
2. **Post New Job**:
   - Click "Post New Job" button
   - Fill in job details
   - Click "Post Job"
   
3. **Manage Applications**:
   - View all applications in the table
   - Click on any row to see applicant details
   - Update application status
   - Download resumes

## 🎨 Features Explained

### Light/Dark Mode
- Automatic theme persistence using localStorage
- Click the sun/moon icon in navbar to toggle
- CSS variables for seamless theme switching

### Responsive Design
- Mobile-first approach
- Works on all screen sizes
- Touch-friendly interfaces

### SOLID Principles Implementation

1. **Single Responsibility**: Each class/function has one job
   - Separate models for User, Job, Application
   - Dedicated views for each operation
   - Modular JavaScript classes

2. **Open/Closed**: Extends without modifying
   - CustomUser extends AbstractUser
   - Forms extend Django's base forms

3. **Liskov Substitution**: Proper inheritance
   - Models properly extend Django's base classes

4. **Interface Segregation**: Specific interfaces
   - Separate API endpoints for different data
   - Dedicated forms for different purposes

5. **Dependency Inversion**: Depend on abstractions
   - Uses Django's ORM abstractions
   - Generic views and forms

## 🔒 Security Features

- CSRF protection on all forms
- User authentication required for applications
- Admin-only access to management features
- File upload validation
- XSS protection through Django templating

## 📝 Model Structure

### CustomUser
- Extends Django's AbstractUser
- Additional fields: user_type, phone, linkedin
- Supports both job seekers and admins

### Job
- Title, company, location
- Description, requirements, responsibilities
- Active/inactive status
- Auto-generated slug

### Application
- Links user to job
- Stores applicant details
- Resume upload
- Status tracking (New, Reviewing, Interview Scheduled, Rejected)

## 🎯 API Endpoints

```
GET  /                                    # Home page with job listings
GET  /accounts/login/                     # Login page
POST /accounts/login/                     # Login action
GET  /accounts/register/                  # Registration page
POST /accounts/register/                  # Registration action
GET  /accounts/logout/                    # Logout action

GET  /api/job/<id>/                      # Get job details (AJAX)
GET  /jobs/create/                       # Create job page (admin)
POST /jobs/create/                       # Create job action (admin)

POST /applications/apply/<job_id>/       # Submit application
GET  /applications/admin/applications/   # View all applications (admin)
GET  /applications/api/application/<id>/ # Get application details (admin)
POST /applications/api/application/<id>/update-status/  # Update status (admin)
```

## 🚀 Deployment Considerations

For production deployment:

1. **Settings Updates**:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Use environment variables for `SECRET_KEY`

2. **Database**:
   - Switch to PostgreSQL or MySQL
   - Update `DATABASES` configuration

3. **Static Files**:
   - Run `python manage.py collectstatic`
   - Configure web server to serve static files

4. **Media Files**:
   - Configure cloud storage (AWS S3, etc.)
   - Or set up proper media file serving

5. **Security**:
   - Enable HTTPS
   - Configure CORS if needed
   - Set up proper file upload limits

## 🤝 Contributing

This project follows Django best practices and coding standards. When contributing:

1. Follow SOLID principles
2. Write descriptive commit messages
3. Comment complex logic
4. Test all features before committing
5. Keep CSS and JS modular

## 📄 License

This project is for educational/portfolio purposes.

## 👨‍💻 Developer

Created with ❤️ following industry best practices and SOLID principles.

---

**Happy Hiring! 🎯**
