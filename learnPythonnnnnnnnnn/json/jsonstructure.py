import json

complex_json_string = """
{
  "companyName": "Tech Solutions Inc.",
  "products": [
    {
      "id": "P001",
      "name": "SuperWidget",
      "specs": {
        "storage": "256GB",
        "ram": "8GB"
      }
    },
    {
      "id": "P002",
      "name": "MegaDevice",
      "specs": {
        "storage": "512GB",
        "ram": "16GB"
      }
    }
  ]
}
"""

#  JSON string to  dictionary
data = json.loads(complex_json_string)

products = data["products"]

first_product_storage = products[0]["specs"]["storage"]
second_product_storage = products[1]["specs"]["storage"]

print("First product storage:", first_product_storage)
print("Second product storage:", second_product_storage)
