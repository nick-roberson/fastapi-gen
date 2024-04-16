# RestaurantQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**cuisine** | [**Cuisine1**](Cuisine1.md) |  | [optional] 
**rating** | [**Rating1**](Rating1.md) |  | [optional] 
**price_range** | [**PriceRange1**](PriceRange1.md) |  | [optional] 

## Example

```python
from openapi_client.models.restaurant_query import RestaurantQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantQuery from a JSON string
restaurant_query_instance = RestaurantQuery.from_json(json)
# print the JSON string representation of the object
print(RestaurantQuery.to_json())

# convert the object into a dict
restaurant_query_dict = restaurant_query_instance.to_dict()
# create an instance of RestaurantQuery from a dict
restaurant_query_form_dict = restaurant_query.from_dict(restaurant_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


