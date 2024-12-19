import os
import pathlib

def create_project_structure():
    base_path = pathlib.Path("ap")
    
    # Create main directories
    directories = [
        "data/raw",
        "data/processed",
        "data/output",
        "src/data_processing",
        "src/clustering",
        "tests"
    ]
    
    for dir_path in directories:
        os.makedirs(base_path / dir_path, exist_ok=True)
    
    # Create __init__.py files
    init_locations = [
        "src",
        "src/data_processing",
        "src/clustering",
        "tests"
    ]
    
    for location in init_locations:
        (base_path / location / "__init__.py").touch()
    
    # Create required files
    files_to_create = [
        "requirements.txt",
        "main.py",
        "src/config.py",
        "src/data_processing/data_processor.py",
        "src/data_processing/feature_engineering.py",
        "src/data_processing/utils.py",
        "src/clustering/hierarchical_clustering.py",
        "src/clustering/visualization.py"
    ]
    
    for file_path in files_to_create:
        (base_path / file_path).touch()

if __name__ == "__main__":
    create_project_structure()
