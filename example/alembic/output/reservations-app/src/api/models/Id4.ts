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
 * The unique identifier of the user
 * @export
 * @interface Id4
 */
export interface Id4 {
}

/**
 * Check if a given object implements the Id4 interface.
 */
export function instanceOfId4(value: object): boolean {
    return true;
}

export function Id4FromJSON(json: any): Id4 {
    return Id4FromJSONTyped(json, false);
}

export function Id4FromJSONTyped(json: any, ignoreDiscriminator: boolean): Id4 {
    return json;
}

export function Id4ToJSON(value?: Id4 | null): any {
    return value;
}

