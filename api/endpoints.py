# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI application!"}

# @router.get("/recommend/{user_id}")
# def recommend(user_id: int, num_recommendations: int = 5):
#     # Dummy recommendation logic
#     return {"user_id": user_id, "num_recommendations": num_recommendations}


from fastapi import APIRouter, HTTPException
import pandas as pd

router = APIRouter()

@router.get("/data/{data_type}")
async def get_data(data_type: str):
    """
    Endpoint to fetch data from CSV files.
    :param data_type: Type of data to fetch ('user_product_interactions', 'user_features', 'product_features')
    :return: Data from the specified CSV file.
    """
    file_map = {
        "user_product_interactions": "data/processed/user_product_interactions.csv",
        "user_features": "data/processed/user_features.csv",
        "product_features": "data/processed/product_features.csv"
    }

    file_path = file_map.get(data_type)
    if not file_path:
        raise HTTPException(status_code=404, detail="Data type not found")

    try:
        data = pd.read_csv(file_path)
        return data.to_dict(orient='records')
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

