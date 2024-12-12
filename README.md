# Movie Recommendation System

## Table of Contents

- [Movie Recommendation System](#movie-recommendation-system)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
    - [Running Locally (with venv)](#running-locally-with-venv)
    - [Running with Docker](#running-with-docker)
  - [Usage](#usage)
  - [API Documentation](#api-documentation)

## Overview

This repository contains database application that will help user find the movies he would like.

## Features

> **todo:**
> describe the features

- User authentication and profile management
- Movie search and filtering by genre, rating, and year
- Personalized movie recommendations
- Responsive and intuitive user interface
- Scalable backend with database integration

## Technologies Used

- **Backend:** Django
- **Frontend:** Django Templates
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Others:** ...

## Setup and Installation

### Running Locally (with venv)

1. Clone the repository:

   ```bash
   git clone https://github.com/Mateusz2673/RecommendationSystem.git
   cd movie-recommendation-system
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at `http://localhost:8000`.

### Running with Docker

1. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

2. Access the application in your browser at `http://localhost:8000`.

3. To stop the containers:
   ```bash
   docker-compose down
   ```

## Usage

> **todo:**
> describe the usage

1. Register or log in to your account.
2. Search for movies or browse recommendations.
3. Filter movies by genre, rating, or year.
4. Save favorite movies to your profile.

## API Documentation

> **todo:**
> setup swagger

The API provides endpoints for user authentication, movie search, and recommendations. Detailed documentation is available at `/api/docs/` when the server is running.
