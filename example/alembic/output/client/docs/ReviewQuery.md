# ReviewQuery

Query model for Review 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**restaurant_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**rating** | **float** |  | [optional] 
**comment** | **str** |  | [optional] 

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
review_query_from_dict = ReviewQuery.from_dict(review_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


