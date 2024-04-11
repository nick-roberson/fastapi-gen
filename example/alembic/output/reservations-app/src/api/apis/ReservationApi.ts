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
import type { HTTPValidationError, Reservation } from "../models/index";
import {
  HTTPValidationErrorFromJSON,
  HTTPValidationErrorToJSON,
  ReservationFromJSON,
  ReservationToJSON,
} from "../models/index";

export interface CreateReservationAsyncReservationAsyncPostRequest {
  reservation: Reservation;
}

export interface CreateReservationReservationPostRequest {
  reservation: Reservation;
}

export interface CreateReservationsAsyncReservationsAsyncPostRequest {
  reservation: Array<Reservation>;
}

export interface CreateReservationsReservationsPostRequest {
  reservation: Array<Reservation>;
}

export interface DeleteReservationAsyncReservationAsyncDeleteRequest {
  reservationId: string;
}

export interface DeleteReservationReservationDeleteRequest {
  reservationId: string;
}

export interface DeleteReservationsAsyncReservationsAsyncDeleteRequest {
  requestBody: Array<string>;
}

export interface DeleteReservationsReservationsDeleteRequest {
  requestBody: Array<string>;
}

export interface GetReservationReservationGetRequest {
  reservationId: string;
}

export interface UpdateReservationAsyncReservationAsyncPutRequest {
  reservation: Reservation;
}

export interface UpdateReservationReservationPutRequest {
  reservation: Reservation;
}

export interface UpdateReservationsAsyncReservationsAsyncPutRequest {
  reservation: Array<Reservation>;
}

export interface UpdateReservationsReservationsPutRequest {
  reservation: Array<Reservation>;
}

/**
 *
 */
export class ReservationApi extends runtime.BaseAPI {
  /**
   * Create a Reservation asynchronously
   * Create Reservation Async
   */
  async createReservationAsyncReservationAsyncPostRaw(
    requestParameters: CreateReservationAsyncReservationAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling createReservationAsyncReservationAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservation/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: ReservationToJSON(requestParameters["reservation"]),
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
   * Create a Reservation asynchronously
   * Create Reservation Async
   */
  async createReservationAsyncReservationAsyncPost(
    requestParameters: CreateReservationAsyncReservationAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createReservationAsyncReservationAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create a Reservation
   * Create Reservation
   */
  async createReservationReservationPostRaw(
    requestParameters: CreateReservationReservationPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Reservation>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling createReservationReservationPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservation`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: ReservationToJSON(requestParameters["reservation"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      ReservationFromJSON(jsonValue),
    );
  }

  /**
   * Create a Reservation
   * Create Reservation
   */
  async createReservationReservationPost(
    requestParameters: CreateReservationReservationPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Reservation> {
    const response = await this.createReservationReservationPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Reservations asynchronously
   * Create Reservations Async
   */
  async createReservationsAsyncReservationsAsyncPostRaw(
    requestParameters: CreateReservationsAsyncReservationsAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling createReservationsAsyncReservationsAsyncPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations/async`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["reservation"]!.map(ReservationToJSON),
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
   * Create multiple Reservations asynchronously
   * Create Reservations Async
   */
  async createReservationsAsyncReservationsAsyncPost(
    requestParameters: CreateReservationsAsyncReservationsAsyncPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.createReservationsAsyncReservationsAsyncPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Create multiple Reservations
   * Create Reservations
   */
  async createReservationsReservationsPostRaw(
    requestParameters: CreateReservationsReservationsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Reservation>>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling createReservationsReservationsPost().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations`,
        method: "POST",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["reservation"]!.map(ReservationToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(ReservationFromJSON),
    );
  }

  /**
   * Create multiple Reservations
   * Create Reservations
   */
  async createReservationsReservationsPost(
    requestParameters: CreateReservationsReservationsPostRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Reservation>> {
    const response = await this.createReservationsReservationsPostRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a Reservation asynchronously
   * Delete Reservation Async
   */
  async deleteReservationAsyncReservationAsyncDeleteRaw(
    requestParameters: DeleteReservationAsyncReservationAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["reservationId"] == null) {
      throw new runtime.RequiredError(
        "reservationId",
        'Required parameter "reservationId" was null or undefined when calling deleteReservationAsyncReservationAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["reservationId"] != null) {
      queryParameters["reservation_id"] = requestParameters["reservationId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/reservation/async`,
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
   * Delete a Reservation asynchronously
   * Delete Reservation Async
   */
  async deleteReservationAsyncReservationAsyncDelete(
    requestParameters: DeleteReservationAsyncReservationAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.deleteReservationAsyncReservationAsyncDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete a Reservation
   * Delete Reservation
   */
  async deleteReservationReservationDeleteRaw(
    requestParameters: DeleteReservationReservationDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Reservation>> {
    if (requestParameters["reservationId"] == null) {
      throw new runtime.RequiredError(
        "reservationId",
        'Required parameter "reservationId" was null or undefined when calling deleteReservationReservationDelete().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["reservationId"] != null) {
      queryParameters["reservation_id"] = requestParameters["reservationId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/reservation`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      ReservationFromJSON(jsonValue),
    );
  }

  /**
   * Delete a Reservation
   * Delete Reservation
   */
  async deleteReservationReservationDelete(
    requestParameters: DeleteReservationReservationDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Reservation> {
    const response = await this.deleteReservationReservationDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Delete multiple Reservations asynchronously
   * Delete Reservations Async
   */
  async deleteReservationsAsyncReservationsAsyncDeleteRaw(
    requestParameters: DeleteReservationsAsyncReservationsAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteReservationsAsyncReservationsAsyncDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations/async`,
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
   * Delete multiple Reservations asynchronously
   * Delete Reservations Async
   */
  async deleteReservationsAsyncReservationsAsyncDelete(
    requestParameters: DeleteReservationsAsyncReservationsAsyncDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response =
      await this.deleteReservationsAsyncReservationsAsyncDeleteRaw(
        requestParameters,
        initOverrides,
      );
    return await response.value();
  }

  /**
   * Delete multiple Reservations
   * Delete Reservations
   */
  async deleteReservationsReservationsDeleteRaw(
    requestParameters: DeleteReservationsReservationsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Reservation>>> {
    if (requestParameters["requestBody"] == null) {
      throw new runtime.RequiredError(
        "requestBody",
        'Required parameter "requestBody" was null or undefined when calling deleteReservationsReservationsDelete().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations`,
        method: "DELETE",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["requestBody"],
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(ReservationFromJSON),
    );
  }

  /**
   * Delete multiple Reservations
   * Delete Reservations
   */
  async deleteReservationsReservationsDelete(
    requestParameters: DeleteReservationsReservationsDeleteRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Reservation>> {
    const response = await this.deleteReservationsReservationsDeleteRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get a Reservation
   * Get Reservation
   */
  async getReservationReservationGetRaw(
    requestParameters: GetReservationReservationGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Reservation>> {
    if (requestParameters["reservationId"] == null) {
      throw new runtime.RequiredError(
        "reservationId",
        'Required parameter "reservationId" was null or undefined when calling getReservationReservationGet().',
      );
    }

    const queryParameters: any = {};

    if (requestParameters["reservationId"] != null) {
      queryParameters["reservation_id"] = requestParameters["reservationId"];
    }

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/reservation`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      ReservationFromJSON(jsonValue),
    );
  }

  /**
   * Get a Reservation
   * Get Reservation
   */
  async getReservationReservationGet(
    requestParameters: GetReservationReservationGetRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Reservation> {
    const response = await this.getReservationReservationGetRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Get all Reservations
   * Get Reservations
   */
  async getReservationsReservationsGetRaw(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Reservation>>> {
    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    const response = await this.request(
      {
        path: `/reservations`,
        method: "GET",
        headers: headerParameters,
        query: queryParameters,
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(ReservationFromJSON),
    );
  }

  /**
   * Get all Reservations
   * Get Reservations
   */
  async getReservationsReservationsGet(
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Reservation>> {
    const response =
      await this.getReservationsReservationsGetRaw(initOverrides);
    return await response.value();
  }

  /**
   * Update a Reservation asynchronously
   * Update Reservation Async
   */
  async updateReservationAsyncReservationAsyncPutRaw(
    requestParameters: UpdateReservationAsyncReservationAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling updateReservationAsyncReservationAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservation/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: ReservationToJSON(requestParameters["reservation"]),
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
   * Update a Reservation asynchronously
   * Update Reservation Async
   */
  async updateReservationAsyncReservationAsyncPut(
    requestParameters: UpdateReservationAsyncReservationAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateReservationAsyncReservationAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update a Reservation
   * Update Reservation
   */
  async updateReservationReservationPutRaw(
    requestParameters: UpdateReservationReservationPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Reservation>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling updateReservationReservationPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservation`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: ReservationToJSON(requestParameters["reservation"]),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      ReservationFromJSON(jsonValue),
    );
  }

  /**
   * Update a Reservation
   * Update Reservation
   */
  async updateReservationReservationPut(
    requestParameters: UpdateReservationReservationPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Reservation> {
    const response = await this.updateReservationReservationPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Reservations asynchronously
   * Update Reservations Async
   */
  async updateReservationsAsyncReservationsAsyncPutRaw(
    requestParameters: UpdateReservationsAsyncReservationsAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<any>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling updateReservationsAsyncReservationsAsyncPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations/async`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["reservation"]!.map(ReservationToJSON),
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
   * Update multiple Reservations asynchronously
   * Update Reservations Async
   */
  async updateReservationsAsyncReservationsAsyncPut(
    requestParameters: UpdateReservationsAsyncReservationsAsyncPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<any> {
    const response = await this.updateReservationsAsyncReservationsAsyncPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }

  /**
   * Update multiple Reservations
   * Update Reservations
   */
  async updateReservationsReservationsPutRaw(
    requestParameters: UpdateReservationsReservationsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<runtime.ApiResponse<Array<Reservation>>> {
    if (requestParameters["reservation"] == null) {
      throw new runtime.RequiredError(
        "reservation",
        'Required parameter "reservation" was null or undefined when calling updateReservationsReservationsPut().',
      );
    }

    const queryParameters: any = {};

    const headerParameters: runtime.HTTPHeaders = {};

    headerParameters["Content-Type"] = "application/json";

    const response = await this.request(
      {
        path: `/reservations`,
        method: "PUT",
        headers: headerParameters,
        query: queryParameters,
        body: requestParameters["reservation"]!.map(ReservationToJSON),
      },
      initOverrides,
    );

    return new runtime.JSONApiResponse(response, (jsonValue) =>
      jsonValue.map(ReservationFromJSON),
    );
  }

  /**
   * Update multiple Reservations
   * Update Reservations
   */
  async updateReservationsReservationsPut(
    requestParameters: UpdateReservationsReservationsPutRequest,
    initOverrides?: RequestInit | runtime.InitOverrideFunction,
  ): Promise<Array<Reservation>> {
    const response = await this.updateReservationsReservationsPutRaw(
      requestParameters,
      initOverrides,
    );
    return await response.value();
  }
}
