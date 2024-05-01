# Reservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**restaurant_id** | **int** | The ID of the alembic where the reservation is made | 
**user_id** | **int** | The ID of the user who made the reservation | 
**reservation_time** | **datetime** | The date and time of the reservation | 
**party_size** | **int** | The size of the party for the reservation | 
**special_requests** | **str** |  | [optional] 

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
reservation_from_dict = Reservation.from_dict(reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


