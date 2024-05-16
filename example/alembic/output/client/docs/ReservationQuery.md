# ReservationQuery

Query model for Reservation 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**restaurant_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**reservation_time** | **datetime** |  | [optional] 
**party_size** | **int** |  | [optional] 
**special_requests** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.reservation_query import ReservationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationQuery from a JSON string
reservation_query_instance = ReservationQuery.from_json(json)
# print the JSON string representation of the object
print(ReservationQuery.to_json())

# convert the object into a dict
reservation_query_dict = reservation_query_instance.to_dict()
# create an instance of ReservationQuery from a dict
reservation_query_from_dict = ReservationQuery.from_dict(reservation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


