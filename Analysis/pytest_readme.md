# Pytest Setup for Preprocessing Tests

## Install
```
pip install pytest
```

## Run Tests
```
pytest test_preprocessing.py -v
```

## What it tests
- Tokenization: List parsing from model outputs
- Date filtering: Time range data filtering  
- Persona injection: Demographic categorization

## When to use
Run before processing new datasets to catch silent bugs in the preprocessing pipeline.