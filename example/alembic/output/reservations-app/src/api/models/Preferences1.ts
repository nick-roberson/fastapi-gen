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
 * @interface Preferences1
 */
export interface Preferences1 {}

/**
 * Check if a given object implements the Preferences1 interface.
 */
export function instanceOfPreferences1(value: object): boolean {
  return true;
}

export function Preferences1FromJSON(json: any): Preferences1 {
  return Preferences1FromJSONTyped(json, false);
}

export function Preferences1FromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): Preferences1 {
  return json;
}

export function Preferences1ToJSON(value?: Preferences1 | null): any {
  return value;
}