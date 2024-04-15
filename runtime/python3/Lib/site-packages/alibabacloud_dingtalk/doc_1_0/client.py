# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.doc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        if UtilClient.empty(self._endpoint):
            self._endpoint = 'api.dingtalk.com'

    def add_workspace_doc_members(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AddWorkspaceDocMembersHeaders()
        return self.add_workspace_doc_members_with_options(workspace_id, node_id, request, headers, runtime)

    async def add_workspace_doc_members_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AddWorkspaceDocMembersHeaders()
        return await self.add_workspace_doc_members_with_options_async(workspace_id, node_id, request, headers, runtime)

    def add_workspace_doc_members_with_options(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.AddWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse(),
            self.do_roarequest('AddWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members', 'none', req, runtime)
        )

    async def add_workspace_doc_members_with_options_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.AddWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AddWorkspaceDocMembersResponse(),
            await self.do_roarequest_async('AddWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members', 'none', req, runtime)
        )

    def add_workspace_members(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AddWorkspaceMembersHeaders()
        return self.add_workspace_members_with_options(workspace_id, request, headers, runtime)

    async def add_workspace_members_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AddWorkspaceMembersHeaders()
        return await self.add_workspace_members_with_options_async(workspace_id, request, headers, runtime)

    def add_workspace_members_with_options(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.AddWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AddWorkspaceMembersResponse(),
            self.do_roarequest('AddWorkspaceMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members', 'json', req, runtime)
        )

    async def add_workspace_members_with_options_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.AddWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.AddWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AddWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AddWorkspaceMembersResponse(),
            await self.do_roarequest_async('AddWorkspaceMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members', 'json', req, runtime)
        )

    def append_rows(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.AppendRowsRequest,
    ) -> dingtalkdoc__1__0_models.AppendRowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AppendRowsHeaders()
        return self.append_rows_with_options(workbook_id, sheet_id, request, headers, runtime)

    async def append_rows_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.AppendRowsRequest,
    ) -> dingtalkdoc__1__0_models.AppendRowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.AppendRowsHeaders()
        return await self.append_rows_with_options_async(workbook_id, sheet_id, request, headers, runtime)

    def append_rows_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.AppendRowsRequest,
        headers: dingtalkdoc__1__0_models.AppendRowsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AppendRowsResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AppendRowsResponse(),
            self.do_roarequest('AppendRows', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/appendRows', 'none', req, runtime)
        )

    async def append_rows_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.AppendRowsRequest,
        headers: dingtalkdoc__1__0_models.AppendRowsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.AppendRowsResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.AppendRowsResponse(),
            await self.do_roarequest_async('AppendRows', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/appendRows', 'none', req, runtime)
        )

    def batch_get_workspace_docs(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsRequest,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.BatchGetWorkspaceDocsHeaders()
        return self.batch_get_workspace_docs_with_options(request, headers, runtime)

    async def batch_get_workspace_docs_async(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsRequest,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.BatchGetWorkspaceDocsHeaders()
        return await self.batch_get_workspace_docs_with_options_async(request, headers, runtime)

    def batch_get_workspace_docs_with_options(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsRequest,
        headers: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_ids):
            body['nodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse(),
            self.do_roarequest('BatchGetWorkspaceDocs', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/docs/infos/query', 'json', req, runtime)
        )

    async def batch_get_workspace_docs_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsRequest,
        headers: dingtalkdoc__1__0_models.BatchGetWorkspaceDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_ids):
            body['nodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.BatchGetWorkspaceDocsResponse(),
            await self.do_roarequest_async('BatchGetWorkspaceDocs', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/docs/infos/query', 'json', req, runtime)
        )

    def batch_get_workspaces(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspacesRequest,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.BatchGetWorkspacesHeaders()
        return self.batch_get_workspaces_with_options(request, headers, runtime)

    async def batch_get_workspaces_async(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspacesRequest,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.BatchGetWorkspacesHeaders()
        return await self.batch_get_workspaces_with_options_async(request, headers, runtime)

    def batch_get_workspaces_with_options(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspacesRequest,
        headers: dingtalkdoc__1__0_models.BatchGetWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.include_recent):
            body['includeRecent'] = request.include_recent
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.workspace_ids):
            body['workspaceIds'] = request.workspace_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.BatchGetWorkspacesResponse(),
            self.do_roarequest('BatchGetWorkspaces', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/infos/query', 'json', req, runtime)
        )

    async def batch_get_workspaces_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.BatchGetWorkspacesRequest,
        headers: dingtalkdoc__1__0_models.BatchGetWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.BatchGetWorkspacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.include_recent):
            body['includeRecent'] = request.include_recent
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.workspace_ids):
            body['workspaceIds'] = request.workspace_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.BatchGetWorkspacesResponse(),
            await self.do_roarequest_async('BatchGetWorkspaces', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/infos/query', 'json', req, runtime)
        )

    def create_sheet(
        self,
        workbook_id: str,
        request: dingtalkdoc__1__0_models.CreateSheetRequest,
    ) -> dingtalkdoc__1__0_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateSheetHeaders()
        return self.create_sheet_with_options(workbook_id, request, headers, runtime)

    async def create_sheet_async(
        self,
        workbook_id: str,
        request: dingtalkdoc__1__0_models.CreateSheetRequest,
    ) -> dingtalkdoc__1__0_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateSheetHeaders()
        return await self.create_sheet_with_options_async(workbook_id, request, headers, runtime)

    def create_sheet_with_options(
        self,
        workbook_id: str,
        request: dingtalkdoc__1__0_models.CreateSheetRequest,
        headers: dingtalkdoc__1__0_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateSheetResponse(),
            self.do_roarequest('CreateSheet', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets', 'json', req, runtime)
        )

    async def create_sheet_with_options_async(
        self,
        workbook_id: str,
        request: dingtalkdoc__1__0_models.CreateSheetRequest,
        headers: dingtalkdoc__1__0_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateSheetResponse(),
            await self.do_roarequest_async('CreateSheet', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets', 'json', req, runtime)
        )

    def create_workspace(
        self,
        request: dingtalkdoc__1__0_models.CreateWorkspaceRequest,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateWorkspaceHeaders()
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: dingtalkdoc__1__0_models.CreateWorkspaceRequest,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateWorkspaceHeaders()
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: dingtalkdoc__1__0_models.CreateWorkspaceRequest,
        headers: dingtalkdoc__1__0_models.CreateWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateWorkspaceResponse(),
            self.do_roarequest('CreateWorkspace', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces', 'json', req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.CreateWorkspaceRequest,
        headers: dingtalkdoc__1__0_models.CreateWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateWorkspaceResponse(),
            await self.do_roarequest_async('CreateWorkspace', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces', 'json', req, runtime)
        )

    def create_workspace_doc(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.CreateWorkspaceDocRequest,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders()
        return self.create_workspace_doc_with_options(workspace_id, request, headers, runtime)

    async def create_workspace_doc_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.CreateWorkspaceDocRequest,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders()
        return await self.create_workspace_doc_with_options_async(workspace_id, request, headers, runtime)

    def create_workspace_doc_with_options(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.CreateWorkspaceDocRequest,
        headers: dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceDocResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['docType'] = request.doc_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.parent_node_id):
            body['parentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateWorkspaceDocResponse(),
            self.do_roarequest('CreateWorkspaceDoc', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs', 'json', req, runtime)
        )

    async def create_workspace_doc_with_options_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.CreateWorkspaceDocRequest,
        headers: dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.CreateWorkspaceDocResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['docType'] = request.doc_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.parent_node_id):
            body['parentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.template_id):
            body['templateId'] = request.template_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.CreateWorkspaceDocResponse(),
            await self.do_roarequest_async('CreateWorkspaceDoc', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs', 'json', req, runtime)
        )

    def delete_sheet(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.DeleteSheetRequest,
    ) -> dingtalkdoc__1__0_models.DeleteSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteSheetHeaders()
        return self.delete_sheet_with_options(workbook_id, sheet_id, request, headers, runtime)

    async def delete_sheet_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.DeleteSheetRequest,
    ) -> dingtalkdoc__1__0_models.DeleteSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteSheetHeaders()
        return await self.delete_sheet_with_options_async(workbook_id, sheet_id, request, headers, runtime)

    def delete_sheet_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.DeleteSheetRequest,
        headers: dingtalkdoc__1__0_models.DeleteSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteSheetResponse(),
            self.do_roarequest('DeleteSheet', 'doc_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'none', req, runtime)
        )

    async def delete_sheet_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.DeleteSheetRequest,
        headers: dingtalkdoc__1__0_models.DeleteSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteSheetResponse(),
            await self.do_roarequest_async('DeleteSheet', 'doc_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'none', req, runtime)
        )

    def delete_workspace_doc(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders()
        return self.delete_workspace_doc_with_options(workspace_id, node_id, request, headers, runtime)

    async def delete_workspace_doc_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders()
        return await self.delete_workspace_doc_with_options_async(workspace_id, node_id, request, headers, runtime)

    def delete_workspace_doc_with_options(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse(),
            self.do_roarequest('DeleteWorkspaceDoc', 'doc_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}', 'none', req, runtime)
        )

    async def delete_workspace_doc_with_options_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceDocResponse(),
            await self.do_roarequest_async('DeleteWorkspaceDoc', 'doc_1.0', 'HTTP', 'DELETE', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}', 'none', req, runtime)
        )

    def delete_workspace_doc_members(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersHeaders()
        return self.delete_workspace_doc_members_with_options(workspace_id, node_id, request, headers, runtime)

    async def delete_workspace_doc_members_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersHeaders()
        return await self.delete_workspace_doc_members_with_options_async(workspace_id, node_id, request, headers, runtime)

    def delete_workspace_doc_members_with_options(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse(),
            self.do_roarequest('DeleteWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members/remove', 'none', req, runtime)
        )

    async def delete_workspace_doc_members_with_options_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceDocMembersResponse(),
            await self.do_roarequest_async('DeleteWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members/remove', 'none', req, runtime)
        )

    def delete_workspace_members(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders()
        return self.delete_workspace_members_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_members_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders()
        return await self.delete_workspace_members_with_options_async(workspace_id, request, headers, runtime)

    def delete_workspace_members_with_options(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse(),
            self.do_roarequest('DeleteWorkspaceMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members/remove', 'none', req, runtime)
        )

    async def delete_workspace_members_with_options_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.DeleteWorkspaceMembersResponse(),
            await self.do_roarequest_async('DeleteWorkspaceMembers', 'doc_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members/remove', 'none', req, runtime)
        )

    def get_range(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.GetRangeRequest,
    ) -> dingtalkdoc__1__0_models.GetRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRangeHeaders()
        return self.get_range_with_options(workbook_id, sheet_id, range_address, request, headers, runtime)

    async def get_range_async(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.GetRangeRequest,
    ) -> dingtalkdoc__1__0_models.GetRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRangeHeaders()
        return await self.get_range_with_options_async(workbook_id, sheet_id, range_address, request, headers, runtime)

    def get_range_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.GetRangeRequest,
        headers: dingtalkdoc__1__0_models.GetRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRangeResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        range_address = OpenApiUtilClient.get_encode_param(range_address)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRangeResponse(),
            self.do_roarequest('GetRange', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/ranges/{range_address}', 'json', req, runtime)
        )

    async def get_range_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.GetRangeRequest,
        headers: dingtalkdoc__1__0_models.GetRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRangeResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        range_address = OpenApiUtilClient.get_encode_param(range_address)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRangeResponse(),
            await self.do_roarequest_async('GetRange', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/ranges/{range_address}', 'json', req, runtime)
        )

    def get_recent_edit_docs(
        self,
        request: dingtalkdoc__1__0_models.GetRecentEditDocsRequest,
    ) -> dingtalkdoc__1__0_models.GetRecentEditDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRecentEditDocsHeaders()
        return self.get_recent_edit_docs_with_options(request, headers, runtime)

    async def get_recent_edit_docs_async(
        self,
        request: dingtalkdoc__1__0_models.GetRecentEditDocsRequest,
    ) -> dingtalkdoc__1__0_models.GetRecentEditDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRecentEditDocsHeaders()
        return await self.get_recent_edit_docs_with_options_async(request, headers, runtime)

    def get_recent_edit_docs_with_options(
        self,
        request: dingtalkdoc__1__0_models.GetRecentEditDocsRequest,
        headers: dingtalkdoc__1__0_models.GetRecentEditDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRecentEditDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRecentEditDocsResponse(),
            self.do_roarequest('GetRecentEditDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/docs/recentEditDocs', 'json', req, runtime)
        )

    async def get_recent_edit_docs_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.GetRecentEditDocsRequest,
        headers: dingtalkdoc__1__0_models.GetRecentEditDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRecentEditDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRecentEditDocsResponse(),
            await self.do_roarequest_async('GetRecentEditDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/docs/recentEditDocs', 'json', req, runtime)
        )

    def get_recent_open_docs(
        self,
        request: dingtalkdoc__1__0_models.GetRecentOpenDocsRequest,
    ) -> dingtalkdoc__1__0_models.GetRecentOpenDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRecentOpenDocsHeaders()
        return self.get_recent_open_docs_with_options(request, headers, runtime)

    async def get_recent_open_docs_async(
        self,
        request: dingtalkdoc__1__0_models.GetRecentOpenDocsRequest,
    ) -> dingtalkdoc__1__0_models.GetRecentOpenDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRecentOpenDocsHeaders()
        return await self.get_recent_open_docs_with_options_async(request, headers, runtime)

    def get_recent_open_docs_with_options(
        self,
        request: dingtalkdoc__1__0_models.GetRecentOpenDocsRequest,
        headers: dingtalkdoc__1__0_models.GetRecentOpenDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRecentOpenDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRecentOpenDocsResponse(),
            self.do_roarequest('GetRecentOpenDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/docs/recentOpenDocs', 'json', req, runtime)
        )

    async def get_recent_open_docs_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.GetRecentOpenDocsRequest,
        headers: dingtalkdoc__1__0_models.GetRecentOpenDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRecentOpenDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRecentOpenDocsResponse(),
            await self.do_roarequest_async('GetRecentOpenDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/docs/recentOpenDocs', 'json', req, runtime)
        )

    def get_related_workspaces(
        self,
        request: dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest,
    ) -> dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders()
        return self.get_related_workspaces_with_options(request, headers, runtime)

    async def get_related_workspaces_async(
        self,
        request: dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest,
    ) -> dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders()
        return await self.get_related_workspaces_with_options_async(request, headers, runtime)

    def get_related_workspaces_with_options(
        self,
        request: dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest,
        headers: dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_recent):
            query['includeRecent'] = request.include_recent
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse(),
            self.do_roarequest('GetRelatedWorkspaces', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces', 'json', req, runtime)
        )

    async def get_related_workspaces_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest,
        headers: dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_recent):
            query['includeRecent'] = request.include_recent
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetRelatedWorkspacesResponse(),
            await self.do_roarequest_async('GetRelatedWorkspaces', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces', 'json', req, runtime)
        )

    def get_sheet(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.GetSheetRequest,
    ) -> dingtalkdoc__1__0_models.GetSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetSheetHeaders()
        return self.get_sheet_with_options(workbook_id, sheet_id, request, headers, runtime)

    async def get_sheet_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.GetSheetRequest,
    ) -> dingtalkdoc__1__0_models.GetSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetSheetHeaders()
        return await self.get_sheet_with_options_async(workbook_id, sheet_id, request, headers, runtime)

    def get_sheet_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.GetSheetRequest,
        headers: dingtalkdoc__1__0_models.GetSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetSheetResponse(),
            self.do_roarequest('GetSheet', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'json', req, runtime)
        )

    async def get_sheet_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.GetSheetRequest,
        headers: dingtalkdoc__1__0_models.GetSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetSheetResponse(),
            await self.do_roarequest_async('GetSheet', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'json', req, runtime)
        )

    def get_workspace(
        self,
        workspace_id: str,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetWorkspaceHeaders()
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_id: str,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetWorkspaceHeaders()
        return await self.get_workspace_with_options_async(workspace_id, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_id: str,
        headers: dingtalkdoc__1__0_models.GetWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetWorkspaceResponse(),
            self.do_roarequest('GetWorkspace', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/{workspace_id}', 'json', req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_id: str,
        headers: dingtalkdoc__1__0_models.GetWorkspaceHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceResponse:
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetWorkspaceResponse(),
            await self.do_roarequest_async('GetWorkspace', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/{workspace_id}', 'json', req, runtime)
        )

    def get_workspace_node(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.GetWorkspaceNodeRequest,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetWorkspaceNodeHeaders()
        return self.get_workspace_node_with_options(workspace_id, node_id, request, headers, runtime)

    async def get_workspace_node_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.GetWorkspaceNodeRequest,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceNodeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.GetWorkspaceNodeHeaders()
        return await self.get_workspace_node_with_options_async(workspace_id, node_id, request, headers, runtime)

    def get_workspace_node_with_options(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.GetWorkspaceNodeRequest,
        headers: dingtalkdoc__1__0_models.GetWorkspaceNodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceNodeResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetWorkspaceNodeResponse(),
            self.do_roarequest('GetWorkspaceNode', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}', 'json', req, runtime)
        )

    async def get_workspace_node_with_options_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.GetWorkspaceNodeRequest,
        headers: dingtalkdoc__1__0_models.GetWorkspaceNodeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.GetWorkspaceNodeResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.GetWorkspaceNodeResponse(),
            await self.do_roarequest_async('GetWorkspaceNode', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}', 'json', req, runtime)
        )

    def search_workspace_docs(
        self,
        request: dingtalkdoc__1__0_models.SearchWorkspaceDocsRequest,
    ) -> dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.SearchWorkspaceDocsHeaders()
        return self.search_workspace_docs_with_options(request, headers, runtime)

    async def search_workspace_docs_async(
        self,
        request: dingtalkdoc__1__0_models.SearchWorkspaceDocsRequest,
    ) -> dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.SearchWorkspaceDocsHeaders()
        return await self.search_workspace_docs_with_options_async(request, headers, runtime)

    def search_workspace_docs_with_options(
        self,
        request: dingtalkdoc__1__0_models.SearchWorkspaceDocsRequest,
        headers: dingtalkdoc__1__0_models.SearchWorkspaceDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse(),
            self.do_roarequest('SearchWorkspaceDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/docs', 'json', req, runtime)
        )

    async def search_workspace_docs_with_options_async(
        self,
        request: dingtalkdoc__1__0_models.SearchWorkspaceDocsRequest,
        headers: dingtalkdoc__1__0_models.SearchWorkspaceDocsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.SearchWorkspaceDocsResponse(),
            await self.do_roarequest_async('SearchWorkspaceDocs', 'doc_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/doc/docs', 'json', req, runtime)
        )

    def update_range(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.UpdateRangeRequest,
    ) -> dingtalkdoc__1__0_models.UpdateRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateRangeHeaders()
        return self.update_range_with_options(workbook_id, sheet_id, range_address, request, headers, runtime)

    async def update_range_async(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.UpdateRangeRequest,
    ) -> dingtalkdoc__1__0_models.UpdateRangeResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateRangeHeaders()
        return await self.update_range_with_options_async(workbook_id, sheet_id, range_address, request, headers, runtime)

    def update_range_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.UpdateRangeRequest,
        headers: dingtalkdoc__1__0_models.UpdateRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateRangeResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        range_address = OpenApiUtilClient.get_encode_param(range_address)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.background_colors):
            body['backgroundColors'] = request.background_colors
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateRangeResponse(),
            self.do_roarequest('UpdateRange', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/ranges/{range_address}', 'none', req, runtime)
        )

    async def update_range_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        range_address: str,
        request: dingtalkdoc__1__0_models.UpdateRangeRequest,
        headers: dingtalkdoc__1__0_models.UpdateRangeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateRangeResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        range_address = OpenApiUtilClient.get_encode_param(range_address)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.background_colors):
            body['backgroundColors'] = request.background_colors
        if not UtilClient.is_unset(request.values):
            body['values'] = request.values
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateRangeResponse(),
            await self.do_roarequest_async('UpdateRange', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}/ranges/{range_address}', 'none', req, runtime)
        )

    def update_sheet(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.UpdateSheetRequest,
    ) -> dingtalkdoc__1__0_models.UpdateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateSheetHeaders()
        return self.update_sheet_with_options(workbook_id, sheet_id, request, headers, runtime)

    async def update_sheet_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.UpdateSheetRequest,
    ) -> dingtalkdoc__1__0_models.UpdateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateSheetHeaders()
        return await self.update_sheet_with_options_async(workbook_id, sheet_id, request, headers, runtime)

    def update_sheet_with_options(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.UpdateSheetRequest,
        headers: dingtalkdoc__1__0_models.UpdateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.visibility):
            body['visibility'] = request.visibility
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateSheetResponse(),
            self.do_roarequest('UpdateSheet', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'none', req, runtime)
        )

    async def update_sheet_with_options_async(
        self,
        workbook_id: str,
        sheet_id: str,
        request: dingtalkdoc__1__0_models.UpdateSheetRequest,
        headers: dingtalkdoc__1__0_models.UpdateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateSheetResponse:
        UtilClient.validate_model(request)
        workbook_id = OpenApiUtilClient.get_encode_param(workbook_id)
        sheet_id = OpenApiUtilClient.get_encode_param(sheet_id)
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.visibility):
            body['visibility'] = request.visibility
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateSheetResponse(),
            await self.do_roarequest_async('UpdateSheet', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workbooks/{workbook_id}/sheets/{sheet_id}', 'none', req, runtime)
        )

    def update_workspace_doc_members(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersHeaders()
        return self.update_workspace_doc_members_with_options(workspace_id, node_id, request, headers, runtime)

    async def update_workspace_doc_members_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersRequest,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersHeaders()
        return await self.update_workspace_doc_members_with_options_async(workspace_id, node_id, request, headers, runtime)

    def update_workspace_doc_members_with_options(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse(),
            self.do_roarequest('UpdateWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members', 'none', req, runtime)
        )

    async def update_workspace_doc_members_with_options_async(
        self,
        workspace_id: str,
        node_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersRequest,
        headers: dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateWorkspaceDocMembersResponse(),
            await self.do_roarequest_async('UpdateWorkspaceDocMembers', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/docs/{node_id}/members', 'none', req, runtime)
        )

    def update_workspace_members(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateWorkspaceMembersHeaders()
        return self.update_workspace_members_with_options(workspace_id, request, headers, runtime)

    async def update_workspace_members_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceMembersRequest,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkdoc__1__0_models.UpdateWorkspaceMembersHeaders()
        return await self.update_workspace_members_with_options_async(workspace_id, request, headers, runtime)

    def update_workspace_members_with_options(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.UpdateWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse(),
            self.do_roarequest('UpdateWorkspaceMembers', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members', 'none', req, runtime)
        )

    async def update_workspace_members_with_options_async(
        self,
        workspace_id: str,
        request: dingtalkdoc__1__0_models.UpdateWorkspaceMembersRequest,
        headers: dingtalkdoc__1__0_models.UpdateWorkspaceMembersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse:
        UtilClient.validate_model(request)
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        body = {}
        if not UtilClient.is_unset(request.members):
            body['members'] = request.members
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_dingtalk_access_token):
            real_headers['x-acs-dingtalk-access-token'] = UtilClient.to_jsonstring(headers.x_acs_dingtalk_access_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            dingtalkdoc__1__0_models.UpdateWorkspaceMembersResponse(),
            await self.do_roarequest_async('UpdateWorkspaceMembers', 'doc_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/doc/workspaces/{workspace_id}/members', 'none', req, runtime)
        )
