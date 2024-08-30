# Personalized Recommendation System

## Overview
This project develops a personalized product recommendation engine using collaborative filtering, content-based filtering, and hybrid models.

## Directory Structure
- `data/`: Contains raw and processed data.
- `models/`: Contains the implementation of different recommendation models.
- `utils/`: Contains utility functions for data loading, preprocessing, and metrics calculation.
- `main.py`: Main script to run the project.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Dockerfile for containerization.
docker build -t personalized-recommendation-system .





## Running the Application

1. **Install Dependencies**

   Ensure you have Python 3.12 and Docker installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt






# Personalized Recommendation System

## Overview

This project is a personalized recommendation system built using FastAPI and Docker. The system provides product recommendations based on user input and evaluates the recommendations using various metrics.

## Features

- **API Endpoints:** Provides recommendations and evaluates them.
- **Dockerized:** Easy to deploy using Docker.
- **Data Integration:** Supports data loading and processing.

## Getting Started

### Prerequisites

- Docker
- Docker Compose (optional for multi-container setups)

### Running the Application Locally

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd personalized_recommendation_system
   ```

2. **Build the Docker Image**

   ```bash
   docker build -t personalized-recommendation-system .
   ```

3. **Run the Docker Container**

   ```bash
   docker run -d -p 8001:8000 -v D:/personalized_recommendation_system/data:/app/data personalized-recommendation-system
   ```

4. **Access the Application**

   Open your browser and go to `http://localhost:8001` to access the FastAPI application.


   ## Endpoints

The following endpoints are available:

- **User Product Interactions**: [http://localhost:8001/data/user_product_interactions](http://localhost:8001/data/user_product_interactions)
- **User Features**: [http://localhost:8001/data/user_features](http://localhost:8001/data/user_features)
- **Product Features**: [http://localhost:8001/data/product_features](http://localhost:8001/data/product_features)

These endpoints provide access to the processed data used for generating recommendations.

### Docker Hub

The Docker image is available on Docker Hub. You can pull it using:

```bash
docker pull <username>/<repository>:latest
