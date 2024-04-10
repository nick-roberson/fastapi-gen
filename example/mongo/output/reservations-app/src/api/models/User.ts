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
import type { Id3 } from './Id3';
import {
    Id3FromJSON,
    Id3FromJSONTyped,
    Id3ToJSON,
} from './Id3';
import type { PhoneNumber } from './PhoneNumber';
import {
    PhoneNumberFromJSON,
    PhoneNumberFromJSONTyped,
    PhoneNumberToJSON,
} from './PhoneNumber';
import type { Preferences } from './Preferences';
import {
    PreferencesFromJSON,
    PreferencesFromJSONTyped,
    PreferencesToJSON,
} from './Preferences';
import type { Role } from './Role';
import {
    RoleFromJSON,
    RoleFromJSONTyped,
    RoleToJSON,
} from './Role';

/**
 *
 * @export
 * @interface User
 */
export interface User {
    /**
     *
     * @type {Id3}
     * @memberof User
     */
    id?: Id3;
    /**
     * The username of the user
     * @type {string}
     * @memberof User
     */
    username: string;
    /**
     * The email address of the user
     * @type {string}
     * @memberof User
     */
    email: string;
    /**
     *
     * @type {PhoneNumber}
     * @memberof User
     */
    phoneNumber?: PhoneNumber;
    /**
     *
     * @type {Preferences}
     * @memberof User
     */
    preferences?: Preferences;
    /**
     *
     * @type {Role}
     * @memberof User
     */
    role?: Role;
}

/**
 * Check if a given object implements the User interface.
 */
export function instanceOfUser(value: object): boolean {
    if (!('username' in value)) return false;
    if (!('email' in value)) return false;
    return true;
}

export function UserFromJSON(json: any): User {
    return UserFromJSONTyped(json, false);
}

export function UserFromJSONTyped(json: any, ignoreDiscriminator: boolean): User {
    if (json == null) {
        return json;
    }
    return {

        'id': json['id'] == null ? undefined : Id3FromJSON(json['id']),
        'username': json['username'],
        'email': json['email'],
        'phoneNumber': json['phone_number'] == null ? undefined : PhoneNumberFromJSON(json['phone_number']),
        'preferences': json['preferences'] == null ? undefined : PreferencesFromJSON(json['preferences']),
        'role': json['role'] == null ? undefined : RoleFromJSON(json['role']),
    };
}

export function UserToJSON(value?: User | null): any {
    if (value == null) {
        return value;
    }
    return {

        'id': Id3ToJSON(value['id']),
        'username': value['username'],
        'email': value['email'],
        'phone_number': PhoneNumberToJSON(value['phoneNumber']),
        'preferences': PreferencesToJSON(value['preferences']),
        'role': RoleToJSON(value['role']),
    };
}