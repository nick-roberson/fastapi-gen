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
 * The dining preferences of the user
 * @export
 * @interface Preferences
 */
export interface Preferences {
}

/**
 * Check if a given object implements the Preferences interface.
 */
export function instanceOfPreferences(value: object): boolean {
    return true;
}

export function PreferencesFromJSON(json: any): Preferences {
    return PreferencesFromJSONTyped(json, false);
}

export function PreferencesFromJSONTyped(json: any, ignoreDiscriminator: boolean): Preferences {
    return json;
}

export function PreferencesToJSON(value?: Preferences | null): any {
    return value;
}