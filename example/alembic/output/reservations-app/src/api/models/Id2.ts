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
 * The unique identifier of the review
 * @export
 * @interface Id2
 */
export interface Id2 {
}

/**
 * Check if a given object implements the Id2 interface.
 */
export function instanceOfId2(value: object): boolean {
    return true;
}

export function Id2FromJSON(json: any): Id2 {
    return Id2FromJSONTyped(json, false);
}

export function Id2FromJSONTyped(json: any, ignoreDiscriminator: boolean): Id2 {
    return json;
}

export function Id2ToJSON(value?: Id2 | null): any {
    return value;
}
