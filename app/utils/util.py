from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from functools import wraps
from flask import request, jsonify
import os

# Use environment variable for security, fallback for development
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_change_in_production")


def encode_token(user_id, role="user"):
    """Generate JWT token for user authentication."""
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc),
        "sub": str(user_id),
        "role": role,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def encode_admin_token(admin_id):
    """Generate JWT token for admin with extended expiration."""
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(hours=3),
        "iat": datetime.now(timezone.utc),
        "sub": str(admin_id),
        "role": "admin",
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def token_required(f):
    """Decorator to require valid JWT token for protected routes."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split()[1]

        if not token:
            return jsonify({"message": "Token is missing. Please log in"}), 401

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_role = payload.get("role")
            user_id = payload["sub"]
        except ExpiredSignatureError:
            return jsonify({"message": "Session expired. Please log in again."}), 401
        except JWTError:
            return jsonify({"message": "Invalid token. Please login again."}), 401

        if user_role not in ["user", "admin"]:
            return jsonify({"message": "Invalid role. Access denied."}), 403

        # Add user info to kwargs for use in the protected route
        kwargs["user_id"] = user_id
        kwargs["user_role"] = user_role
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    """Decorator to require admin role for protected admin routes."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split()[1]

        if not token:
            return jsonify({"message": "Token is missing. Please log in"}), 401

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_role = payload.get("role")
            user_id = payload["sub"]
        except ExpiredSignatureError:
            return jsonify({"message": "Session expired. Please log in again."}), 401
        except JWTError:
            return jsonify({"message": "Invalid token. Please login again."}), 401

        if user_role != "admin":
            return jsonify({"message": "Admin access required. Access denied."}), 403

        # Add admin info to kwargs
        kwargs["admin_id"] = user_id
        kwargs["user_role"] = user_role
        return f(*args, **kwargs)

    return decorated_function


def calculate_trail_danger_level(recent_sightings, trail_id):
    """Calculate danger level based on recent predator sightings."""
    if not recent_sightings:
        return "Low"

    # Count sightings in last 7 days
    week_ago = datetime.now() - timedelta(days=7)
    recent_count = len(
        [s for s in recent_sightings if s.sighting_date >= week_ago.date()]
    )

    # Count aggressive behavior incidents
    aggressive_count = len([s for s in recent_sightings if s.aggressive_behavior])

    if aggressive_count > 0:
        return "Critical"
    elif recent_count >= 3:
        return "High"
    elif recent_count >= 1:
        return "Medium"
    else:
        return "Low"


def get_alternative_trails(current_trail_id, forest_id, danger_threshold="Medium"):
    """Get alternative trails with lower danger levels."""
    # This would query the database for trails in the same forest
    # with lower danger levels - placeholder for now
    return []


def format_sighting_response(sighting):
    """Format sighting data for API response."""
    return {
        "id": sighting.id,
        "predator_species": sighting.predator.species if sighting.predator else None,
        "trail_name": sighting.trail.trail_name if sighting.trail else None,
        "location": {
            "latitude": sighting.latitude,
            "longitude": sighting.longitude,
            "description": sighting.location_description,
        },
        "sighting_date": (
            sighting.sighting_date.isoformat() if sighting.sighting_date else None
        ),
        "verified": sighting.is_verified,
        "aggressive_behavior": sighting.aggressive_behavior,
        "description": sighting.description,
    }
