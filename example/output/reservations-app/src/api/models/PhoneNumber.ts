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
 * The phone number of the user
 * @export
 * @interface PhoneNumber
 */
export interface PhoneNumber {}

/**
 * Check if a given object implements the PhoneNumber interface.
 */
export function instanceOfPhoneNumber(value: object): boolean {
  return true;
}

export function PhoneNumberFromJSON(json: any): PhoneNumber {
  return PhoneNumberFromJSONTyped(json, false);
}

export function PhoneNumberFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): PhoneNumber {
  return json;
}

export function PhoneNumberToJSON(value?: PhoneNumber | null): any {
  return value;
}
