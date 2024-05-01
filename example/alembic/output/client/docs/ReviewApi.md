# openapi_client.ReviewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_review_async_review_async_post**](ReviewApi.md#create_review_async_review_async_post) | **POST** /review/async | Create Review Async
[**create_review_review_post**](ReviewApi.md#create_review_review_post) | **POST** /review | Create Review
[**create_reviews_async_reviews_async_post**](ReviewApi.md#create_reviews_async_reviews_async_post) | **POST** /reviews/async | Create Reviews Async
[**create_reviews_reviews_post**](ReviewApi.md#create_reviews_reviews_post) | **POST** /reviews | Create Reviews
[**delete_review_async_review_async_delete**](ReviewApi.md#delete_review_async_review_async_delete) | **DELETE** /review/async | Delete Review Async
[**delete_review_review_delete**](ReviewApi.md#delete_review_review_delete) | **DELETE** /review | Delete Review
[**delete_reviews_async_reviews_async_delete**](ReviewApi.md#delete_reviews_async_reviews_async_delete) | **DELETE** /reviews/async | Delete Reviews Async
[**delete_reviews_reviews_delete**](ReviewApi.md#delete_reviews_reviews_delete) | **DELETE** /reviews | Delete Reviews
[**get_review_review_get**](ReviewApi.md#get_review_review_get) | **GET** /review | Get Review
[**get_reviews_reviews_get**](ReviewApi.md#get_reviews_reviews_get) | **GET** /reviews | Get Reviews
[**query_review_review_query_post**](ReviewApi.md#query_review_review_query_post) | **POST** /review/query | Query Review
[**update_review_async_review_async_put**](ReviewApi.md#update_review_async_review_async_put) | **PUT** /review/async | Update Review Async
[**update_review_review_put**](ReviewApi.md#update_review_review_put) | **PUT** /review | Update Review
[**update_reviews_async_reviews_async_put**](ReviewApi.md#update_reviews_async_reviews_async_put) | **PUT** /reviews/async | Update Reviews Async
[**update_reviews_reviews_put**](ReviewApi.md#update_reviews_reviews_put) | **PUT** /reviews | Update Reviews


# **create_review_async_review_async_post**
> object create_review_async_review_async_post(review)

Create Review Async

Create a Review asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = openapi_client.Review() # Review | 

    try:
        # Create Review Async
        api_response = api_instance.create_review_async_review_async_post(review)
        print("The response of ReviewApi->create_review_async_review_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->create_review_async_review_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Review**](Review.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = openapi_client.Review() # Review | 

    try:
        # Create Review
        api_response = api_instance.create_review_review_post(review)
        print("The response of ReviewApi->create_review_review_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->create_review_review_post: %s\n" % e)
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

# **create_reviews_async_reviews_async_post**
> object create_reviews_async_reviews_async_post(review)

Create Reviews Async

Create multiple Reviews asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = [openapi_client.Review()] # List[Review] | 

    try:
        # Create Reviews Async
        api_response = api_instance.create_reviews_async_reviews_async_post(review)
        print("The response of ReviewApi->create_reviews_async_reviews_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->create_reviews_async_reviews_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**List[Review]**](Review.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = [openapi_client.Review()] # List[Review] | 

    try:
        # Create Reviews
        api_response = api_instance.create_reviews_reviews_post(review)
        print("The response of ReviewApi->create_reviews_reviews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->create_reviews_reviews_post: %s\n" % e)
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

# **delete_review_async_review_async_delete**
> object delete_review_async_review_async_delete(review_id)

Delete Review Async

Delete a Review asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    review_id = 56 # int | 

    try:
        # Delete Review Async
        api_response = api_instance.delete_review_async_review_async_delete(review_id)
        print("The response of ReviewApi->delete_review_async_review_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->delete_review_async_review_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **int**|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review_id = 56 # int | 

    try:
        # Delete Review
        api_response = api_instance.delete_review_review_delete(review_id)
        print("The response of ReviewApi->delete_review_review_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->delete_review_review_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **int**|  | 

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

# **delete_reviews_async_reviews_async_delete**
> object delete_reviews_async_reviews_async_delete(request_body)

Delete Reviews Async

Delete multiple Reviews asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Delete Reviews Async
        api_response = api_instance.delete_reviews_async_reviews_async_delete(request_body)
        print("The response of ReviewApi->delete_reviews_async_reviews_async_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->delete_reviews_async_reviews_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Delete Reviews
        api_response = api_instance.delete_reviews_reviews_delete(request_body)
        print("The response of ReviewApi->delete_reviews_reviews_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->delete_reviews_reviews_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review_id = 'review_id_example' # str | 

    try:
        # Get Review
        api_response = api_instance.get_review_review_get(review_id)
        print("The response of ReviewApi->get_review_review_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->get_review_review_get: %s\n" % e)
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

Get all Reviews

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
    api_instance = openapi_client.ReviewApi(api_client)

    try:
        # Get Reviews
        api_response = api_instance.get_reviews_reviews_get()
        print("The response of ReviewApi->get_reviews_reviews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->get_reviews_reviews_get: %s\n" % e)
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

# **query_review_review_query_post**
> List[Review] query_review_review_query_post(review_query)

Query Review

Query Reviews

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.models.review_query import ReviewQuery
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
    api_instance = openapi_client.ReviewApi(api_client)
    review_query = openapi_client.ReviewQuery() # ReviewQuery | 

    try:
        # Query Review
        api_response = api_instance.query_review_review_query_post(review_query)
        print("The response of ReviewApi->query_review_review_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->query_review_review_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_query** | [**ReviewQuery**](ReviewQuery.md)|  | 

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

# **update_review_async_review_async_put**
> object update_review_async_review_async_put(review)

Update Review Async

Update a Review asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = openapi_client.Review() # Review | 

    try:
        # Update Review Async
        api_response = api_instance.update_review_async_review_async_put(review)
        print("The response of ReviewApi->update_review_async_review_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->update_review_async_review_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Review**](Review.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = openapi_client.Review() # Review | 

    try:
        # Update Review
        api_response = api_instance.update_review_review_put(review)
        print("The response of ReviewApi->update_review_review_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->update_review_review_put: %s\n" % e)
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

# **update_reviews_async_reviews_async_put**
> object update_reviews_async_reviews_async_put(review)

Update Reviews Async

Update multiple Reviews asynchronously

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = [openapi_client.Review()] # List[Review] | 

    try:
        # Update Reviews Async
        api_response = api_instance.update_reviews_async_reviews_async_put(review)
        print("The response of ReviewApi->update_reviews_async_reviews_async_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->update_reviews_async_reviews_async_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**List[Review]**](Review.md)|  | 

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
    api_instance = openapi_client.ReviewApi(api_client)
    review = [openapi_client.Review()] # List[Review] | 

    try:
        # Update Reviews
        api_response = api_instance.update_reviews_reviews_put(review)
        print("The response of ReviewApi->update_reviews_reviews_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->update_reviews_reviews_put: %s\n" % e)
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

