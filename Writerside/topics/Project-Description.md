# Virtual Event Management System

## Project Description

Allow users to create and manage virtual events
- Users can create, manage, and participate in virtual events

## Features

- Python for backend development
- FastAPI for RESTful API
- MongoDB for database
- Motor for MongoDB async driver
- Google Cloud Run for deployment
- GitHub Actions for CI/CD
- Docker for containerization
- Jinja2 for server-side templating


## System Architecture

- Backend: FastAPI, MongoDB, Motor
- Frontend: Jinja2
- Deployment: Google Cloud Run
- CI/CD: GitHub Actions
- Containerization: Docker
- Version Control: Git, GitHub

## Core Features

- User Management
  - Registration
  - Login
  - Profile Management without front-end interaction (API)
- Event Management
  - Create Event
    - Event Name
    - Date
    - Time
    - Description
    - Link
  - Update Event
- Event Discovery
  - provide functionality to discover events and receive a unique e-ticket via email (Jinja2 for template)
- Notification
  - Send email notification to users

## Data Model

- Design MongoDB schema for user and event management
  - User
    - username
    - email
    - password
    - created_at
  - Event
    - event_name
    - date
    - time
    - description
    - link
    - created_at
    - updated_at
  - Ticket
    - user_id
    - event_id
    - ticket_id
    - created_at
    - updated_at

## API Endpoints

- User
  - Register User
  - Login User
  - Get User Profile
  - Update User Profile
- Event
  - Create Event
  - Update Event
  - Get Event
  - Get All Events
- Ticket
  - Create Ticket
  - Get Ticket
  - Get All Tickets
- Notification
  - Send Email Notification
- Authentication
  - JWT Token Authentication
- Error Handling
  - Custom Exception Handling
  - Error Response

## Deployment

- Use Docker for containerization
- Deploy FastAPI application on Google Cloud Run
- Use GitHub Actions for CI/CD
- Use Terraform for Infrastructure as Code


## Expected Outcomes:
A fully functioning Virtual Event Management System that can handle creation, discovery, and management of virtual events.
- Efficient use of asynchronous programming to manage concurrent requests
  - leading to a highly responsive and scalable application.

- An application ready to be deployed on Google Cloud Run
  - demonstrating knowledge of containerization and cloud deployment strategies.

- A well-structured MongoDB schema for user and event management
- A well-documented RESTful API