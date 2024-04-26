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
 * @interface RestaurantQuery
 */
export interface RestaurantQuery {
  /**
   *
   * @type {number}
   * @memberof RestaurantQuery
   */
  id?: number;
  /**
   *
   * @type {string}
   * @memberof RestaurantQuery
   */
  name?: string;
  /**
   *
   * @type {string}
   * @memberof RestaurantQuery
   */
  location?: string;
  /**
   *
   * @type {string}
   * @memberof RestaurantQuery
   */
  cuisine?: string;
  /**
   *
   * @type {number}
   * @memberof RestaurantQuery
   */
  rating?: number;
  /**
   *
   * @type {string}
   * @memberof RestaurantQuery
   */
  priceRange?: string;
}

/**
 * Check if a given object implements the RestaurantQuery interface.
 */
export function instanceOfRestaurantQuery(value: object): boolean {
  return true;
}

export function RestaurantQueryFromJSON(json: any): RestaurantQuery {
  return RestaurantQueryFromJSONTyped(json, false);
}

export function RestaurantQueryFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): RestaurantQuery {
  if (json == null) {
    return json;
  }
  return {
    id: json["id"] == null ? undefined : json["id"],
    name: json["name"] == null ? undefined : json["name"],
    location: json["location"] == null ? undefined : json["location"],
    cuisine: json["cuisine"] == null ? undefined : json["cuisine"],
    rating: json["rating"] == null ? undefined : json["rating"],
    priceRange: json["price_range"] == null ? undefined : json["price_range"],
  };
}

export function RestaurantQueryToJSON(value?: RestaurantQuery | null): any {
  if (value == null) {
    return value;
  }
  return {
    id: value["id"],
    name: value["name"],
    location: value["location"],
    cuisine: value["cuisine"],
    rating: value["rating"],
    price_range: value["priceRange"],
  };
}
