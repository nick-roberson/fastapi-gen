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
 * 
 * @export
 * @interface Comment1
 */
export interface Comment1 {
}

/**
 * Check if a given object implements the Comment1 interface.
 */
export function instanceOfComment1(value: object): boolean {
    return true;
}

export function Comment1FromJSON(json: any): Comment1 {
    return Comment1FromJSONTyped(json, false);
}

export function Comment1FromJSONTyped(json: any, ignoreDiscriminator: boolean): Comment1 {
    return json;
}

export function Comment1ToJSON(value?: Comment1 | null): any {
    return value;
}

