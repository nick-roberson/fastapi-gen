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
 * @interface PriceRange1
 */
export interface PriceRange1 {
}

/**
 * Check if a given object implements the PriceRange1 interface.
 */
export function instanceOfPriceRange1(value: object): boolean {
    return true;
}

export function PriceRange1FromJSON(json: any): PriceRange1 {
    return PriceRange1FromJSONTyped(json, false);
}

export function PriceRange1FromJSONTyped(json: any, ignoreDiscriminator: boolean): PriceRange1 {
    return json;
}

export function PriceRange1ToJSON(value?: PriceRange1 | null): any {
    return value;
}

