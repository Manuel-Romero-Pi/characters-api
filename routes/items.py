from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.item import (
    ItemCreate,
    ItemResponse,
    ItemListResponse,
    ErrorResponse,
    SuccessResponse
)
from services.item_service import (
    get_all_items,
    get_items_by_name,
    add_item as add_item_service,
    delete_item as delete_item_service
)

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get(
    "/getAll",
    response_model=List[ItemListResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all items",
    description="Retrieve all items from storage. Returns a list containing only id, name, height, mass, and birth_year fields.",
    response_description="List of all items with fields: id, name, height, mass, birth_year"
)
async def get_all_items():
    """
    Get all items
    
    Returns all items stored in memory. Each item in the response contains:
    - id: Unique identifier (integer)
    - name: Character name (string)
    - height: Height in centimeters (integer)
    - mass: Mass in kilograms (integer)
    - birth_year: Birth year (string, optional)
    
    **Response:**
    - HTTP 200: Successfully retrieved all items
    
    **Example Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Luke Skywalker",
            "height": 172,
            "mass": 77,
            "birth_year": null
        }
    ]
    ```
    """
    items = get_all_items()
    return items


@router.get(
    "/get/{name}",
    response_model=List[ItemResponse],
    status_code=status.HTTP_200_OK,
    summary="Get items by name",
    description="Search for items by name. Returns all items matching the provided name (case-insensitive). Returns all fields for matching items.",
    response_description="List of items matching the name with all fields",
    responses={
        200: {
            "description": "Items found",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "name": "Luke Skywalker",
                            "height": 172,
                            "mass": 77,
                            "hair_color": "blond",
                            "skin_color": "fair",
                            "eye_color": "blue",
                            "birth_year": None
                        }
                    ]
                }
            }
        },
        404: {
            "description": "No items found with the provided name",
            "model": ErrorResponse
        }
    }
)
async def get_items_by_name(name: str):
    """
    Get items by name
    
    Searches for items matching the provided name (case-insensitive).
    
    **Parameters:**
    - name: Name of the character to search for (path parameter)
    
    **Response:**
    - HTTP 200: Successfully found items
    - HTTP 404: No items found with the provided name
    
    **Example Request:**
    ```
    GET /items/get/Luke Skywalker
    ```
    
    **Example Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Luke Skywalker",
            "height": 172,
            "mass": 77,
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": null
        }
    ]
    ```
    """
    items = get_items_by_name(name)
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No items found with name '{name}'"
        )
    return items


@router.post(
    "/add",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new item",
    description="Create and add a new item to storage. All fields are required and must not be null. The id must be unique.",
    response_description="The created item with all its fields",
    responses={
        201: {
            "description": "Item successfully created",
            "content": {
                "application/json": {
                    "example": {
                        "id": 9,
                        "name": "Yoda",
                        "height": 66,
                        "mass": 17,
                        "hair_color": "white",
                        "skin_color": "green",
                        "eye_color": "brown",
                        "birth_year": None
                    }
                }
            }
        },
        400: {
            "description": "Bad request - Item validation failed or item with same id already exists",
            "model": ErrorResponse
        },
        422: {
            "description": "Validation error - Invalid data format or missing required fields"
        }
    }
)
async def add_item(item: ItemCreate):
    """
    Add a new item
    
    Creates a new item in storage. The request body must include all required fields.
    
    **Validation Rules:**
    - All fields are required and cannot be null
    - id must be a unique integer
    - height and mass must be integers
    - name, hair_color, skin_color, eye_color must be strings
    - birth_year is optional (string or null)
    - Item with the same id cannot already exist
    
    **Request Body:**
    - id: Unique identifier (integer, required)
    - name: Character name (string, required)
    - height: Height in centimeters (integer, required)
    - mass: Mass in kilograms (integer, required)
    - hair_color: Hair color (string, required)
    - skin_color: Skin color (string, required)
    - eye_color: Eye color (string, required)
    - birth_year: Birth year (string, optional)
    
    **Response:**
    - HTTP 201: Item successfully created
    - HTTP 400: Item with same id already exists
    - HTTP 422: Validation error (missing fields, wrong types, etc.)
    
    **Example Request:**
    ```json
    {
        "id": 9,
        "name": "Yoda",
        "height": 66,
        "mass": 17,
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": null
    }
    ```
    
    **Example Response:**
    ```json
    {
        "id": 9,
        "name": "Yoda",
        "height": 66,
        "mass": 17,
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": null
    }
    ```
    
    **Example Error Response (400):**
    ```json
    {
        "detail": "Item with id 9 already exists"
    }
    ```
    """
    try:
        new_item = add_item_service(item)
        return new_item
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    "/delete/{id}",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete an item by id",
    description="Delete an item from storage using its id. Returns success message if item was found and deleted.",
    response_description="Success message confirming the item was deleted",
    responses={
        200: {
            "description": "Item successfully deleted",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Item with id 1 deleted successfully"
                    }
                }
            }
        },
        400: {
            "description": "Bad request - Item with the provided id does not exist",
            "model": ErrorResponse
        }
    }
)
async def delete_item(id: int):
    """
    Delete an item by id
    
    Removes an item from storage using its unique identifier.
    
    **Parameters:**
    - id: Unique identifier of the item to delete (path parameter, integer)
    
    **Response:**
    - HTTP 200: Item successfully deleted
    - HTTP 400: Item with the provided id does not exist
    
    **Example Request:**
    ```
    DELETE /items/delete/1
    ```
    
    **Example Response (200):**
    ```json
    {
        "detail": "Item with id 1 deleted successfully"
    }
    ```
    
    **Example Error Response (400):**
    ```json
    {
        "detail": "Item with id 1 not found"
    }
    ```
    """
    try:
        delete_item_service(id)
        return SuccessResponse(detail=f"Item with id {id} deleted successfully")
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

