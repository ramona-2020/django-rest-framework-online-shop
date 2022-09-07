"""Generated client library for cloudasset version v1p1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1p1beta1 import cloudasset_v1p1beta1_messages as messages


class CloudassetV1p1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1p1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudasset.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudasset.mtls.googleapis.com/'

  _PACKAGE = 'cloudasset'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1p1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudassetV1p1beta1'
  _URL_VERSION = 'v1p1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1p1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.iamPolicies = self.IamPoliciesService(self)
    self.resources = self.ResourcesService(self)

  class IamPoliciesService(base_api.BaseApiService):
    """Service class for the iamPolicies resource."""

    _NAME = 'iamPolicies'

    def __init__(self, client):
      super(CloudassetV1p1beta1.IamPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def SearchAll(self, request, global_params=None):
      r"""Searches all the IAM policies within a given accessible CRM scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the IAM policies within a scope, even if they don't have `.getIamPolicy` permission of all the IAM policies. Callers should have `cloud.assets.SearchAllIamPolicies` permission on the requested scope, otherwise the request will be rejected.

      Args:
        request: (CloudassetIamPoliciesSearchAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchAllIamPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('SearchAll')
      return self._RunMethod(
          config, request, global_params=global_params)

    SearchAll.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/{v1p1beta1Id}/{v1p1beta1Id1}/iamPolicies:searchAll',
        http_method='GET',
        method_id='cloudasset.iamPolicies.searchAll',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['pageSize', 'pageToken', 'query'],
        relative_path='v1p1beta1/{+scope}/iamPolicies:searchAll',
        request_field='',
        request_type_name='CloudassetIamPoliciesSearchAllRequest',
        response_type_name='SearchAllIamPoliciesResponse',
        supports_download=False,
    )

  class ResourcesService(base_api.BaseApiService):
    """Service class for the resources resource."""

    _NAME = 'resources'

    def __init__(self, client):
      super(CloudassetV1p1beta1.ResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def SearchAll(self, request, global_params=None):
      r"""Searches all the resources within a given accessible CRM scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the resources within a scope, even if they don't have `.get` permission of all the resources. Callers should have `cloud.assets.SearchAllResources` permission on the requested scope, otherwise the request will be rejected.

      Args:
        request: (CloudassetResourcesSearchAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchAllResourcesResponse) The response message.
      """
      config = self.GetMethodConfig('SearchAll')
      return self._RunMethod(
          config, request, global_params=global_params)

    SearchAll.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/{v1p1beta1Id}/{v1p1beta1Id1}/resources:searchAll',
        http_method='GET',
        method_id='cloudasset.resources.searchAll',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['assetTypes', 'orderBy', 'pageSize', 'pageToken', 'query'],
        relative_path='v1p1beta1/{+scope}/resources:searchAll',
        request_field='',
        request_type_name='CloudassetResourcesSearchAllRequest',
        response_type_name='SearchAllResourcesResponse',
        supports_download=False,
    )
