"""Custom render for user data"""
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class UserRenderer(JSONRenderer):
    """Class to define the custom renderer for user data"""
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None)->Response:
        """
        Render the data of user instance in a json format. Overides defalt render method

        Args:
            data (dict): user data
            accepted_media_type (_type_, optional): _description_. Defaults to None.
            renderer_context (_type_, optional): _description_. Defaults to None.

        Returns:
            Response: data with errors or jsonlike user data
        """
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return response
