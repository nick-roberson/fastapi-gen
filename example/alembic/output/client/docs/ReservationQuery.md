# ReservationQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**restaurant_id** | [**RestaurantId**](RestaurantId.md) |  | [optional] 
**user_id** | [**UserId**](UserId.md) |  | [optional] 
**reservation_time** | [**ReservationTime**](ReservationTime.md) |  | [optional] 
**party_size** | [**PartySize**](PartySize.md) |  | [optional] 
**special_requests** | [**SpecialRequests1**](SpecialRequests1.md) |  | [optional] 

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
reservation_query_form_dict = reservation_query.from_dict(reservation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


