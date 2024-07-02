import json
import psycopg2
import os

def lambda_handler(event, context):
    # Database connection details
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Insert data (assuming event['body'] contains a JSON object with 'name' and 'description')
        item = json.loads(event['body'])
        cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item['name'], item['description']))
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps('Item created successfully!')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
