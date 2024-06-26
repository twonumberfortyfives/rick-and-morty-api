# Rick and Morty API

This project is a Django-based API for retrieving information about characters from the "Rick and Morty" universe. It includes endpoints for fetching random characters and filtering characters by name. The application is containerized using Docker and includes services for the database, Redis, Celery, and Flower.

## Table of Contents

- [Endpoints](#endpoints)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Services](#services)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [License](#license)

## Endpoints

### Get Random Character

**URL:** `/api/random-character/`  
**Method:** `GET`  
**Description:** Fetches a random character from the database.  
**Response:** JSON representation of a character.

### List Characters

**URL:** `/api/characters/`  
**Method:** `GET`  
**Description:** Lists characters with optional name filtering.  
**Query Params:**
- `name` (string, optional): Filter characters by name.

**Response:** JSON representation of a list of characters.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/rick-and-morty-api.git
   cd rick-and-morty-api
   docker-compose build
   docker-compose up
