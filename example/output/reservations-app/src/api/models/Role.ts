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
 * The role of the user (e.g., admin, user, restaurant_owner)
 * @export
 * @interface Role
 */
export interface Role {}

/**
 * Check if a given object implements the Role interface.
 */
export function instanceOfRole(value: object): boolean {
  return true;
}

export function RoleFromJSON(json: any): Role {
  return RoleFromJSONTyped(json, false);
}

export function RoleFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): Role {
  return json;
}

export function RoleToJSON(value?: Role | null): any {
  return value;
}