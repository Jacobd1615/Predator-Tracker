# 🐾 Animal Predator Tracker

**A comprehensive wildlife safety application for hikers, climbers, campers, and cave divers**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()

## 🎯 Overview

The Animal Predator Tracker is a web-based application designed to enhance outdoor safety by providing real-time information about predator activity across forest trails. The application helps outdoor enthusiasts make informed decisions about trail selection by tracking wildlife sightings, analyzing danger levels, and recommending safer alternative routes.

### 🌲 Featured Forest Areas
- **Pine Forest State Park** - Primary hiking destination with moderate trail difficulty
- **Oak Ridge Wildlife Area** - Family-friendly trails with established safety protocols  
- **Mountain View Forest** - Advanced trails for experienced hikers and climbers

## ✨ Key Features

### 🗺️ Trail Intelligence
- **Real-time Danger Assessment** - Dynamic safety ratings based on recent predator activity
- **Alternative Route Recommendations** - Intelligent suggestions when primary trails show high risk
- **Geographic Mapping** - Precise GPS coordinates for all sightings and trail markers
- **Trail Closure Alerts** - Immediate notifications for unsafe conditions

### 🐻 Predator Monitoring
- **Species Identification** - Comprehensive database of regional predators
- **Behavioral Analysis** - Tracking of aggressive vs. passive encounters
- **Seasonal Activity Patterns** - Historical data analysis for predictive insights
- **Verification System** - Expert validation of reported sightings

### 👥 Community Features
- **User Reporting** - Simple interface for submitting predator sightings
- **Photo Documentation** - Visual evidence support for sighting verification
- **Expert Verification** - Professional wildlife biologist review system
- **Safety Alerts** - Community-wide notifications for immediate threats

### 📊 Analytics & Insights
- **Hotspot Detection** - Machine learning algorithms identify high-risk areas
- **Trend Analysis** - Long-term patterns in predator movement and behavior
- **Safety Metrics** - Comprehensive trail safety scoring system
- **Predictive Modeling** - AI-powered risk assessment for future conditions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0+ (for production) or SQLite (for development)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/animal-predator-tracker.git
   cd animal-predator-tracker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Initialize database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

Visit `http://localhost:5000` to access the application.

## 🏗️ Architecture

### Technology Stack
- **Backend**: Flask (Python)
- **Database**: SQLAlchemy ORM with MySQL/SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Mapping**: Leaflet.js with OpenStreetMap
- **Testing**: pytest with comprehensive test coverage
- **Deployment**: Docker-ready with CI/CD support

### Database Schema
```
├── Users (Authentication & Profiles)
├── Forests (Regional Forest Areas)
├── Trails (Individual Trail Data)
├── Predators (Species Information)
├── Sightings (User-Reported Encounters)
└── Alerts (Safety Notifications)
```

## 📁 Project Structure

```
animal-predator-tracker/
├── app/
│   ├── blueprints/          # Route modules
│   ├── models.py           # Database models
│   ├── utils/              # Utility functions
│   ├── static/             # CSS, JS, images
│   └── extensions.py       # Flask extensions
├── tests/                  # Comprehensive test suite
├── config.py              # Configuration settings
├── app.py                 # Application entry point
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test categories
pytest tests/test_models.py
pytest tests/test_routes.py
pytest tests/test_trail_analysis.py
```

## 🔒 Security Features

- **Input Validation** - Comprehensive data sanitization
- **Authentication** - Secure user login and session management
- **Authorization** - Role-based access control (User/Admin)
- **Data Protection** - Encrypted sensitive information storage
- **API Security** - Rate limiting and request validation

## 🌍 API Documentation

### Core Endpoints

#### Trails
- `GET /api/trails` - List all trails with current safety status
- `GET /api/trails/{id}` - Detailed trail information
- `GET /api/trails/{id}/danger-level` - Current risk assessment

#### Sightings
- `POST /api/sightings` - Submit new predator sighting
- `GET /api/sightings` - Retrieve sightings by area/date
- `PUT /api/sightings/{id}/verify` - Verify sighting (Admin only)

#### Safety
- `GET /api/safety/recommendations` - Get alternative trail suggestions
- `GET /api/alerts` - Current safety alerts
- `POST /api/alerts` - Create safety alert (Admin only)

## 🤝 Contributing

We welcome contributions from the outdoor and development communities!

### Development Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with tests
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Standards
- Follow PEP 8 Python style guidelines
- Maintain test coverage above 90%
- Document all public functions and classes
- Use meaningful commit messages

## 📈 Roadmap

### Phase 1 (Current)
- ✅ Core trail and sighting management
- ✅ Basic safety assessment algorithms
- ✅ User authentication system

### Phase 2 (Q4 2025)
- 🔄 Mobile application (iOS/Android)
- 🔄 Advanced machine learning predictions
- 🔄 Integration with park service APIs

### Phase 3 (2026)
- 📋 Real-time weather integration
- 📋 Crowdsourced trail condition updates
- 📋 Emergency response coordination

## 🆘 Support & Safety

### Emergency Contacts
- **Emergency Services**: 911
- **Park Service**: Contact local ranger station
- **Wildlife Emergency**: State wildlife department

### Disclaimer
This application provides informational guidance only. Always follow official park guidelines, carry appropriate safety equipment, and inform others of your hiking plans. The developers are not responsible for decisions made based on app recommendations.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- State Forest Service for trail data cooperation
- Wildlife biology experts for species information
- Beta testing community of local hikers and outdoor enthusiasts
- Open source mapping communities

## 📞 Contact

**Project Maintainer**: Jacob  
**Email**: [jdyson.pnw@gmail.com]  
**GitHub**: [@Jacobd1615](https://github.com/Jacobd1615)

---

**Stay Safe. Stay Informed. Enjoy the Outdoors.** 🏔️

*Built with ❤️ for the outdoor community*
