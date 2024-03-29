#!/usr/bin/python3

"""
Script to import data into the Fifithatlady Nanny Jobs database
"""

import argparse
import json
from models import db_session
from models.fifithatlady_nanny_job import FifithatladyNannyJob

def import_data(file_path):
    """Import data from a JSON file into the database."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                # Validate data before processing
                if not all(key in item for key in ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'area', 'address', 'city_id', 'user_id', 'security']):
                    print("Error: Invalid data format. Missing required fields.")
                    return
                
                nanny_job_data = {
                    'title': item['title'],
                    'description': item['description'],
                    'price': item['price'],
                    'bedrooms': item['bedrooms'],
                    'bathrooms': item['bathrooms'],
                    'area': item['area'],
                    'address': item['address'],
                    'city_id': item['city_id'],
                    'user_id': item['user_id'],
                    'security': item['security'],
                }
                nanny_job_obj = FifithatladyNannyJob(**nanny_job_data)
                db_session.add(nanny_job_obj)

        db_session.commit()
        print("Data imported successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Import data into the Fifithatlady Nanny Jobs database")
    parser.add_argument("file_path", help="Path to the JSON file containing data")
    args = parser.parse_args()

    import_data(args.file_path)

if __name__ == "__main__":
    main()

