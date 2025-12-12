from pydantic import BaseModel, Field
from typing import Optional


class ItemBase(BaseModel):
    """Base schema for item with all fields"""
    id: int = Field(..., description="Unique identifier for the item")
    name: str = Field(..., description="Name of the character")
    height: int = Field(..., description="Height in centimeters")
    mass: int = Field(..., description="Mass in kilograms")
    hair_color: str = Field(..., description="Hair color")
    skin_color: str = Field(..., description="Skin color")
    eye_color: str = Field(..., description="Eye color")
    birth_year: Optional[str] = Field(None, description="Birth year (optional)")


class ItemCreate(ItemBase):
    """Schema for creating a new item"""
    pass


class ItemResponse(ItemBase):
    """Schema for item response with all fields"""
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Luke Skywalker",
                "height": 172,
                "mass": 77,
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": None
            }
        }


class ItemListResponse(BaseModel):
    """Schema for item in list response (only id, name, height, mass, birth_year)"""
    id: int = Field(..., description="Unique identifier for the item")
    name: str = Field(..., description="Name of the character")
    height: int = Field(..., description="Height in centimeters")
    mass: int = Field(..., description="Mass in kilograms")
    birth_year: Optional[str] = Field(None, description="Birth year (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Luke Skywalker",
                "height": 172,
                "mass": 77,
                "birth_year": None
            }
        }


class ErrorResponse(BaseModel):
    """Schema for error responses"""
    detail: str = Field(..., description="Error message")

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Item with id 1 already exists"
            }
        }


class SuccessResponse(BaseModel):
    """Schema for success responses"""
    detail: str = Field(..., description="Success message")

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Item deleted successfully"
            }
        }

