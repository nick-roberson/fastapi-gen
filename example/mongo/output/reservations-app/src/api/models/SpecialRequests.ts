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

import { mapValues } from '../runtime';
/**
 * Any special requests made by the user
 * @export
 * @interface SpecialRequests
 */
export interface SpecialRequests {
}

/**
 * Check if a given object implements the SpecialRequests interface.
 */
export function instanceOfSpecialRequests(value: object): boolean {
    return true;
}

export function SpecialRequestsFromJSON(json: any): SpecialRequests {
    return SpecialRequestsFromJSONTyped(json, false);
}

export function SpecialRequestsFromJSONTyped(json: any, ignoreDiscriminator: boolean): SpecialRequests {
    return json;
}

export function SpecialRequestsToJSON(value?: SpecialRequests | null): any {
    return value;
}
