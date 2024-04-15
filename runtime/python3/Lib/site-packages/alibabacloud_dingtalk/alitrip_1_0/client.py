# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
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

    def add_city_car_apply(
        self,
        request: dingtalkalitrip__1__0_models.AddCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.AddCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.AddCityCarApplyHeaders()
        return self.add_city_car_apply_with_options(request, headers, runtime)

    async def add_city_car_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.AddCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.AddCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.AddCityCarApplyHeaders()
        return await self.add_city_car_apply_with_options_async(request, headers, runtime)

    def add_city_car_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.AddCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.AddCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.AddCityCarApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['cause'] = request.cause
        if not UtilClient.is_unset(request.city):
            body['city'] = request.city
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.date):
            body['date'] = request.date
        if not UtilClient.is_unset(request.finished_date):
            body['finishedDate'] = request.finished_date
        if not UtilClient.is_unset(request.project_code):
            body['projectCode'] = request.project_code
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['thirdPartCostCenterId'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['thirdPartInvoiceId'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.times_total):
            body['timesTotal'] = request.times_total
        if not UtilClient.is_unset(request.times_type):
            body['timesType'] = request.times_type
        if not UtilClient.is_unset(request.times_used):
            body['timesUsed'] = request.times_used
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.AddCityCarApplyResponse(),
            self.do_roarequest('AddCityCarApply', 'alitrip_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    async def add_city_car_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.AddCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.AddCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.AddCityCarApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['cause'] = request.cause
        if not UtilClient.is_unset(request.city):
            body['city'] = request.city
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.date):
            body['date'] = request.date
        if not UtilClient.is_unset(request.finished_date):
            body['finishedDate'] = request.finished_date
        if not UtilClient.is_unset(request.project_code):
            body['projectCode'] = request.project_code
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.third_part_cost_center_id):
            body['thirdPartCostCenterId'] = request.third_part_cost_center_id
        if not UtilClient.is_unset(request.third_part_invoice_id):
            body['thirdPartInvoiceId'] = request.third_part_invoice_id
        if not UtilClient.is_unset(request.times_total):
            body['timesTotal'] = request.times_total
        if not UtilClient.is_unset(request.times_type):
            body['timesType'] = request.times_type
        if not UtilClient.is_unset(request.times_used):
            body['timesUsed'] = request.times_used
        if not UtilClient.is_unset(request.title):
            body['title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.AddCityCarApplyResponse(),
            await self.do_roarequest_async('AddCityCarApply', 'alitrip_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    def approve_city_car_apply(
        self,
        request: dingtalkalitrip__1__0_models.ApproveCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.ApproveCityCarApplyHeaders()
        return self.approve_city_car_apply_with_options(request, headers, runtime)

    async def approve_city_car_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.ApproveCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.ApproveCityCarApplyHeaders()
        return await self.approve_city_car_apply_with_options_async(request, headers, runtime)

    def approve_city_car_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.ApproveCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.ApproveCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.operate_time):
            body['operateTime'] = request.operate_time
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse(),
            self.do_roarequest('ApproveCityCarApply', 'alitrip_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    async def approve_city_car_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.ApproveCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.ApproveCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.operate_time):
            body['operateTime'] = request.operate_time
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.third_part_apply_id):
            body['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.ApproveCityCarApplyResponse(),
            await self.do_roarequest_async('ApproveCityCarApply', 'alitrip_1.0', 'HTTP', 'PUT', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    def bill_settement_btrip_train(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementBtripTrainRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementBtripTrainHeaders()
        return self.bill_settement_btrip_train_with_options(request, headers, runtime)

    async def bill_settement_btrip_train_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementBtripTrainRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementBtripTrainHeaders()
        return await self.bill_settement_btrip_train_with_options_async(request, headers, runtime)

    def bill_settement_btrip_train_with_options(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementBtripTrainRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementBtripTrainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse(),
            self.do_roarequest('BillSettementBtripTrain', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/btripTrains', 'json', req, runtime)
        )

    async def bill_settement_btrip_train_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementBtripTrainRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementBtripTrainHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementBtripTrainResponse(),
            await self.do_roarequest_async('BillSettementBtripTrain', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/btripTrains', 'json', req, runtime)
        )

    def bill_settement_car(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementCarRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementCarResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementCarHeaders()
        return self.bill_settement_car_with_options(request, headers, runtime)

    async def bill_settement_car_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementCarRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementCarResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementCarHeaders()
        return await self.bill_settement_car_with_options_async(request, headers, runtime)

    def bill_settement_car_with_options(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementCarRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementCarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementCarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementCarResponse(),
            self.do_roarequest('BillSettementCar', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/cars', 'json', req, runtime)
        )

    async def bill_settement_car_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementCarRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementCarHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementCarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementCarResponse(),
            await self.do_roarequest_async('BillSettementCar', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/cars', 'json', req, runtime)
        )

    def bill_settement_flight(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementFlightRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementFlightResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementFlightHeaders()
        return self.bill_settement_flight_with_options(request, headers, runtime)

    async def bill_settement_flight_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementFlightRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementFlightResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementFlightHeaders()
        return await self.bill_settement_flight_with_options_async(request, headers, runtime)

    def bill_settement_flight_with_options(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementFlightRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementFlightHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementFlightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementFlightResponse(),
            self.do_roarequest('BillSettementFlight', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/flights', 'json', req, runtime)
        )

    async def bill_settement_flight_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementFlightRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementFlightHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementFlightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementFlightResponse(),
            await self.do_roarequest_async('BillSettementFlight', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/flights', 'json', req, runtime)
        )

    def bill_settement_hotel(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementHotelRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementHotelResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementHotelHeaders()
        return self.bill_settement_hotel_with_options(request, headers, runtime)

    async def bill_settement_hotel_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementHotelRequest,
    ) -> dingtalkalitrip__1__0_models.BillSettementHotelResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.BillSettementHotelHeaders()
        return await self.bill_settement_hotel_with_options_async(request, headers, runtime)

    def bill_settement_hotel_with_options(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementHotelRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementHotelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementHotelResponse(),
            self.do_roarequest('BillSettementHotel', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/hotels', 'json', req, runtime)
        )

    async def bill_settement_hotel_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.BillSettementHotelRequest,
        headers: dingtalkalitrip__1__0_models.BillSettementHotelHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.BillSettementHotelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.period_end):
            query['periodEnd'] = request.period_end
        if not UtilClient.is_unset(request.period_start):
            query['periodStart'] = request.period_start
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
            dingtalkalitrip__1__0_models.BillSettementHotelResponse(),
            await self.do_roarequest_async('BillSettementHotel', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/billSettlements/hotels', 'json', req, runtime)
        )

    def get_flight_exceed_apply(
        self,
        request: dingtalkalitrip__1__0_models.GetFlightExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetFlightExceedApplyHeaders()
        return self.get_flight_exceed_apply_with_options(request, headers, runtime)

    async def get_flight_exceed_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.GetFlightExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetFlightExceedApplyHeaders()
        return await self.get_flight_exceed_apply_with_options_async(request, headers, runtime)

    def get_flight_exceed_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.GetFlightExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetFlightExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse(),
            self.do_roarequest('GetFlightExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getFlight', 'json', req, runtime)
        )

    async def get_flight_exceed_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.GetFlightExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetFlightExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetFlightExceedApplyResponse(),
            await self.do_roarequest_async('GetFlightExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getFlight', 'json', req, runtime)
        )

    def get_hotel_exceed_apply(
        self,
        request: dingtalkalitrip__1__0_models.GetHotelExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetHotelExceedApplyHeaders()
        return self.get_hotel_exceed_apply_with_options(request, headers, runtime)

    async def get_hotel_exceed_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.GetHotelExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetHotelExceedApplyHeaders()
        return await self.get_hotel_exceed_apply_with_options_async(request, headers, runtime)

    def get_hotel_exceed_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.GetHotelExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetHotelExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse(),
            self.do_roarequest('GetHotelExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getHotel', 'json', req, runtime)
        )

    async def get_hotel_exceed_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.GetHotelExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetHotelExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetHotelExceedApplyResponse(),
            await self.do_roarequest_async('GetHotelExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getHotel', 'json', req, runtime)
        )

    def get_train_exceed_apply(
        self,
        request: dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders()
        return self.get_train_exceed_apply_with_options(request, headers, runtime)

    async def get_train_exceed_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders()
        return await self.get_train_exceed_apply_with_options_async(request, headers, runtime)

    def get_train_exceed_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse(),
            self.do_roarequest('GetTrainExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getTrain', 'json', req, runtime)
        )

    async def get_train_exceed_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
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
            dingtalkalitrip__1__0_models.GetTrainExceedApplyResponse(),
            await self.do_roarequest_async('GetTrainExceedApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/exceedapply/getTrain', 'json', req, runtime)
        )

    def query_city_car_apply(
        self,
        request: dingtalkalitrip__1__0_models.QueryCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.QueryCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders()
        return self.query_city_car_apply_with_options(request, headers, runtime)

    async def query_city_car_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.QueryCityCarApplyRequest,
    ) -> dingtalkalitrip__1__0_models.QueryCityCarApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders()
        return await self.query_city_car_apply_with_options_async(request, headers, runtime)

    def query_city_car_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.QueryCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.QueryCityCarApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.created_end_at):
            query['createdEndAt'] = request.created_end_at
        if not UtilClient.is_unset(request.created_start_at):
            query['createdStartAt'] = request.created_start_at
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.QueryCityCarApplyResponse(),
            self.do_roarequest('QueryCityCarApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    async def query_city_car_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.QueryCityCarApplyRequest,
        headers: dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.QueryCityCarApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.created_end_at):
            query['createdEndAt'] = request.created_end_at
        if not UtilClient.is_unset(request.created_start_at):
            query['createdStartAt'] = request.created_start_at
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.QueryCityCarApplyResponse(),
            await self.do_roarequest_async('QueryCityCarApply', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/cityCarApprovals', 'json', req, runtime)
        )

    def query_union_order(
        self,
        request: dingtalkalitrip__1__0_models.QueryUnionOrderRequest,
    ) -> dingtalkalitrip__1__0_models.QueryUnionOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.QueryUnionOrderHeaders()
        return self.query_union_order_with_options(request, headers, runtime)

    async def query_union_order_async(
        self,
        request: dingtalkalitrip__1__0_models.QueryUnionOrderRequest,
    ) -> dingtalkalitrip__1__0_models.QueryUnionOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.QueryUnionOrderHeaders()
        return await self.query_union_order_with_options_async(request, headers, runtime)

    def query_union_order_with_options(
        self,
        request: dingtalkalitrip__1__0_models.QueryUnionOrderRequest,
        headers: dingtalkalitrip__1__0_models.QueryUnionOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.QueryUnionOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.union_no):
            query['unionNo'] = request.union_no
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
            dingtalkalitrip__1__0_models.QueryUnionOrderResponse(),
            self.do_roarequest('QueryUnionOrder', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/unionOrders', 'json', req, runtime)
        )

    async def query_union_order_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.QueryUnionOrderRequest,
        headers: dingtalkalitrip__1__0_models.QueryUnionOrderHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.QueryUnionOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.third_part_apply_id):
            query['thirdPartApplyId'] = request.third_part_apply_id
        if not UtilClient.is_unset(request.union_no):
            query['unionNo'] = request.union_no
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
            dingtalkalitrip__1__0_models.QueryUnionOrderResponse(),
            await self.do_roarequest_async('QueryUnionOrder', 'alitrip_1.0', 'HTTP', 'GET', 'AK', f'/v1.0/alitrip/unionOrders', 'json', req, runtime)
        )

    def sync_exceed_apply(
        self,
        request: dingtalkalitrip__1__0_models.SyncExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.SyncExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.SyncExceedApplyHeaders()
        return self.sync_exceed_apply_with_options(request, headers, runtime)

    async def sync_exceed_apply_async(
        self,
        request: dingtalkalitrip__1__0_models.SyncExceedApplyRequest,
    ) -> dingtalkalitrip__1__0_models.SyncExceedApplyResponse:
        runtime = util_models.RuntimeOptions()
        headers = dingtalkalitrip__1__0_models.SyncExceedApplyHeaders()
        return await self.sync_exceed_apply_with_options_async(request, headers, runtime)

    def sync_exceed_apply_with_options(
        self,
        request: dingtalkalitrip__1__0_models.SyncExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.SyncExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.SyncExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdpartyFlowId'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.SyncExceedApplyResponse(),
            self.do_roarequest('SyncExceedApply', 'alitrip_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/alitrip/exceedapply/sync', 'json', req, runtime)
        )

    async def sync_exceed_apply_with_options_async(
        self,
        request: dingtalkalitrip__1__0_models.SyncExceedApplyRequest,
        headers: dingtalkalitrip__1__0_models.SyncExceedApplyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> dingtalkalitrip__1__0_models.SyncExceedApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['applyId'] = request.apply_id
        if not UtilClient.is_unset(request.corp_id):
            query['corpId'] = request.corp_id
        if not UtilClient.is_unset(request.remark):
            query['remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.thirdparty_flow_id):
            query['thirdpartyFlowId'] = request.thirdparty_flow_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            dingtalkalitrip__1__0_models.SyncExceedApplyResponse(),
            await self.do_roarequest_async('SyncExceedApply', 'alitrip_1.0', 'HTTP', 'POST', 'AK', f'/v1.0/alitrip/exceedapply/sync', 'json', req, runtime)
        )
