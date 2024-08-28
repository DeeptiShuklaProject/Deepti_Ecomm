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


## Endpoints

The following endpoints are available:

- **User Product Interactions**: [http://localhost:8080/data/user_product_interactions](http://localhost:8080/data/user_product_interactions)
- **User Features**: [http://localhost:8080/data/user_features](http://localhost:8080/data/user_features)
- **Product Features**: [http://localhost:8080/data/product_features](http://localhost:8080/data/product_features)

These endpoints provide access to the processed data used for generating recommendations.

## Running the Application

1. **Install Dependencies**

   Ensure you have Python 3.12 and Docker installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt


## How to Run
1. Clone the repository.
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the project:
    ```bash
    python main.py
    ```
4. To run the project in a Docker container:
    ```bash
    docker build -t personalized_recommendation_system .
    docker run -it --rm personalized_recommendation_system
    ```

## Deployment
The project can be containerized using Docker for easy deployment.
