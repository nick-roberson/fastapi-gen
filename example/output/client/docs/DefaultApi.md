# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation_reservation_post**](DefaultApi.md#create_reservation_reservation_post) | **POST** /reservation | Create Reservation
[**create_reservations_reservations_post**](DefaultApi.md#create_reservations_reservations_post) | **POST** /reservations | Create Reservations
[**create_restaurant_restaurant_post**](DefaultApi.md#create_restaurant_restaurant_post) | **POST** /restaurant | Create Restaurant
[**create_restaurants_restaurants_post**](DefaultApi.md#create_restaurants_restaurants_post) | **POST** /restaurants | Create Restaurants
[**create_review_review_post**](DefaultApi.md#create_review_review_post) | **POST** /review | Create Review
[**create_reviews_reviews_post**](DefaultApi.md#create_reviews_reviews_post) | **POST** /reviews | Create Reviews
[**create_user_user_post**](DefaultApi.md#create_user_user_post) | **POST** /user | Create User
[**create_users_users_post**](DefaultApi.md#create_users_users_post) | **POST** /users | Create Users
[**delete_reservation_reservation_delete**](DefaultApi.md#delete_reservation_reservation_delete) | **DELETE** /reservation | Delete Reservation
[**delete_reservations_reservations_delete**](DefaultApi.md#delete_reservations_reservations_delete) | **DELETE** /reservations | Delete Reservations
[**delete_restaurant_restaurant_delete**](DefaultApi.md#delete_restaurant_restaurant_delete) | **DELETE** /restaurant | Delete Restaurant
[**delete_restaurants_restaurants_delete**](DefaultApi.md#delete_restaurants_restaurants_delete) | **DELETE** /restaurants | Delete Restaurants
[**delete_review_review_delete**](DefaultApi.md#delete_review_review_delete) | **DELETE** /review | Delete Review
[**delete_reviews_reviews_delete**](DefaultApi.md#delete_reviews_reviews_delete) | **DELETE** /reviews | Delete Reviews
[**delete_user_user_delete**](DefaultApi.md#delete_user_user_delete) | **DELETE** /user | Delete User
[**delete_users_users_delete**](DefaultApi.md#delete_users_users_delete) | **DELETE** /users | Delete Users
[**get_reservation_reservation_get**](DefaultApi.md#get_reservation_reservation_get) | **GET** /reservation | Get Reservation
[**get_reservations_reservations_get**](DefaultApi.md#get_reservations_reservations_get) | **GET** /reservations | Get Reservations
[**get_restaurant_restaurant_get**](DefaultApi.md#get_restaurant_restaurant_get) | **GET** /restaurant | Get Restaurant
[**get_restaurants_restaurants_get**](DefaultApi.md#get_restaurants_restaurants_get) | **GET** /restaurants | Get Restaurants
[**get_review_review_get**](DefaultApi.md#get_review_review_get) | **GET** /review | Get Review
[**get_reviews_reviews_get**](DefaultApi.md#get_reviews_reviews_get) | **GET** /reviews | Get Reviews
[**get_user_user_get**](DefaultApi.md#get_user_user_get) | **GET** /user | Get User
[**get_users_users_get**](DefaultApi.md#get_users_users_get) | **GET** /users | Get Users
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**update_reservation_reservation_put**](DefaultApi.md#update_reservation_reservation_put) | **PUT** /reservation | Update Reservation
[**update_reservations_reservations_put**](DefaultApi.md#update_reservations_reservations_put) | **PUT** /reservations | Update Reservations
[**update_restaurant_restaurant_put**](DefaultApi.md#update_restaurant_restaurant_put) | **PUT** /restaurant | Update Restaurant
[**update_restaurants_restaurants_put**](DefaultApi.md#update_restaurants_restaurants_put) | **PUT** /restaurants | Update Restaurants
[**update_review_review_put**](DefaultApi.md#update_review_review_put) | **PUT** /review | Update Review
[**update_reviews_reviews_put**](DefaultApi.md#update_reviews_reviews_put) | **PUT** /reviews | Update Reviews
[**update_user_user_put**](DefaultApi.md#update_user_user_put) | **PUT** /user | Update User
[**update_users_users_put**](DefaultApi.md#update_users_users_put) | **PUT** /users | Update Users


# **create_reservation_reservation_post**
> Reservation create_reservation_reservation_post(reservation)

Create Reservation

Create a Reservation

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Create Reservation
        api_response = api_instance.create_reservation_reservation_post(reservation)
        print("The response of DefaultApi->create_reservation_reservation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_reservation_reservation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**Reservation**](Reservation.md)|  |

### Return type

[**Reservation**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reservations_reservations_post**
> List[Reservation] create_reservations_reservations_post(reservation)

Create Reservations

Create multiple Reservations

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Create Reservations
        api_response = api_instance.create_reservations_reservations_post(reservation)
        print("The response of DefaultApi->create_reservations_reservations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_reservations_reservations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**List[Reservation]**](Reservation.md)|  |

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_restaurant_restaurant_post**
> Restaurant create_restaurant_restaurant_post(restaurant)

Create Restaurant

Create a Restaurant

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant |

    try:
        # Create Restaurant
        api_response = api_instance.create_restaurant_restaurant_post(restaurant)
        print("The response of DefaultApi->create_restaurant_restaurant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_restaurant_restaurant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**Restaurant**](Restaurant.md)|  |

### Return type

[**Restaurant**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_restaurants_restaurants_post**
> List[Restaurant] create_restaurants_restaurants_post(restaurant)

Create Restaurants

Create multiple Restaurants

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] |

    try:
        # Create Restaurants
        api_response = api_instance.create_restaurants_restaurants_post(restaurant)
        print("The response of DefaultApi->create_restaurants_restaurants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_restaurants_restaurants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**List[Restaurant]**](Restaurant.md)|  |

### Return type

[**List[Restaurant]**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_review_review_post**
> Review create_review_review_post(review)

Create Review

Create a Review

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review = openapi_client.Review() # Review |

    try:
        # Create Review
        api_response = api_instance.create_review_review_post(review)
        print("The response of DefaultApi->create_review_review_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_review_review_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Review**](Review.md)|  |

### Return type

[**Review**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reviews_reviews_post**
> List[Review] create_reviews_reviews_post(review)

Create Reviews

Create multiple Reviews

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review = [openapi_client.Review()] # List[Review] |

    try:
        # Create Reviews
        api_response = api_instance.create_reviews_reviews_post(review)
        print("The response of DefaultApi->create_reviews_reviews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_reviews_reviews_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**List[Review]**](Review.md)|  |

### Return type

[**List[Review]**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_user_post**
> User create_user_user_post(user)

Create User

Create a User

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = openapi_client.User() # User |

    try:
        # Create User
        api_response = api_instance.create_user_user_post(user)
        print("The response of DefaultApi->create_user_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_users_users_post**
> List[User] create_users_users_post(user)

Create Users

Create multiple Users

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = [openapi_client.User()] # List[User] |

    try:
        # Create Users
        api_response = api_instance.create_users_users_post(user)
        print("The response of DefaultApi->create_users_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_users_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**List[User]**](User.md)|  |

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservation_reservation_delete**
> Reservation delete_reservation_reservation_delete(reservation_id)

Delete Reservation

Delete a Reservation

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation_id = 'reservation_id_example' # str |

    try:
        # Delete Reservation
        api_response = api_instance.delete_reservation_reservation_delete(reservation_id)
        print("The response of DefaultApi->delete_reservation_reservation_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_reservation_reservation_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**|  |

### Return type

[**Reservation**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservations_reservations_delete**
> List[Reservation] delete_reservations_reservations_delete(request_body)

Delete Reservations

Delete multiple Reservations

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Reservations
        api_response = api_instance.delete_reservations_reservations_delete(request_body)
        print("The response of DefaultApi->delete_reservations_reservations_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_reservations_reservations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restaurant_restaurant_delete**
> Restaurant delete_restaurant_restaurant_delete(restaurant_id)

Delete Restaurant

Delete a Restaurant

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant_id = 'restaurant_id_example' # str |

    try:
        # Delete Restaurant
        api_response = api_instance.delete_restaurant_restaurant_delete(restaurant_id)
        print("The response of DefaultApi->delete_restaurant_restaurant_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_restaurant_restaurant_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant_id** | **str**|  |

### Return type

[**Restaurant**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restaurants_restaurants_delete**
> List[Restaurant] delete_restaurants_restaurants_delete(request_body)

Delete Restaurants

Delete multiple Restaurants

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Restaurants
        api_response = api_instance.delete_restaurants_restaurants_delete(request_body)
        print("The response of DefaultApi->delete_restaurants_restaurants_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_restaurants_restaurants_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

[**List[Restaurant]**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_review_review_delete**
> Review delete_review_review_delete(review_id)

Delete Review

Delete a Review

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_id = 'review_id_example' # str |

    try:
        # Delete Review
        api_response = api_instance.delete_review_review_delete(review_id)
        print("The response of DefaultApi->delete_review_review_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_review_review_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **str**|  |

### Return type

[**Review**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reviews_reviews_delete**
> List[Review] delete_reviews_reviews_delete(request_body)

Delete Reviews

Delete multiple Reviews

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Reviews
        api_response = api_instance.delete_reviews_reviews_delete(request_body)
        print("The response of DefaultApi->delete_reviews_reviews_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_reviews_reviews_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

[**List[Review]**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_user_delete**
> User delete_user_user_delete(user_id)

Delete User

Delete a User

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str |

    try:
        # Delete User
        api_response = api_instance.delete_user_user_delete(user_id)
        print("The response of DefaultApi->delete_user_user_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user_user_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_users_delete**
> List[User] delete_users_users_delete(request_body)

Delete Users

Delete multiple Users

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Users
        api_response = api_instance.delete_users_users_delete(request_body)
        print("The response of DefaultApi->delete_users_users_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_users_users_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation_reservation_get**
> Reservation get_reservation_reservation_get(reservation_id)

Get Reservation

Get a Reservation

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation_id = 'reservation_id_example' # str |

    try:
        # Get Reservation
        api_response = api_instance.get_reservation_reservation_get(reservation_id)
        print("The response of DefaultApi->get_reservation_reservation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_reservation_reservation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**|  |

### Return type

[**Reservation**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations_reservations_get**
> List[Reservation] get_reservations_reservations_get()

Get Reservations

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Reservations
        api_response = api_instance.get_reservations_reservations_get()
        print("The response of DefaultApi->get_reservations_reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_reservations_reservations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restaurant_restaurant_get**
> Restaurant get_restaurant_restaurant_get(restaurant_id)

Get Restaurant

Get a Restaurant

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant_id = 'restaurant_id_example' # str |

    try:
        # Get Restaurant
        api_response = api_instance.get_restaurant_restaurant_get(restaurant_id)
        print("The response of DefaultApi->get_restaurant_restaurant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_restaurant_restaurant_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant_id** | **str**|  |

### Return type

[**Restaurant**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restaurants_restaurants_get**
> List[Restaurant] get_restaurants_restaurants_get()

Get Restaurants

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Restaurants
        api_response = api_instance.get_restaurants_restaurants_get()
        print("The response of DefaultApi->get_restaurants_restaurants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_restaurants_restaurants_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Restaurant]**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_review_review_get**
> Review get_review_review_get(review_id)

Get Review

Get a Review

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_id = 'review_id_example' # str |

    try:
        # Get Review
        api_response = api_instance.get_review_review_get(review_id)
        print("The response of DefaultApi->get_review_review_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_review_review_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **str**|  |

### Return type

[**Review**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reviews_reviews_get**
> List[Review] get_reviews_reviews_get()

Get Reviews

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Reviews
        api_response = api_instance.get_reviews_reviews_get()
        print("The response of DefaultApi->get_reviews_reviews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_reviews_reviews_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Review]**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_user_get**
> User get_user_user_get(user_id)

Get User

Get a User

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str |

    try:
        # Get User
        api_response = api_instance.get_user_user_get(user_id)
        print("The response of DefaultApi->get_user_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_users_get**
> List[User] get_users_users_get()

Get Users

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Users
        api_response = api_instance.get_users_users_get()
        print("The response of DefaultApi->get_users_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> object root_get()

Root

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reservation_reservation_put**
> Reservation update_reservation_reservation_put(reservation)

Update Reservation

Update a Reservation

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Update Reservation
        api_response = api_instance.update_reservation_reservation_put(reservation)
        print("The response of DefaultApi->update_reservation_reservation_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_reservation_reservation_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**Reservation**](Reservation.md)|  |

### Return type

[**Reservation**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reservations_reservations_put**
> List[Reservation] update_reservations_reservations_put(reservation)

Update Reservations

Update multiple Reservations

### Example


```python
import openapi_client
from openapi_client.models.reservation import Reservation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Update Reservations
        api_response = api_instance.update_reservations_reservations_put(reservation)
        print("The response of DefaultApi->update_reservations_reservations_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_reservations_reservations_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**List[Reservation]**](Reservation.md)|  |

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restaurant_restaurant_put**
> Restaurant update_restaurant_restaurant_put(restaurant)

Update Restaurant

Update a Restaurant

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant |

    try:
        # Update Restaurant
        api_response = api_instance.update_restaurant_restaurant_put(restaurant)
        print("The response of DefaultApi->update_restaurant_restaurant_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_restaurant_restaurant_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**Restaurant**](Restaurant.md)|  |

### Return type

[**Restaurant**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restaurants_restaurants_put**
> List[Restaurant] update_restaurants_restaurants_put(restaurant)

Update Restaurants

Update multiple Restaurants

### Example


```python
import openapi_client
from openapi_client.models.restaurant import Restaurant
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] |

    try:
        # Update Restaurants
        api_response = api_instance.update_restaurants_restaurants_put(restaurant)
        print("The response of DefaultApi->update_restaurants_restaurants_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_restaurants_restaurants_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**List[Restaurant]**](Restaurant.md)|  |

### Return type

[**List[Restaurant]**](Restaurant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_review_review_put**
> Review update_review_review_put(review)

Update Review

Update a Review

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review = openapi_client.Review() # Review |

    try:
        # Update Review
        api_response = api_instance.update_review_review_put(review)
        print("The response of DefaultApi->update_review_review_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_review_review_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Review**](Review.md)|  |

### Return type

[**Review**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reviews_reviews_put**
> List[Review] update_reviews_reviews_put(review)

Update Reviews

Update multiple Reviews

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review = [openapi_client.Review()] # List[Review] |

    try:
        # Update Reviews
        api_response = api_instance.update_reviews_reviews_put(review)
        print("The response of DefaultApi->update_reviews_reviews_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_reviews_reviews_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**List[Review]**](Review.md)|  |

### Return type

[**List[Review]**](Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_user_put**
> User update_user_user_put(user)

Update User

Update a User

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = openapi_client.User() # User |

    try:
        # Update User
        api_response = api_instance.update_user_user_put(user)
        print("The response of DefaultApi->update_user_user_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user_user_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users_users_put**
> List[User] update_users_users_put(user)

Update Users

Update multiple Users

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user = [openapi_client.User()] # List[User] |

    try:
        # Update Users
        api_response = api_instance.update_users_users_put(user)
        print("The response of DefaultApi->update_users_users_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_users_users_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**List[User]**](User.md)|  |

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
