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
/**
 *
 * @export
 * @interface RestaurantId
 */
export interface RestaurantId {}

/**
 * Check if a given object implements the RestaurantId interface.
 */
export function instanceOfRestaurantId(value: object): boolean {
  return true;
}

export function RestaurantIdFromJSON(json: any): RestaurantId {
  return RestaurantIdFromJSONTyped(json, false);
}

export function RestaurantIdFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): RestaurantId {
  return json;
}

export function RestaurantIdToJSON(value?: RestaurantId | null): any {
  return value;
}
