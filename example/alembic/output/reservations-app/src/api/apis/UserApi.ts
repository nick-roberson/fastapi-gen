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
import type { HTTPValidationError, User, UserQuery } from "../models/index";
import {
  HTTPValidationErrorFromJSON,
  HTTPValidationErrorToJSON,
  UserFromJSON,
  UserToJSON,
  UserQueryFromJSON,
  UserQueryToJSON,
} from "../models/index";

export interface CreateUserAsyncUserAsyncPostRequest {
  user: User;
}

export interface CreateUserUserPostRequest {
  user: User;
}

export interface CreateUsersAsyncUsersAsyncPostRequest {
  user: Array<User>;
}

export interface CreateUsersUsersPostRequest {
  user: Array<User>;
}

export interface DeleteUserAsyncUserAsyncDeleteRequest {
  userId: number;
}

export interface DeleteUserUserDeleteRequest {
  userId: number;
}

export interface DeleteUsersAsyncUsersAsyncDeleteRequest {
  requestBody: Array<number>;
}

export interface DeleteUsersUsersDeleteRequest {
  requestBody: Array<number>;
}

export interface GetUserUserGetRequest {
  userId: string;
}

export interface QueryUserUserQueryPostRequest {
  userQuery: UserQuery;
}

export interface UpdateUserAsyncUserAsyncPutRequest {
  user: User;
}

export interface UpdateUserUserPutRequest {
  user: User;
}

export interface UpdateUsersAsyncUsersAsyncPutRequest {
  user: Array<User>;
}

export interface UpdateUsersUsersPutRequest {
  user: Array<User>;
}

/**
 *
 */
export class UserApi extends runtime.BaseAPI {
  /**
   * Create a User asynchronously
   * Create User Async
   */
  async createUserAsyncUserAsyncPostRaw(
    requestParameters: CreateUserAsyncUserAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling createUserAsyncUserAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/user/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: UserToJSON(requestParameters["user"]),
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
   * Create a User asynchronously
   * Create User Async
   */
  async createUserAsyncUserAsyncPost(
    requestParameters: CreateUserAsyncUserAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createUserAsyncUserAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create a User
   * Create User
   */
  async createUserUserPostRaw(
    requestParameters: CreateUserUserPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<User>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling createUserUserPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/user`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: UserToJSON(requestParameters["user"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      UserFromJSON(jsonValue),
    );
  }

  /**
   * Create a User
   * Create User
   */
  async createUserUserPost(
    requestParameters: CreateUserUserPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<User> {
    const response = await this.createUserUserPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Users asynchronously
   * Create Users Async
   */
  async createUsersAsyncUsersAsyncPostRaw(
    requestParameters: CreateUsersAsyncUsersAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling createUsersAsyncUsersAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["user"]!.map(UserToJSON),
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
   * Create multiple Users asynchronously
   * Create Users Async
   */
  async createUsersAsyncUsersAsyncPost(
    requestParameters: CreateUsersAsyncUsersAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createUsersAsyncUsersAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Users
   * Create Users
   */
  async createUsersUsersPostRaw(
    requestParameters: CreateUsersUsersPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<User>>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling createUsersUsersPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["user"]!.map(UserToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(UserFromJSON),
    );
  }

  /**
   * Create multiple Users
   * Create Users
   */
  async createUsersUsersPost(
    requestParameters: CreateUsersUsersPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.createUsersUsersPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a User asynchronously
   * Delete User Async
   */
  async deleteUserAsyncUserAsyncDeleteRaw(
    requestParameters: DeleteUserAsyncUserAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["userId"] == null) {
      throw new runtime.RequiredError(
        "userId",
        'Required parameter "userId" was null or undefined when calling deleteUserAsyncUserAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["userId"] != null) {
      queryParameters["user_id"] = requestParameters["userId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/user/async`,
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
   * Delete a User asynchronously
   * Delete User Async
   */
  async deleteUserAsyncUserAsyncDelete(
    requestParameters: DeleteUserAsyncUserAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteUserAsyncUserAsyncDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a User
   * Delete User
   */
  async deleteUserUserDeleteRaw(
    requestParameters: DeleteUserUserDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<User>> {
    if (requestParameters["userId"] == null) {
      throw new runtime.RequiredError(
        "userId",
        'Required parameter "userId" was null or undefined when calling deleteUserUserDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["userId"] != null) {
      queryParameters["user_id"] = requestParameters["userId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/user`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      UserFromJSON(jsonValue),
    );
  }

  /**
   * Delete a User
   * Delete User
   */
  async deleteUserUserDelete(
    requestParameters: DeleteUserUserDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<User> {
    const response = await this.deleteUserUserDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Users asynchronously
   * Delete Users Async
   */
  async deleteUsersAsyncUsersAsyncDeleteRaw(
    requestParameters: DeleteUsersAsyncUsersAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteUsersAsyncUsersAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users/async`,
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
   * Delete multiple Users asynchronously
   * Delete Users Async
   */
  async deleteUsersAsyncUsersAsyncDelete(
    requestParameters: DeleteUsersAsyncUsersAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteUsersAsyncUsersAsyncDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Users
   * Delete Users
   */
  async deleteUsersUsersDeleteRaw(
    requestParameters: DeleteUsersUsersDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<User>>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteUsersUsersDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["requestBody"],
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(UserFromJSON),
    );
  }

  /**
   * Delete multiple Users
   * Delete Users
   */
  async deleteUsersUsersDelete(
    requestParameters: DeleteUsersUsersDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.deleteUsersUsersDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get a User
   * Get User
   */
  async getUserUserGetRaw(
    requestParameters: GetUserUserGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<User>> {
    if (requestParameters["userId"] == null) {
      throw new runtime.RequiredError(
        "userId",
        'Required parameter "userId" was null or undefined when calling getUserUserGet().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["userId"] != null) {
      queryParameters["user_id"] = requestParameters["userId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/user`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      UserFromJSON(jsonValue),
    );
  }

  /**
   * Get a User
   * Get User
   */
  async getUserUserGet(
    requestParameters: GetUserUserGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<User> {
    const response = await this.getUserUserGetRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get all Users
   * Get Users
   */
  async getUsersUsersGetRaw(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<User>>> {
    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/users`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(UserFromJSON),
    );
  }

  /**
   * Get all Users
   * Get Users
   */
  async getUsersUsersGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.getUsersUsersGetRaw(initOverrides);
    return await response.value();
  }

  /**
   * Query Users
   * Query User
   */
  async queryUserUserQueryPostRaw(
    requestParameters: QueryUserUserQueryPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<User>>> {
    if (requestParameters["userQuery"] == null) {
      throw new runtime.RequiredError(
        "userQuery",
        'Required parameter "userQuery" was null or undefined when calling queryUserUserQueryPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/user/query`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: UserQueryToJSON(requestParameters["userQuery"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(UserFromJSON),
    );
  }

  /**
   * Query Users
   * Query User
   */
  async queryUserUserQueryPost(
    requestParameters: QueryUserUserQueryPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.queryUserUserQueryPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update a User asynchronously
   * Update User Async
   */
  async updateUserAsyncUserAsyncPutRaw(
    requestParameters: UpdateUserAsyncUserAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling updateUserAsyncUserAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/user/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: UserToJSON(requestParameters["user"]),
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
   * Update a User asynchronously
   * Update User Async
   */
  async updateUserAsyncUserAsyncPut(
    requestParameters: UpdateUserAsyncUserAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateUserAsyncUserAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update a User
   * Update User
   */
  async updateUserUserPutRaw(
    requestParameters: UpdateUserUserPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<User>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling updateUserUserPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/user`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: UserToJSON(requestParameters["user"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      UserFromJSON(jsonValue),
    );
  }

  /**
   * Update a User
   * Update User
   */
  async updateUserUserPut(
    requestParameters: UpdateUserUserPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<User> {
    const response = await this.updateUserUserPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Users asynchronously
   * Update Users Async
   */
  async updateUsersAsyncUsersAsyncPutRaw(
    requestParameters: UpdateUsersAsyncUsersAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling updateUsersAsyncUsersAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["user"]!.map(UserToJSON),
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
   * Update multiple Users asynchronously
   * Update Users Async
   */
  async updateUsersAsyncUsersAsyncPut(
    requestParameters: UpdateUsersAsyncUsersAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateUsersAsyncUsersAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Users
   * Update Users
   */
  async updateUsersUsersPutRaw(
    requestParameters: UpdateUsersUsersPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<User>>> {
    if (requestParameters["user"] == null) {
      throw new runtime.RequiredError(
        "user",
        'Required parameter "user" was null or undefined when calling updateUsersUsersPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/users`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["user"]!.map(UserToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(UserFromJSON),
    );
  }

  /**
   * Update multiple Users
   * Update Users
   */
  async updateUsersUsersPut(
    requestParameters: UpdateUsersUsersPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.updateUsersUsersPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }
}
