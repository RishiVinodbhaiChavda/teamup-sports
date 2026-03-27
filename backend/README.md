<<<<<<< HEAD
# TeamUp Sports - Python Backend

A Flask-based REST API for the TeamUp Sports platform.

## Setup

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- `GET /api/health` - Check if API is running

### Authentication
- `POST /api/auth/register` - Create account
- `POST /api/auth/login` - Login (returns JWT)
- `POST /api/auth/send-otp` - Send OTP
- `POST /api/auth/verify-otp` - Verify OTP
- `GET /api/auth/me` - Get current user

### Users
- `GET /api/users/me` - Get profile
- `PUT /api/users/me` - Update profile
- `POST /api/users/me/picture` - Upload picture
- `GET /api/users/me/history` - Match history
- `GET /api/users/<id>` - Public profile

### Matches
- `GET /api/matches` - List matches (with filters)
- `POST /api/matches` - Create match
- `GET /api/matches/<id>` - Match details
- `PUT /api/matches/<id>` - Update match
- `DELETE /api/matches/<id>` - Delete match
- `POST /api/matches/<id>/join` - Request to join
- `GET /api/matches/<id>/requests` - View requests

### Join Requests
- `GET /api/requests/my` - My requests
- `PUT /api/requests/<id>/approve` - Approve
- `PUT /api/requests/<id>/reject` - Reject
- `DELETE /api/requests/<id>/cancel` - Cancel

## Demo OTP
Use code `123456` for OTP verification.

## Database
SQLite database is created automatically as `teamup.db`.
=======
# TeamUp Sports

A sports team matching platform to connect players, create matches, and organize games.

## 🚀 Access the Application

### Frontend (User Interface)
**http://localhost:5500**

### Backend (API Server)
**http://localhost:5000**

### API Health Check
**http://localhost:5000/api/health**

## ✅ Email OTP System - WORKING!

The OTP email verification system is **fully functional**:
- ✅ Emails sent via Gmail SMTP (teamupsports1845@gmail.com)
- ✅ Beautiful HTML email template with 6-digit OTP
- ✅ Secure TLS encryption
- ✅ 5-minute expiration
- ✅ OTP also printed in backend console for testing
- ✅ Resend functionality available

**Check `EMAIL_WORKING.md` for complete details.**

## ✨ Features

- User registration & authentication (Email/Password + Google OAuth)
- **Email OTP Verification** - Secure 6-digit codes sent to user's mailbox
- Create and manage sports matches
- Browse and filter matches by sport, location, date
- Join request system with captain approval
- Credit score system based on attendance
- Geolocation-based match filtering
- Profile management with match history
- Support for 8 sports: Cricket, Football, Basketball, Badminton, Tennis, Volleyball, Hockey, Kabaddi

## 🔐 Email Verification

When users register:
1. Enter email address and click "Verify"
2. Receive 6-digit OTP in email (1-30 seconds)
3. Enter OTP code in registration form
4. Complete registration

**Note**: Check spam folder if email doesn't arrive. OTP is also printed in backend console.

## 🛠️ Tech Stack

**Frontend**: Vanilla JavaScript, HTML5, CSS3  
**Backend**: Flask (Python)  
**Database**: SQLite  
**Authentication**: JWT + bcrypt  
**Email**: Gmail SMTP with TLS

## 📝 Quick Test

1. Open http://localhost:5500/register.html
2. Fill in your details
3. Click "Verify" on email field
4. Check your email for OTP code
5. Enter the 6-digit code
6. Complete registration

## 🔌 API Endpoints

- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login
- `POST /api/auth/send-otp` - Send OTP to email
- `POST /api/auth/verify-otp` - Verify OTP code
- `GET /api/matches` - List matches
- `POST /api/matches` - Create match
- `POST /api/matches/<id>/join` - Join match
- `GET /api/users/me` - Get profile

Full API documentation: `backend/README.md`

## 📂 Project Structure

```
teamup-sports/
├── backend/          # Flask API
│   ├── models/       # Database models
│   ├── routes/       # API endpoints
│   ├── utils/        # Helper functions (email, auth, validators)
│   └── instance/     # SQLite database
├── js/               # Frontend JavaScript
├── styles/           # CSS files
└── *.html            # HTML pages
```

## ⚠️ Note

Both servers are currently running. Press Ctrl+C in the terminal windows to stop them.

## 📧 Email Configuration

**SMTP**: Gmail (smtp.gmail.com:587)  
**From**: teamupsports1845@gmail.com  
**Security**: TLS encryption enabled  
**Status**: ✅ Working and sending emails

See `EMAIL_WORKING.md` for detailed email setup information.

>>>>>>> f53eae0d79a4e2ff5685904f26645d65ea972e9e
