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

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface User
 */
export interface User {
    /**
     * The unique identifier of the user
     * @type {any}
     * @memberof User
     */
    id?: any | null;
    /**
     * The username of the user
     * @type {any}
     * @memberof User
     */
    username: any | null;
    /**
     * The email of the user
     * @type {any}
     * @memberof User
     */
    email: any | null;
    /**
     * The location of the user
     * @type {any}
     * @memberof User
     */
    location: any | null;
    /**
     * The age of the user
     * @type {any}
     * @memberof User
     */
    age: any | null;
    /**
     * The team name of the user
     * @type {any}
     * @memberof User
     */
    team: any | null;
}

/**
 * Check if a given object implements the User interface.
 */
export function instanceOfUser(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "username" in value;
    isInstance = isInstance && "email" in value;
    isInstance = isInstance && "location" in value;
    isInstance = isInstance && "age" in value;
    isInstance = isInstance && "team" in value;

    return isInstance;
}

export function UserFromJSON(json: any): User {
    return UserFromJSONTyped(json, false);
}

export function UserFromJSONTyped(json: any, ignoreDiscriminator: boolean): User {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'username': json['username'],
        'email': json['email'],
        'location': json['location'],
        'age': json['age'],
        'team': json['team'],
    };
}

export function UserToJSON(value?: User | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'username': value.username,
        'email': value.email,
        'location': value.location,
        'age': value.age,
        'team': value.team,
    };
}

