# UserQuery

Query model for User 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**preferences** | **List[object]** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_query import UserQuery

# TODO update the JSON string below
json = "{}"
# create an instance of UserQuery from a JSON string
user_query_instance = UserQuery.from_json(json)
# print the JSON string representation of the object
print(UserQuery.to_json())

# convert the object into a dict
user_query_dict = user_query_instance.to_dict()
# create an instance of UserQuery from a dict
user_query_from_dict = UserQuery.from_dict(user_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


