# Restaurant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**name** | **str** | The name of the alembic | 
**location** | **str** | The physical location of the alembic | 
**cuisine** | [**Cuisine**](Cuisine.md) |  | [optional] 
**rating** | [**Rating**](Rating.md) |  | [optional] 
**price_range** | [**PriceRange**](PriceRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.restaurant import Restaurant

# TODO update the JSON string below
json = "{}"
# create an instance of Restaurant from a JSON string
restaurant_instance = Restaurant.from_json(json)
# print the JSON string representation of the object
print(Restaurant.to_json())

# convert the object into a dict
restaurant_dict = restaurant_instance.to_dict()
# create an instance of Restaurant from a dict
restaurant_form_dict = restaurant.from_dict(restaurant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


