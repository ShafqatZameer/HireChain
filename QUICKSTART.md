# HireChain - Quick Start Guide

## 🚀 Get Started in 3 Minutes!

### Step 1: Start the Server

```powershell
# Navigate to project directory
cd D:\FriendsProjects\HireChain\HireChain

# Make sure virtual environment is activated
# (Look for (.vemv) at the beginning of your prompt)

# Run the development server
python manage.py runserver
```

### Step 2: Create Admin Account

Open a **new terminal** and run:

```powershell
cd D:\FriendsProjects\HireChain\HireChain
python manage.py createsuperuser
```

Enter:
- Username: `admin`
- Email: `admin@hirechain.com`
- Password: (your choice, minimum 8 characters)

### Step 3: Access the Application

Open your browser and visit:
- **Home Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🎯 Testing the Application

### Test as Job Seeker:

1. Visit http://127.0.0.1:8000/
2. Click "Sign Up" (top right)
3. Create an account
4. Browse jobs on the home page
5. Click "View Details" on any job
6. Click "Apply" and fill out the form

### Test as Admin:

1. **Method 1 - Update existing user:**
   - Login to Django Admin: http://127.0.0.1:8000/admin/
   - Click "Users"
   - Click on your username
   - Change "User type" to "Admin"
   - Save

2. **Method 2 - Use superuser:**
   - Superusers automatically have admin access
   - Just login with the superuser credentials

3. **Access Admin Features:**
   - Click your profile icon → "Admin Panel"
   - View all applications
   - Click "Post New Job" to create job postings
   - Click on any applicant row to see details
   - Update application status

## 🎨 Features to Try

### Theme Toggle
- Click the sun/moon icon in the navbar
- Watch the entire site switch between light and dark mode
- Theme preference is saved automatically

### Job Search
- Use the search bar on the home page
- Search by keywords, company, or location
- Results filter in real-time

### Application Management
- As admin, click on any applicant row
- View complete details including resume
- Update status (New → Reviewing → Interview Scheduled)
- Download resumes by checking the box

## 📊 Sample Data

The database already contains 4 sample jobs:
- Software Specialist at Innovate Corp
- Global Tech at Global Tech
- Project Manager at Creative Solutions
- Marketing Specialist at Innovate Corp

## 🔧 Common Commands

```powershell
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Add more sample jobs
python manage.py populate_jobs

# Access Python shell
python manage.py shell

# Make database changes
python manage.py makemigrations
python manage.py migrate
```

## 🐛 Troubleshooting

### Server won't start?
```powershell
# Make sure you're in the right directory
cd D:\FriendsProjects\HireChain\HireChain

# Check if virtual environment is activated
# You should see (.vemv) in your prompt
```

### Can't access admin panel?
- Make sure you created a superuser
- Or set user_type to "Admin" for regular users

### Static files not loading?
```powershell
# Collect static files
python manage.py collectstatic --noinput
```

### Database errors?
```powershell
# Reset database (WARNING: Deletes all data)
del db.sqlite3
python manage.py migrate
python manage.py populate_jobs
python manage.py createsuperuser
```

## 📱 URLs Quick Reference

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Register | http://127.0.0.1:8000/accounts/register/ |
| Admin Applications | http://127.0.0.1:8000/applications/admin/applications/ |
| Post Job | http://127.0.0.1:8000/jobs/create/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

## 🎓 Project Structure Overview

```
HireChain/
├── accounts/         # User authentication (login, register, logout)
├── jobs/            # Job postings (list, detail, create)
├── applications/    # Job applications (apply, manage, update)
├── static/          # CSS, JavaScript, Images
├── templates/       # HTML files
└── media/          # Uploaded files (resumes)
```

## ✨ Key Features

✅ User Authentication (Register/Login/Logout)
✅ Job Browsing with Search
✅ Job Details Modal
✅ Application Submission with Resume Upload
✅ Admin Panel for Application Management
✅ Job Posting Form for Admins
✅ Application Status Updates
✅ Light/Dark Mode Toggle
✅ Responsive Design
✅ Real-time Search
✅ SOLID Principles Implementation

---

**Need help?** Check the main README.md for detailed documentation!

**Happy Testing! 🚀**
