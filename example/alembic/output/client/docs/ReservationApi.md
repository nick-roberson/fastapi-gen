# openapi_client.ReservationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation_async_reservation_async_post**](ReservationApi.md#create_reservation_async_reservation_async_post) | **POST** /reservation/async | Create Reservation Async
[**create_reservation_reservation_post**](ReservationApi.md#create_reservation_reservation_post) | **POST** /reservation | Create Reservation
[**create_reservations_async_reservations_async_post**](ReservationApi.md#create_reservations_async_reservations_async_post) | **POST** /reservations/async | Create Reservations Async
[**create_reservations_reservations_post**](ReservationApi.md#create_reservations_reservations_post) | **POST** /reservations | Create Reservations
[**delete_reservation_async_reservation_async_delete**](ReservationApi.md#delete_reservation_async_reservation_async_delete) | **DELETE** /reservation/async | Delete Reservation Async
[**delete_reservation_reservation_delete**](ReservationApi.md#delete_reservation_reservation_delete) | **DELETE** /reservation | Delete Reservation
[**delete_reservations_async_reservations_async_delete**](ReservationApi.md#delete_reservations_async_reservations_async_delete) | **DELETE** /reservations/async | Delete Reservations Async
[**delete_reservations_reservations_delete**](ReservationApi.md#delete_reservations_reservations_delete) | **DELETE** /reservations | Delete Reservations
[**get_reservation_reservation_get**](ReservationApi.md#get_reservation_reservation_get) | **GET** /reservation | Get Reservation
[**get_reservations_reservations_get**](ReservationApi.md#get_reservations_reservations_get) | **GET** /reservations | Get Reservations
[**update_reservation_async_reservation_async_put**](ReservationApi.md#update_reservation_async_reservation_async_put) | **PUT** /reservation/async | Update Reservation Async
[**update_reservation_reservation_put**](ReservationApi.md#update_reservation_reservation_put) | **PUT** /reservation | Update Reservation
[**update_reservations_async_reservations_async_put**](ReservationApi.md#update_reservations_async_reservations_async_put) | **PUT** /reservations/async | Update Reservations Async
[**update_reservations_reservations_put**](ReservationApi.md#update_reservations_reservations_put) | **PUT** /reservations | Update Reservations


# **create_reservation_async_reservation_async_post**
> object create_reservation_async_reservation_async_post(reservation)

Create Reservation Async

Create a Reservation asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Create Reservation Async
        api_response = api_instance.create_reservation_async_reservation_async_post(reservation)
        print("The response of ReservationApi->create_reservation_async_reservation_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->create_reservation_async_reservation_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**Reservation**](Reservation.md)|  |

### Return type

**object**

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Create Reservation
        api_response = api_instance.create_reservation_reservation_post(reservation)
        print("The response of ReservationApi->create_reservation_reservation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->create_reservation_reservation_post: %s\n" % e)
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

# **create_reservations_async_reservations_async_post**
> object create_reservations_async_reservations_async_post(reservation)

Create Reservations Async

Create multiple Reservations asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Create Reservations Async
        api_response = api_instance.create_reservations_async_reservations_async_post(reservation)
        print("The response of ReservationApi->create_reservations_async_reservations_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->create_reservations_async_reservations_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**List[Reservation]**](Reservation.md)|  |

### Return type

**object**

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Create Reservations
        api_response = api_instance.create_reservations_reservations_post(reservation)
        print("The response of ReservationApi->create_reservations_reservations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->create_reservations_reservations_post: %s\n" % e)
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

# **delete_reservation_async_reservation_async_delete**
> object delete_reservation_async_reservation_async_delete(reservation_id)

Delete Reservation Async

Delete a Reservation asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str |

    try:
        # Delete Reservation Async
        api_response = api_instance.delete_reservation_async_reservation_async_delete(reservation_id)
        print("The response of ReservationApi->delete_reservation_async_reservation_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->delete_reservation_async_reservation_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**|  |

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str |

    try:
        # Delete Reservation
        api_response = api_instance.delete_reservation_reservation_delete(reservation_id)
        print("The response of ReservationApi->delete_reservation_reservation_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->delete_reservation_reservation_delete: %s\n" % e)
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

# **delete_reservations_async_reservations_async_delete**
> object delete_reservations_async_reservations_async_delete(request_body)

Delete Reservations Async

Delete multiple Reservations asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Reservations Async
        api_response = api_instance.delete_reservations_async_reservations_async_delete(request_body)
        print("The response of ReservationApi->delete_reservations_async_reservations_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->delete_reservations_async_reservations_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

**object**

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
    api_instance = openapi_client.ReservationApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Delete Reservations
        api_response = api_instance.delete_reservations_reservations_delete(request_body)
        print("The response of ReservationApi->delete_reservations_reservations_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->delete_reservations_reservations_delete: %s\n" % e)
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_id = 'reservation_id_example' # str |

    try:
        # Get Reservation
        api_response = api_instance.get_reservation_reservation_get(reservation_id)
        print("The response of ReservationApi->get_reservation_reservation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservation_reservation_get: %s\n" % e)
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

Get all Reservations

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
    api_instance = openapi_client.ReservationApi(api_client)

    try:
        # Get Reservations
        api_response = api_instance.get_reservations_reservations_get()
        print("The response of ReservationApi->get_reservations_reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservations_reservations_get: %s\n" % e)
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

# **update_reservation_async_reservation_async_put**
> object update_reservation_async_reservation_async_put(reservation)

Update Reservation Async

Update a Reservation asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Update Reservation Async
        api_response = api_instance.update_reservation_async_reservation_async_put(reservation)
        print("The response of ReservationApi->update_reservation_async_reservation_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->update_reservation_async_reservation_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**Reservation**](Reservation.md)|  |

### Return type

**object**

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = openapi_client.Reservation() # Reservation |

    try:
        # Update Reservation
        api_response = api_instance.update_reservation_reservation_put(reservation)
        print("The response of ReservationApi->update_reservation_reservation_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->update_reservation_reservation_put: %s\n" % e)
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

# **update_reservations_async_reservations_async_put**
> object update_reservations_async_reservations_async_put(reservation)

Update Reservations Async

Update multiple Reservations asynchronously

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Update Reservations Async
        api_response = api_instance.update_reservations_async_reservations_async_put(reservation)
        print("The response of ReservationApi->update_reservations_async_reservations_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->update_reservations_async_reservations_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | [**List[Reservation]**](Reservation.md)|  |

### Return type

**object**

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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation = [openapi_client.Reservation()] # List[Reservation] |

    try:
        # Update Reservations
        api_response = api_instance.update_reservations_reservations_put(reservation)
        print("The response of ReservationApi->update_reservations_reservations_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->update_reservations_reservations_put: %s\n" % e)
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
