# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user | [optional]
**username** | **str** | The username of the user |
**email** | **str** | The email address of the user |
**phone_number** | **str** | The phone number of the user | [optional]
**preferences** | **List[object]** | The dining preferences of the user | [optional] [default to []]
**role** | **str** | The role of the user (e.g., admin, user, restaurant_owner) | [optional] [default to 'user']

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
