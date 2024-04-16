# ReviewQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**restaurant_id** | [**RestaurantId**](RestaurantId.md) |  | [optional] 
**user_id** | [**UserId**](UserId.md) |  | [optional] 
**rating** | [**Rating1**](Rating1.md) |  | [optional] 
**comment** | [**Comment1**](Comment1.md) |  | [optional] 

## Example

```python
from openapi_client.models.review_query import ReviewQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewQuery from a JSON string
review_query_instance = ReviewQuery.from_json(json)
# print the JSON string representation of the object
print(ReviewQuery.to_json())

# convert the object into a dict
review_query_dict = review_query_instance.to_dict()
# create an instance of ReviewQuery from a dict
review_query_form_dict = review_query.from_dict(review_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


