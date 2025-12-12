from typing import List, Optional
from schemas.item import ItemBase


# Initial data in memory
INITIAL_DATA = [
    {
        "id": 1,
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue"
    },
    {
        "id": 2,
        "name": "R2-D2",
        "height": 96,
        "mass": 32,
        "hair_color": "n/a",
        "skin_color": "blue",
        "eye_color": "red"
    },
    {
        "id": 3,
        "name": "C-3PO",
        "height": 167,
        "mass": 75,
        "hair_color": "n/a",
        "skin_color": "gold",
        "eye_color": "yellow"
    },
    {
        "id": 4,
        "name": "Darth Vader",
        "height": 202,
        "mass": 136,
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow"
    },
    {
        "id": 5,
        "name": "Leia Organa",
        "height": 150,
        "mass": 49,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown"
    },
    {
        "id": 6,
        "name": "Owen Lars",
        "height": 178,
        "mass": 120,
        "hair_color": "grey",
        "skin_color": "light",
        "eye_color": "blue"
    },
    {
        "id": 7,
        "name": "Beru Whitesun lars",
        "height": 165,
        "mass": 75,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "blue"
    },
    {
        "id": 8,
        "name": "R5-D4",
        "height": 97,
        "mass": 32,
        "hair_color": "n/a",
        "skin_color": "white",
        "eye_color": "red"
    }
]

# In-memory storage
_items_storage: List[dict] = INITIAL_DATA.copy()


def get_all_items() -> List[dict]:
    """
    Get all items from storage
    
    Returns:
        List of all items
    """
    return _items_storage.copy()


def get_items_by_name(name: str) -> List[dict]:
    """
    Get items by name (case-insensitive search)
    
    Args:
        name: Name to search for
        
    Returns:
        List of items matching the name
    """
    return [item for item in _items_storage if item["name"].lower() == name.lower()]


def get_item_by_id(item_id: int) -> Optional[dict]:
    """
    Get item by id
    
    Args:
        item_id: Item identifier
        
    Returns:
        Item if found, None otherwise
    """
    for item in _items_storage:
        if item["id"] == item_id:
            return item
    return None


def add_item(item: ItemBase) -> dict:
    """
    Add a new item to storage
    
    Args:
        item: Item to add
        
    Returns:
        The added item
        
    Raises:
        ValueError: If item with same id already exists
    """
    # Check if item with same id exists
    if get_item_by_id(item.id) is not None:
        raise ValueError(f"Item with id {item.id} already exists")
    
    # Convert Pydantic model to dict
    item_dict = item.model_dump()
    _items_storage.append(item_dict)
    return item_dict


def delete_item(item_id: int) -> bool:
    """
    Delete an item from storage
    
    Args:
        item_id: Item identifier
        
    Returns:
        True if item was deleted, False if not found
        
    Raises:
        ValueError: If item does not exist
    """
    item = get_item_by_id(item_id)
    if item is None:
        raise ValueError(f"Item with id {item_id} not found")
    
    _items_storage.remove(item)
    return True

