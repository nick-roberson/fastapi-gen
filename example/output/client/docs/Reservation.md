# Reservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) |  | [optional]
**restaurant_id** | **str** | The ID of the restaurant where the reservation is made |
**user_id** | **str** | The ID of the user who made the reservation |
**reservation_time** | **datetime** | The date and time of the reservation |
**party_size** | **int** | The size of the party for the reservation |
**special_requests** | [**SpecialRequests**](SpecialRequests.md) |  | [optional]

## Example

```python
from openapi_client.models.reservation import Reservation

# TODO update the JSON string below
json = "{}"
# create an instance of Reservation from a JSON string
reservation_instance = Reservation.from_json(json)
# print the JSON string representation of the object
print(Reservation.to_json())

# convert the object into a dict
reservation_dict = reservation_instance.to_dict()
# create an instance of Reservation from a dict
reservation_form_dict = reservation.from_dict(reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
