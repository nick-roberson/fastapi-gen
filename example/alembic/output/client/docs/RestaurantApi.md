# openapi_client.RestaurantApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_restaurant_async_restaurant_async_post**](RestaurantApi.md#create_restaurant_async_restaurant_async_post) | **POST** /restaurant/async | Create Restaurant Async
[**create_restaurant_restaurant_post**](RestaurantApi.md#create_restaurant_restaurant_post) | **POST** /restaurant | Create Restaurant
[**create_restaurants_async_restaurants_async_post**](RestaurantApi.md#create_restaurants_async_restaurants_async_post) | **POST** /restaurants/async | Create Restaurants Async
[**create_restaurants_restaurants_post**](RestaurantApi.md#create_restaurants_restaurants_post) | **POST** /restaurants | Create Restaurants
[**delete_restaurant_async_restaurant_async_delete**](RestaurantApi.md#delete_restaurant_async_restaurant_async_delete) | **DELETE** /restaurant/async | Delete Restaurant Async
[**delete_restaurant_restaurant_delete**](RestaurantApi.md#delete_restaurant_restaurant_delete) | **DELETE** /restaurant | Delete Restaurant
[**delete_restaurants_async_restaurants_async_delete**](RestaurantApi.md#delete_restaurants_async_restaurants_async_delete) | **DELETE** /restaurants/async | Delete Restaurants Async
[**delete_restaurants_restaurants_delete**](RestaurantApi.md#delete_restaurants_restaurants_delete) | **DELETE** /restaurants | Delete Restaurants
[**get_restaurant_restaurant_get**](RestaurantApi.md#get_restaurant_restaurant_get) | **GET** /restaurant | Get Restaurant
[**get_restaurants_restaurants_get**](RestaurantApi.md#get_restaurants_restaurants_get) | **GET** /restaurants | Get Restaurants
[**update_restaurant_async_restaurant_async_put**](RestaurantApi.md#update_restaurant_async_restaurant_async_put) | **PUT** /restaurant/async | Update Restaurant Async
[**update_restaurant_restaurant_put**](RestaurantApi.md#update_restaurant_restaurant_put) | **PUT** /restaurant | Update Restaurant
[**update_restaurants_async_restaurants_async_put**](RestaurantApi.md#update_restaurants_async_restaurants_async_put) | **PUT** /restaurants/async | Update Restaurants Async
[**update_restaurants_restaurants_put**](RestaurantApi.md#update_restaurants_restaurants_put) | **PUT** /restaurants | Update Restaurants


# **create_restaurant_async_restaurant_async_post**
> object create_restaurant_async_restaurant_async_post(restaurant)

Create Restaurant Async

Create a Restaurant asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant | 

    try:
        # Create Restaurant Async
        api_response = api_instance.create_restaurant_async_restaurant_async_post(restaurant)
        print("The response of RestaurantApi->create_restaurant_async_restaurant_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->create_restaurant_async_restaurant_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**Restaurant**](Restaurant.md)|  | 

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant | 

    try:
        # Create Restaurant
        api_response = api_instance.create_restaurant_restaurant_post(restaurant)
        print("The response of RestaurantApi->create_restaurant_restaurant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->create_restaurant_restaurant_post: %s\n" % e)
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

# **create_restaurants_async_restaurants_async_post**
> object create_restaurants_async_restaurants_async_post(restaurant)

Create Restaurants Async

Create multiple Restaurants asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] | 

    try:
        # Create Restaurants Async
        api_response = api_instance.create_restaurants_async_restaurants_async_post(restaurant)
        print("The response of RestaurantApi->create_restaurants_async_restaurants_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->create_restaurants_async_restaurants_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**List[Restaurant]**](Restaurant.md)|  | 

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] | 

    try:
        # Create Restaurants
        api_response = api_instance.create_restaurants_restaurants_post(restaurant)
        print("The response of RestaurantApi->create_restaurants_restaurants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->create_restaurants_restaurants_post: %s\n" % e)
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

# **delete_restaurant_async_restaurant_async_delete**
> object delete_restaurant_async_restaurant_async_delete(restaurant_id)

Delete Restaurant Async

Delete a Restaurant asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant_id = 'restaurant_id_example' # str | 

    try:
        # Delete Restaurant Async
        api_response = api_instance.delete_restaurant_async_restaurant_async_delete(restaurant_id)
        print("The response of RestaurantApi->delete_restaurant_async_restaurant_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->delete_restaurant_async_restaurant_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant_id** | **str**|  | 

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant_id = 'restaurant_id_example' # str | 

    try:
        # Delete Restaurant
        api_response = api_instance.delete_restaurant_restaurant_delete(restaurant_id)
        print("The response of RestaurantApi->delete_restaurant_restaurant_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->delete_restaurant_restaurant_delete: %s\n" % e)
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

# **delete_restaurants_async_restaurants_async_delete**
> object delete_restaurants_async_restaurants_async_delete(request_body)

Delete Restaurants Async

Delete multiple Restaurants asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete Restaurants Async
        api_response = api_instance.delete_restaurants_async_restaurants_async_delete(request_body)
        print("The response of RestaurantApi->delete_restaurants_async_restaurants_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->delete_restaurants_async_restaurants_async_delete: %s\n" % e)
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
    api_instance = openapi_client.RestaurantApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete Restaurants
        api_response = api_instance.delete_restaurants_restaurants_delete(request_body)
        print("The response of RestaurantApi->delete_restaurants_restaurants_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->delete_restaurants_restaurants_delete: %s\n" % e)
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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant_id = 'restaurant_id_example' # str | 

    try:
        # Get Restaurant
        api_response = api_instance.get_restaurant_restaurant_get(restaurant_id)
        print("The response of RestaurantApi->get_restaurant_restaurant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->get_restaurant_restaurant_get: %s\n" % e)
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

Get all Restaurants

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
    api_instance = openapi_client.RestaurantApi(api_client)

    try:
        # Get Restaurants
        api_response = api_instance.get_restaurants_restaurants_get()
        print("The response of RestaurantApi->get_restaurants_restaurants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->get_restaurants_restaurants_get: %s\n" % e)
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

# **update_restaurant_async_restaurant_async_put**
> object update_restaurant_async_restaurant_async_put(restaurant)

Update Restaurant Async

Update a Restaurant asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant | 

    try:
        # Update Restaurant Async
        api_response = api_instance.update_restaurant_async_restaurant_async_put(restaurant)
        print("The response of RestaurantApi->update_restaurant_async_restaurant_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->update_restaurant_async_restaurant_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**Restaurant**](Restaurant.md)|  | 

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = openapi_client.Restaurant() # Restaurant | 

    try:
        # Update Restaurant
        api_response = api_instance.update_restaurant_restaurant_put(restaurant)
        print("The response of RestaurantApi->update_restaurant_restaurant_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->update_restaurant_restaurant_put: %s\n" % e)
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

# **update_restaurants_async_restaurants_async_put**
> object update_restaurants_async_restaurants_async_put(restaurant)

Update Restaurants Async

Update multiple Restaurants asynchronously

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] | 

    try:
        # Update Restaurants Async
        api_response = api_instance.update_restaurants_async_restaurants_async_put(restaurant)
        print("The response of RestaurantApi->update_restaurants_async_restaurants_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->update_restaurants_async_restaurants_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurant** | [**List[Restaurant]**](Restaurant.md)|  | 

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
    api_instance = openapi_client.RestaurantApi(api_client)
    restaurant = [openapi_client.Restaurant()] # List[Restaurant] | 

    try:
        # Update Restaurants
        api_response = api_instance.update_restaurants_restaurants_put(restaurant)
        print("The response of RestaurantApi->update_restaurants_restaurants_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantApi->update_restaurants_restaurants_put: %s\n" % e)
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

