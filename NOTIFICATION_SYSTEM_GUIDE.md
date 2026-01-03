# HireChain Notification System Guide

## Overview
The notification system alerts job applicants when their application status is updated by admins.

## How It Works

### 1. **For Job Seekers (Applicants)**
   - A notification bell icon appears in the navbar (top right)
   - The bell shows a badge with the count of unread notifications
   - Click the bell to view notifications
   - Notifications appear when:
     - You submit a new application
     - An admin updates your application status

### 2. **For Admins**
   - When you update an application status in the admin panel
   - The system automatically creates a notification for that applicant
   - Different messages for different statuses:
     - **New**: "Your application status has been updated to: New"
     - **Reviewing**: "Good news! Your application for [Job Title] is now being reviewed by the hiring team."
     - **Interview Scheduled**: "Congratulations! You have been selected for an interview for the [Job Title] position. The HR team will contact you soon."
     - **Rejected**: "Thank you for your interest in the [Job Title] position. Unfortunately, we have decided to move forward with other candidates."

## Testing the Notification System

### Step 1: Create a Job Seeker Account
1. Go to http://127.0.0.1:8000/
2. Click "Sign Up" (top right)
3. Fill in the registration form:
   - Username: testuser
   - Email: test@example.com
   - Password: test123456
   - User Type: Job Seeker
4. Click Register

### Step 2: Apply for a Job
1. After logging in, browse available jobs on the homepage
2. Click on any job card to view details
3. Fill in the application form:
   - Cover Letter: Write a brief message
   - Upload Resume (optional)
4. Click "Submit Application"
5. **You should see your first notification**: "Your application for [Job Title] at [Company] has been submitted successfully!"

### Step 3: Admin Updates Status
1. Log out from the job seeker account
2. Login as Admin:
   - Username: Admin123
   - Password: hirechain123
3. Click "Admin Panel" in the dropdown menu
4. You'll see the application from testuser
5. Click "View Details" on the application
6. In the status dropdown, select a different status (e.g., "Reviewing")
7. The status will be updated

### Step 4: Check Notifications
1. Log out from admin account
2. Login as testuser again
3. Look at the notification bell icon - it should show a badge with "1"
4. Click the bell to see the notification
5. The message should say: "Good news! Your application for [Job Title] is now being reviewed by the hiring team."

### Step 5: Test Different Status Updates
Repeat Step 3-4 with different statuses:
- **Interview Scheduled** - Should show congratulations message
- **Rejected** - Should show thank you message

### Step 6: Mark Notifications as Read
1. Click the "X" button on individual notifications to mark them as read
2. Or click "Mark all as read" to clear all notifications
3. The badge count should update accordingly

## Notification Features

### Auto-Refresh
- Notifications automatically refresh every 30 seconds
- No need to reload the page to see new notifications

### Real-Time Badge Update
- The badge updates immediately when you mark notifications as read
- Shows "99+" if you have more than 99 unread notifications

### Notification Details
- Each notification shows:
  - The message about status change
  - Date and time of the notification
  - Related job title

## Technical Details

### Database
- Notifications are stored in the `applications_notification` table
- Fields:
  - `user`: The applicant receiving the notification
  - `application`: The related job application
  - `message`: The notification text
  - `is_read`: Boolean flag (False for unread)
  - `created_at`: Timestamp

### API Endpoints
- `GET /applications/api/notifications/` - Get unread notifications
- `POST /applications/api/notifications/<id>/read/` - Mark one as read
- `POST /applications/api/notifications/read-all/` - Mark all as read

### Security
- Notifications are user-specific (users can only see their own)
- CSRF protection on all POST requests
- Login required for all notification endpoints

## Troubleshooting

### Notifications Not Showing?
1. Make sure you're logged in as a job seeker (not admin)
2. Check browser console for JavaScript errors (F12)
3. Verify the server is running
4. Clear browser cache and reload

### Badge Count Wrong?
- The badge only shows unread notifications
- Click "Mark all as read" and it should reset to 0

### Notification Dropdown Not Opening?
- Click directly on the bell icon
- Make sure JavaScript is enabled
- Check for console errors

## Future Enhancements (Not Yet Implemented)
- Email notifications
- Push notifications
- Notification preferences
- Notification history (including read notifications)
- Real-time updates using WebSockets
