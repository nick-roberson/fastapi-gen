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

import { mapValues } from "../runtime";
import type { Id } from "./Id";
import { IdFromJSON, IdFromJSONTyped, IdToJSON } from "./Id";
import type { SpecialRequests } from "./SpecialRequests";
import {
  SpecialRequestsFromJSON,
  SpecialRequestsFromJSONTyped,
  SpecialRequestsToJSON,
} from "./SpecialRequests";

/**
 *
 * @export
 * @interface Reservation
 */
export interface Reservation {
  /**
   *
   * @type {Id}
   * @memberof Reservation
   */
  id?: Id;
  /**
   * The ID of the alembic where the reservation is made
   * @type {number}
   * @memberof Reservation
   */
  restaurantId: number;
  /**
   * The ID of the user who made the reservation
   * @type {number}
   * @memberof Reservation
   */
  userId: number;
  /**
   * The date and time of the reservation
   * @type {Date}
   * @memberof Reservation
   */
  reservationTime: Date;
  /**
   * The size of the party for the reservation
   * @type {number}
   * @memberof Reservation
   */
  partySize: number;
  /**
   *
   * @type {SpecialRequests}
   * @memberof Reservation
   */
  specialRequests?: SpecialRequests;
}

/**
 * Check if a given object implements the Reservation interface.
 */
export function instanceOfReservation(value: object): boolean {
  if (!("restaurantId" in value)) return false;
  if (!("userId" in value)) return false;
  if (!("reservationTime" in value)) return false;
  if (!("partySize" in value)) return false;
  return true;
}

export function ReservationFromJSON(json: any): Reservation {
  return ReservationFromJSONTyped(json, false);
}

export function ReservationFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): Reservation {
  if (json == null) {
    return json;
  }
  return {
    id: json["id"] == null ? undefined : IdFromJSON(json["id"]),
    restaurantId: json["restaurant_id"],
    userId: json["user_id"],
    reservationTime: new Date(json["reservation_time"]),
    partySize: json["party_size"],
    specialRequests:
      json["special_requests"] == null
        ? undefined
        : SpecialRequestsFromJSON(json["special_requests"]),
  };
}

export function ReservationToJSON(value?: Reservation | null): any {
  if (value == null) {
    return value;
  }
  return {
    id: IdToJSON(value["id"]),
    restaurant_id: value["restaurantId"],
    user_id: value["userId"],
    reservation_time: value["reservationTime"].toISOString(),
    party_size: value["partySize"],
    special_requests: SpecialRequestsToJSON(value["specialRequests"]),
  };
}