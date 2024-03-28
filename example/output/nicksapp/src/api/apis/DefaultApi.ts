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
import type { Group, HTTPValidationError, User } from "../models/index";
import {
  GroupFromJSON,
  GroupToJSON,
  HTTPValidationErrorFromJSON,
  HTTPValidationErrorToJSON,
  UserFromJSON,
  UserToJSON,
} from "../models/index";

export interface CreateGroupGroupPostRequest {
  group: Group;
}

export interface CreateGroupsGroupsPostRequest {
  group: Array<Group>;
}

export interface CreateUserUserPostRequest {
  user: User;
}

export interface CreateUsersUsersPostRequest {
  user: Array<User>;
}

export interface DeleteGroupGroupDeleteRequest {
  groupId: string;
}

export interface DeleteGroupsGroupsDeleteRequest {
  requestBody: Array<string>;
}

export interface DeleteUserUserDeleteRequest {
  userId: string;
}

export interface DeleteUsersUsersDeleteRequest {
  requestBody: Array<string>;
}

export interface GetGroupGroupGetRequest {
  groupId: string;
}

export interface GetUserUserGetRequest {
  userId: string;
}

export interface UpdateGroupGroupPutRequest {
  group: Group;
}

export interface UpdateGroupsGroupsPutRequest {
  group: Array<Group>;
}

export interface UpdateUserUserPutRequest {
  user: User;
}

export interface UpdateUsersUsersPutRequest {
  user: Array<User>;
}

/**
 *
 */
export class DefaultApi extends runtime.BaseAPI {
  /**
   * Create a Group
   * Create Group
   */
  async createGroupGroupPostRaw(
    requestParameters: CreateGroupGroupPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Group>> {
    if (requestParameters["group"] == null) {
      throw new runtime.RequiredError(
        "group",
        'Required parameter "group" was null or undefined when calling createGroupGroupPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/group`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: GroupToJSON(requestParameters["group"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      GroupFromJSON(jsonValue),
    );
  }

  /**
   * Create a Group
   * Create Group
   */
  async createGroupGroupPost(
    requestParameters: CreateGroupGroupPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Group> {
    const response = await this.createGroupGroupPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Groups
   * Create Groups
   */
  async createGroupsGroupsPostRaw(
    requestParameters: CreateGroupsGroupsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Group>>> {
    if (requestParameters["group"] == null) {
      throw new runtime.RequiredError(
        "group",
        'Required parameter "group" was null or undefined when calling createGroupsGroupsPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/groups`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["group"]!.map(GroupToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(GroupFromJSON),
    );
  }

  /**
   * Create multiple Groups
   * Create Groups
   */
  async createGroupsGroupsPost(
    requestParameters: CreateGroupsGroupsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Group>> {
    const response = await this.createGroupsGroupsPostRaw(
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
   * Delete a Group
   * Delete Group
   */
  async deleteGroupGroupDeleteRaw(
    requestParameters: DeleteGroupGroupDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["groupId"] == null) {
      throw new runtime.RequiredError(
        "groupId",
        'Required parameter "groupId" was null or undefined when calling deleteGroupGroupDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["groupId"] != null) {
      queryParameters["group_id"] = requestParameters["groupId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/group`,
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
   * Delete a Group
   * Delete Group
   */
  async deleteGroupGroupDelete(
    requestParameters: DeleteGroupGroupDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteGroupGroupDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Groups
   * Delete Groups
   */
  async deleteGroupsGroupsDeleteRaw(
    requestParameters: DeleteGroupsGroupsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteGroupsGroupsDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/groups`,
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
   * Delete multiple Groups
   * Delete Groups
   */
  async deleteGroupsGroupsDelete(
    requestParameters: DeleteGroupsGroupsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteGroupsGroupsDeleteRaw(
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
  ): Promise<runtime.ApiResponse<any>> {
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

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Delete a User
   * Delete User
   */
  async deleteUserUserDelete(
    requestParameters: DeleteUserUserDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteUserUserDeleteRaw(
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
  ): Promise<runtime.ApiResponse<any>> {
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

    if (this.isJsonMime(response.headers.get("content-type"))) {
      return new runtime.JSONApiResponse<any>(response);
    } else {
      return new runtime.TextApiResponse(response) as any;
    }
  }

  /**
   * Delete multiple Users
   * Delete Users
   */
  async deleteUsersUsersDelete(
    requestParameters: DeleteUsersUsersDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteUsersUsersDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get a Group
   * Get Group
   */
  async getGroupGroupGetRaw(
    requestParameters: GetGroupGroupGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Group>> {
    if (requestParameters["groupId"] == null) {
      throw new runtime.RequiredError(
        "groupId",
        'Required parameter "groupId" was null or undefined when calling getGroupGroupGet().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["groupId"] != null) {
      queryParameters["group_id"] = requestParameters["groupId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/group`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      GroupFromJSON(jsonValue),
    );
  }

  /**
   * Get a Group
   * Get Group
   */
  async getGroupGroupGet(
    requestParameters: GetGroupGroupGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Group> {
    const response = await this.getGroupGroupGetRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get Groups
   */
  async getGroupsGroupsGetRaw(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Group>>> {
    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/groups`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(GroupFromJSON),
    );
  }

  /**
   * Get Groups
   */
  async getGroupsGroupsGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Group>> {
    const response = await this.getGroupsGroupsGetRaw(initOverrides);
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
   * Get Users
   */
  async getUsersUsersGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<User>> {
    const response = await this.getUsersUsersGetRaw(initOverrides);
    return await response.value();
  }

  /**
   * Root
   */
  async rootGetRaw(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/`,
        method: "GET",
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
   * Root
   */
  async rootGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.rootGetRaw(initOverrides);
    return await response.value();
  }

  /**
   * Update a Group
   * Update Group
   */
  async updateGroupGroupPutRaw(
    requestParameters: UpdateGroupGroupPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Group>> {
    if (requestParameters["group"] == null) {
      throw new runtime.RequiredError(
        "group",
        'Required parameter "group" was null or undefined when calling updateGroupGroupPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/group`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: GroupToJSON(requestParameters["group"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      GroupFromJSON(jsonValue),
    );
  }

  /**
   * Update a Group
   * Update Group
   */
  async updateGroupGroupPut(
    requestParameters: UpdateGroupGroupPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Group> {
    const response = await this.updateGroupGroupPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Groups
   * Update Groups
   */
  async updateGroupsGroupsPutRaw(
    requestParameters: UpdateGroupsGroupsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Group>>> {
    if (requestParameters["group"] == null) {
      throw new runtime.RequiredError(
        "group",
        'Required parameter "group" was null or undefined when calling updateGroupsGroupsPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/groups`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["group"]!.map(GroupToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(GroupFromJSON),
    );
  }

  /**
   * Update multiple Groups
   * Update Groups
   */
  async updateGroupsGroupsPut(
    requestParameters: UpdateGroupsGroupsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Group>> {
    const response = await this.updateGroupsGroupsPutRaw(
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
