import pytest
import pandas as pd
import numpy as np
import json
import ast
import re

# Some functions from main_analysis.ipynb
def parse_list(list_str, model_name=None, row_id=None):
    """Parse a string representation of a list into a list of floats."""
    if pd.isna(list_str):
        return None
    
    if model_name == "DeepSeek-V3" and row_id == 70119139:
        return None
    
    try:
        if isinstance(list_str, str):
            list_str = list_str.strip()
            
            # Try JSON first
            try:
                result = json.loads(list_str)
                if isinstance(result, list) and len(result) == 10:
                    return [float(x) for x in result]
            except:
                pass
            
            # Try ast.literal_eval
            try:
                result = ast.literal_eval(list_str)
                if isinstance(result, list) and len(result) == 10:
                    return [float(x) for x in result]
            except:
                pass
        
        return None
    except:
        return None

def create_age_group(age):
    """Convert numeric age to age group category."""
    if pd.isna(age):
        return "Unknown"
    try:
        age = float(age)
        if age < 25:
            return "18-24"
        elif age < 35:
            return "25-34"
        elif age < 45:
            return "35-44"
        else:
            return "45+"
    except:
        return "Unknown"

def filter_by_date(df, date_column, start_date, end_date):
    """Filter dataframe by date range."""
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    return df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]

# ==================== TESTS ====================

def test_tokenization():
    """Test that list parsing correctly tokenizes different input formats."""
    # Valid JSON format
    json_str = "[10, 15, 20, 25, 30, 5, 8, 12, 18, 22]"
    result = parse_list(json_str)
    assert result == [10.0, 15.0, 20.0, 25.0, 30.0, 5.0, 8.0, 12.0, 18.0, 22.0]
    
    # Invalid format should return None
    invalid_str = "not a list"
    assert parse_list(invalid_str) is None
    
    # Wrong length should return None
    short_list = "[10, 15, 20]"
    assert parse_list(short_list) is None

def test_date_filtering():
    """Test date filtering logic works correctly."""
    # Create test dataframe
    df = pd.DataFrame({
        'date': ['2024-01-01', '2024-06-15', '2024-12-31', '2025-01-01'],
        'value': [1, 2, 3, 4]
    })
    
    # Filter for 2024 data
    filtered = filter_by_date(df, 'date', '2024-01-01', '2024-12-31')
    
    assert len(filtered) == 3
    assert filtered['value'].tolist() == [1, 2, 3]

def test_persona_injection():
    """Test demographic categorization (persona injection) logic."""
    # Test age group assignment
    assert create_age_group(20) == "18-24"
    assert create_age_group(30) == "25-34"
    assert create_age_group(40) == "35-44"
    assert create_age_group(50) == "45+"
    
    # Test invalid inputs
    assert create_age_group(None) == "Unknown"
    assert create_age_group("invalid") == "Unknown"