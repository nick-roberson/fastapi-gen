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
 * The average rating of the alembic
 * @export
 * @interface Rating
 */
export interface Rating {
}

/**
 * Check if a given object implements the Rating interface.
 */
export function instanceOfRating(value: object): boolean {
    return true;
}

export function RatingFromJSON(json: any): Rating {
    return RatingFromJSONTyped(json, false);
}

export function RatingFromJSONTyped(json: any, ignoreDiscriminator: boolean): Rating {
    return json;
}

export function RatingToJSON(value?: Rating | null): any {
    return value;
}