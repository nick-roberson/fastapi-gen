# Review


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id2**](Id2.md) |  | [optional]
**restaurant_id** | **str** | The ID of the restaurant being reviewed |
**user_id** | **str** | The ID of the user who wrote the review |
**rating** | **float** | The rating given by the user |
**comment** | [**Comment**](Comment.md) |  | [optional]

## Example

```python
from openapi_client.models.review import Review

# TODO update the JSON string below
json = "{}"
# create an instance of Review from a JSON string
review_instance = Review.from_json(json)
# print the JSON string representation of the object
print(Review.to_json())

# convert the object into a dict
review_dict = review_instance.to_dict()
# create an instance of Review from a dict
review_form_dict = review.from_dict(review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
