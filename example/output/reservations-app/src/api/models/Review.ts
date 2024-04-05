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

import { mapValues } from "../runtime";
import type { Comment } from "./Comment";
import {
  CommentFromJSON,
  CommentFromJSONTyped,
  CommentToJSON,
} from "./Comment";
import type { Id2 } from "./Id2";
import { Id2FromJSON, Id2FromJSONTyped, Id2ToJSON } from "./Id2";

/**
 *
 * @export
 * @interface Review
 */
export interface Review {
  /**
   *
   * @type {Id2}
   * @memberof Review
   */
  id?: Id2;
  /**
   * The ID of the restaurant being reviewed
   * @type {string}
   * @memberof Review
   */
  restaurantId: string;
  /**
   * The ID of the user who wrote the review
   * @type {string}
   * @memberof Review
   */
  userId: string;
  /**
   * The rating given by the user
   * @type {number}
   * @memberof Review
   */
  rating: number;
  /**
   *
   * @type {Comment}
   * @memberof Review
   */
  comment?: Comment;
}

/**
 * Check if a given object implements the Review interface.
 */
export function instanceOfReview(value: object): boolean {
  if (!("restaurantId" in value)) return false;
  if (!("userId" in value)) return false;
  if (!("rating" in value)) return false;
  return true;
}

export function ReviewFromJSON(json: any): Review {
  return ReviewFromJSONTyped(json, false);
}

export function ReviewFromJSONTyped(
  json: any,
  ignoreDiscriminator: boolean,
): Review {
  if (json == null) {
    return json;
  }
  return {
    id: json["id"] == null ? undefined : Id2FromJSON(json["id"]),
    restaurantId: json["restaurant_id"],
    userId: json["user_id"],
    rating: json["rating"],
    comment:
      json["comment"] == null ? undefined : CommentFromJSON(json["comment"]),
  };
}

export function ReviewToJSON(value?: Review | null): any {
  if (value == null) {
    return value;
  }
  return {
    id: Id2ToJSON(value["id"]),
    restaurant_id: value["restaurantId"],
    user_id: value["userId"],
    rating: value["rating"],
    comment: CommentToJSON(value["comment"]),
  };
}