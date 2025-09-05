from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Date, ForeignKey, Float, DateTime, Text, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date, datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Define models for Animal Predator Tracker


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(360), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    password: Mapped[str] = mapped_column(String(225), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    sightings = relationship("Sighting", back_populates="reporter")


class Predator(Base):
    __tablename__ = "predators"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    species: Mapped[str] = mapped_column(String(50), nullable=False)
    common_name: Mapped[str] = mapped_column(String(100), nullable=False)
    scientific_name: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    danger_level: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # Low, Medium, High, Critical
    size_category: Mapped[str] = mapped_column(
        String(20), nullable=True
    )  # Small, Medium, Large
    active_seasons: Mapped[str] = mapped_column(
        String(100), nullable=True
    )  # Spring, Summer, Fall, Winter
    prevention: Mapped[str] = mapped_column(String(360), nullable=False)

    # Relationships
    sightings = relationship("Sighting", back_populates="predator")


class Forest(Base):
    __tablename__ = "forests"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    forest_name: Mapped[str] = mapped_column(String(360), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    county: Mapped[str] = mapped_column(String(100), nullable=True)
    total_area_sq_miles: Mapped[float] = mapped_column(Float, nullable=True)
    elevation_min: Mapped[int] = mapped_column(Integer, nullable=True)
    elevation_max: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    contact_info: Mapped[str] = mapped_column(String(200), nullable=True)

    # Relationships
    trails = relationship("Trail", back_populates="forest")


class Trail(Base):
    __tablename__ = "trails"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trail_name: Mapped[str] = mapped_column(String(360), nullable=False)
    forest_id: Mapped[int] = mapped_column(ForeignKey("forests.id"), nullable=False)

    # Location data
    start_latitude: Mapped[float] = mapped_column(Float, nullable=False)
    start_longitude: Mapped[float] = mapped_column(Float, nullable=False)
    end_latitude: Mapped[float] = mapped_column(Float, nullable=True)
    end_longitude: Mapped[float] = mapped_column(Float, nullable=True)

    # Trail details
    length_miles: Mapped[float] = mapped_column(Float, nullable=False)
    difficulty_level: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # Easy, Moderate, Difficult, Expert
    elevation_gain: Mapped[int] = mapped_column(Integer, nullable=True)
    trail_type: Mapped[str] = mapped_column(
        String(50), nullable=True
    )  # Loop, Out-and-back, Point-to-point

    # Safety information
    current_danger_level: Mapped[str] = mapped_column(String(20), default="Low")
    last_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_closed: Mapped[bool] = mapped_column(Boolean, default=False)
    closure_reason: Mapped[str] = mapped_column(String(200), nullable=True)

    # Relationships
    forest = relationship("Forest", back_populates="trails")
    sightings = relationship("Sighting", back_populates="trail")


class Sighting(Base):
    __tablename__ = "sightings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Foreign keys
    predator_id: Mapped[int] = mapped_column(ForeignKey("predators.id"), nullable=False)
    trail_id: Mapped[int] = mapped_column(ForeignKey("trails.id"), nullable=False)
    reporter_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    # Location details
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    location_description: Mapped[str] = mapped_column(String(500), nullable=True)

    # Sighting details
    sighting_date: Mapped[date] = mapped_column(Date, nullable=False)
    sighting_time: Mapped[str] = mapped_column(
        String(10), nullable=True
    )  # HH:MM format
    weather_conditions: Mapped[str] = mapped_column(String(100), nullable=True)

    # Predator behavior
    behavior_observed: Mapped[str] = mapped_column(Text, nullable=True)
    number_of_animals: Mapped[int] = mapped_column(Integer, default=1)
    aggressive_behavior: Mapped[bool] = mapped_column(Boolean, default=False)

    # Additional information
    description: Mapped[str] = mapped_column(Text, nullable=True)
    photo_url: Mapped[str] = mapped_column(String(500), nullable=True)

    # Verification and status
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    verified_by: Mapped[str] = mapped_column(String(100), nullable=True)
    verification_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # Metadata
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    predator = relationship("Predator", back_populates="sightings")
    trail = relationship("Trail", back_populates="sightings")
    reporter = relationship("User", back_populates="sightings")


class Alert(Base):
    __tablename__ = "alerts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Alert details
    alert_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # Trail Closure, High Activity, etc.
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # Low, Medium, High, Critical
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)

    # Location (can be trail-specific or forest-wide)
    forest_id: Mapped[int] = mapped_column(ForeignKey("forests.id"), nullable=True)
    trail_id: Mapped[int] = mapped_column(ForeignKey("trails.id"), nullable=True)

    # Timing
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Metadata
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
