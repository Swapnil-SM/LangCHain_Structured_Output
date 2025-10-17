# JSON Schema describing a student object
# this file is created to show how to define a json schema manually
student_schema = {
    "title": "student",                # Title or name of the schema
    "description": "Schema about students",  # Short info about what this schema represents
    "type": "object",                  # Defines that the data must be a JSON object
    "properties": {                    # Lists all possible keys (fields) and their expected types
        "name": { "type": "string" },  # 'name' must be a string value
        "age": { "type": "integer" }   # 'age' must be an integer value
    },
    "required": ["name"]               # Fields that must be present in the JSON data
}

# Example usage:
import json
print(json.dumps(student_schema, indent=2))
