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
 * The price range of the alembic
 * @export
 * @interface PriceRange
 */
export interface PriceRange {
}

/**
 * Check if a given object implements the PriceRange interface.
 */
export function instanceOfPriceRange(value: object): boolean {
    return true;
}

export function PriceRangeFromJSON(json: any): PriceRange {
    return PriceRangeFromJSONTyped(json, false);
}

export function PriceRangeFromJSONTyped(json: any, ignoreDiscriminator: boolean): PriceRange {
    return json;
}

export function PriceRangeToJSON(value?: PriceRange | null): any {
    return value;
}