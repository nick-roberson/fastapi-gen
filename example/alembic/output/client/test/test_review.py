# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.review import Review


class TestReview(unittest.TestCase):
    """Review unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Review:
        """Test Review
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Review`
        """
        model = Review()
        if include_optional:
            return Review(
                id = None,
                restaurant_id = 56,
                user_id = 56,
                rating = 1.337,
                comment = None
            )
        else:
            return Review(
                restaurant_id = 56,
                user_id = 56,
                rating = 1.337,
        )
        """

    def testReview(self):
        """Test Review"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
