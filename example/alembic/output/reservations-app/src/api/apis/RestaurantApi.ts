/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import * as runtime from "../runtime";
import type {
  HTTPValidationError,
  Restaurant,
  RestaurantQuery,
} from "../models/index";
import {
  HTTPValidationErrorFromJSON,
  HTTPValidationErrorToJSON,
  RestaurantFromJSON,
  RestaurantToJSON,
  RestaurantQueryFromJSON,
  RestaurantQueryToJSON,
} from "../models/index";

export interface CreateRestaurantAsyncRestaurantAsyncPostRequest {
  restaurant: Restaurant;
}

export interface CreateRestaurantRestaurantPostRequest {
  restaurant: Restaurant;
}

export interface CreateRestaurantsAsyncRestaurantsAsyncPostRequest {
  restaurant: Array<Restaurant>;
}

export interface CreateRestaurantsRestaurantsPostRequest {
  restaurant: Array<Restaurant>;
}

export interface DeleteRestaurantAsyncRestaurantAsyncDeleteRequest {
  restaurantId: number;
}

export interface DeleteRestaurantRestaurantDeleteRequest {
  restaurantId: number;
}

export interface DeleteRestaurantsAsyncRestaurantsAsyncDeleteRequest {
  requestBody: Array<number>;
}

export interface DeleteRestaurantsRestaurantsDeleteRequest {
  requestBody: Array<number>;
}

export interface GetRestaurantRestaurantGetRequest {
  restaurantId: string;
}

export interface QueryRestaurantRestaurantQueryPostRequest {
  restaurantQuery: RestaurantQuery;
}

export interface UpdateRestaurantAsyncRestaurantAsyncPutRequest {
  restaurant: Restaurant;
}

export interface UpdateRestaurantRestaurantPutRequest {
  restaurant: Restaurant;
}

export interface UpdateRestaurantsAsyncRestaurantsAsyncPutRequest {
  restaurant: Array<Restaurant>;
}

export interface UpdateRestaurantsRestaurantsPutRequest {
  restaurant: Array<Restaurant>;
}

/**
 *
 */
export class RestaurantApi extends runtime.BaseAPI {
  /**
   * Create a Restaurant asynchronously
   * Create Restaurant Async
   */
  async createRestaurantAsyncRestaurantAsyncPostRaw(
    requestParameters: CreateRestaurantAsyncRestaurantAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling createRestaurantAsyncRestaurantAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurant/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: RestaurantToJSON(requestParameters["restaurant"]),
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Create a Restaurant asynchronously
   * Create Restaurant Async
   */
  async createRestaurantAsyncRestaurantAsyncPost(
    requestParameters: CreateRestaurantAsyncRestaurantAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createRestaurantAsyncRestaurantAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create a Restaurant
   * Create Restaurant
   */
  async createRestaurantRestaurantPostRaw(
    requestParameters: CreateRestaurantRestaurantPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Restaurant>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling createRestaurantRestaurantPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurant`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: RestaurantToJSON(requestParameters["restaurant"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      RestaurantFromJSON(jsonValue),
    );
  }

  /**
   * Create a Restaurant
   * Create Restaurant
   */
  async createRestaurantRestaurantPost(
    requestParameters: CreateRestaurantRestaurantPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Restaurant> {
    const response = await this.createRestaurantRestaurantPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Restaurants asynchronously
   * Create Restaurants Async
   */
  async createRestaurantsAsyncRestaurantsAsyncPostRaw(
    requestParameters: CreateRestaurantsAsyncRestaurantsAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling createRestaurantsAsyncRestaurantsAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["restaurant"]!.map(RestaurantToJSON),
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Create multiple Restaurants asynchronously
   * Create Restaurants Async
   */
  async createRestaurantsAsyncRestaurantsAsyncPost(
    requestParameters: CreateRestaurantsAsyncRestaurantsAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createRestaurantsAsyncRestaurantsAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Restaurants
   * Create Restaurants
   */
  async createRestaurantsRestaurantsPostRaw(
    requestParameters: CreateRestaurantsRestaurantsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Restaurant>>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling createRestaurantsRestaurantsPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["restaurant"]!.map(RestaurantToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(RestaurantFromJSON),
    );
  }

  /**
   * Create multiple Restaurants
   * Create Restaurants
   */
  async createRestaurantsRestaurantsPost(
    requestParameters: CreateRestaurantsRestaurantsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Restaurant>> {
    const response = await this.createRestaurantsRestaurantsPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a Restaurant asynchronously
   * Delete Restaurant Async
   */
  async deleteRestaurantAsyncRestaurantAsyncDeleteRaw(
    requestParameters: DeleteRestaurantAsyncRestaurantAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["restaurantId"] == null) {
      throw new runtime.RequiredError(
        "restaurantId",
        'Required parameter "restaurantId" was null or undefined when calling deleteRestaurantAsyncRestaurantAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["restaurantId"] != null) {
      queryParameters["restaurant_id"] = requestParameters["restaurantId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/restaurant/async`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Delete a Restaurant asynchronously
   * Delete Restaurant Async
   */
  async deleteRestaurantAsyncRestaurantAsyncDelete(
    requestParameters: DeleteRestaurantAsyncRestaurantAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteRestaurantAsyncRestaurantAsyncDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a Restaurant
   * Delete Restaurant
   */
  async deleteRestaurantRestaurantDeleteRaw(
    requestParameters: DeleteRestaurantRestaurantDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Restaurant>> {
    if (requestParameters["restaurantId"] == null) {
      throw new runtime.RequiredError(
        "restaurantId",
        'Required parameter "restaurantId" was null or undefined when calling deleteRestaurantRestaurantDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["restaurantId"] != null) {
      queryParameters["restaurant_id"] = requestParameters["restaurantId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/restaurant`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      RestaurantFromJSON(jsonValue),
    );
  }

  /**
   * Delete a Restaurant
   * Delete Restaurant
   */
  async deleteRestaurantRestaurantDelete(
    requestParameters: DeleteRestaurantRestaurantDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Restaurant> {
    const response = await this.deleteRestaurantRestaurantDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Restaurants asynchronously
   * Delete Restaurants Async
   */
  async deleteRestaurantsAsyncRestaurantsAsyncDeleteRaw(
    requestParameters: DeleteRestaurantsAsyncRestaurantsAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteRestaurantsAsyncRestaurantsAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants/async`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["requestBody"],
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Delete multiple Restaurants asynchronously
   * Delete Restaurants Async
   */
  async deleteRestaurantsAsyncRestaurantsAsyncDelete(
    requestParameters: DeleteRestaurantsAsyncRestaurantsAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteRestaurantsAsyncRestaurantsAsyncDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Restaurants
   * Delete Restaurants
   */
  async deleteRestaurantsRestaurantsDeleteRaw(
    requestParameters: DeleteRestaurantsRestaurantsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Restaurant>>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteRestaurantsRestaurantsDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["requestBody"],
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(RestaurantFromJSON),
    );
  }

  /**
   * Delete multiple Restaurants
   * Delete Restaurants
   */
  async deleteRestaurantsRestaurantsDelete(
    requestParameters: DeleteRestaurantsRestaurantsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Restaurant>> {
    const response = await this.deleteRestaurantsRestaurantsDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get a Restaurant
   * Get Restaurant
   */
  async getRestaurantRestaurantGetRaw(
    requestParameters: GetRestaurantRestaurantGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Restaurant>> {
    if (requestParameters["restaurantId"] == null) {
      throw new runtime.RequiredError(
        "restaurantId",
        'Required parameter "restaurantId" was null or undefined when calling getRestaurantRestaurantGet().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["restaurantId"] != null) {
      queryParameters["restaurant_id"] = requestParameters["restaurantId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/restaurant`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      RestaurantFromJSON(jsonValue),
    );
  }

  /**
   * Get a Restaurant
   * Get Restaurant
   */
  async getRestaurantRestaurantGet(
    requestParameters: GetRestaurantRestaurantGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Restaurant> {
    const response = await this.getRestaurantRestaurantGetRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get all Restaurants
   * Get Restaurants
   */
  async getRestaurantsRestaurantsGetRaw(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Restaurant>>> {
    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/restaurants`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(RestaurantFromJSON),
    );
  }

  /**
   * Get all Restaurants
   * Get Restaurants
   */
  async getRestaurantsRestaurantsGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Restaurant>> {
    const response = await this.getRestaurantsRestaurantsGetRaw(initOverrides);
    return await response.value();
  }

  /**
   * Query Restaurants
   * Query Restaurant
   */
  async queryRestaurantRestaurantQueryPostRaw(
    requestParameters: QueryRestaurantRestaurantQueryPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Restaurant>>> {
    if (requestParameters["restaurantQuery"] == null) {
      throw new runtime.RequiredError(
        "restaurantQuery",
        'Required parameter "restaurantQuery" was null or undefined when calling queryRestaurantRestaurantQueryPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurant/query`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: RestaurantQueryToJSON(requestParameters["restaurantQuery"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(RestaurantFromJSON),
    );
  }

  /**
   * Query Restaurants
   * Query Restaurant
   */
  async queryRestaurantRestaurantQueryPost(
    requestParameters: QueryRestaurantRestaurantQueryPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Restaurant>> {
    const response = await this.queryRestaurantRestaurantQueryPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update a Restaurant asynchronously
   * Update Restaurant Async
   */
  async updateRestaurantAsyncRestaurantAsyncPutRaw(
    requestParameters: UpdateRestaurantAsyncRestaurantAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling updateRestaurantAsyncRestaurantAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurant/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: RestaurantToJSON(requestParameters["restaurant"]),
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Update a Restaurant asynchronously
   * Update Restaurant Async
   */
  async updateRestaurantAsyncRestaurantAsyncPut(
    requestParameters: UpdateRestaurantAsyncRestaurantAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateRestaurantAsyncRestaurantAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update a Restaurant
   * Update Restaurant
   */
  async updateRestaurantRestaurantPutRaw(
    requestParameters: UpdateRestaurantRestaurantPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Restaurant>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling updateRestaurantRestaurantPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurant`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: RestaurantToJSON(requestParameters["restaurant"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      RestaurantFromJSON(jsonValue),
    );
  }

  /**
   * Update a Restaurant
   * Update Restaurant
   */
  async updateRestaurantRestaurantPut(
    requestParameters: UpdateRestaurantRestaurantPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Restaurant> {
    const response = await this.updateRestaurantRestaurantPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Restaurants asynchronously
   * Update Restaurants Async
   */
  async updateRestaurantsAsyncRestaurantsAsyncPutRaw(
    requestParameters: UpdateRestaurantsAsyncRestaurantsAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling updateRestaurantsAsyncRestaurantsAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["restaurant"]!.map(RestaurantToJSON),
      },
      initOverrides,
    );

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Update multiple Restaurants asynchronously
   * Update Restaurants Async
   */
  async updateRestaurantsAsyncRestaurantsAsyncPut(
    requestParameters: UpdateRestaurantsAsyncRestaurantsAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateRestaurantsAsyncRestaurantsAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Restaurants
   * Update Restaurants
   */
  async updateRestaurantsRestaurantsPutRaw(
    requestParameters: UpdateRestaurantsRestaurantsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Restaurant>>> {
    if (requestParameters["restaurant"] == null) {
      throw new runtime.RequiredError(
        "restaurant",
        'Required parameter "restaurant" was null or undefined when calling updateRestaurantsRestaurantsPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/restaurants`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["restaurant"]!.map(RestaurantToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(RestaurantFromJSON),
    );
  }

  /**
   * Update multiple Restaurants
   * Update Restaurants
   */
  async updateRestaurantsRestaurantsPut(
    requestParameters: UpdateRestaurantsRestaurantsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Restaurant>> {
    const response = await this.updateRestaurantsRestaurantsPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }
}
