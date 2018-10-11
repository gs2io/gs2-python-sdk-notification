# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2NotificationClient(AbstractGs2Client):

    ENDPOINT = "notification"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2NotificationClient, self).__init__(credential, region)

    def create_notification(self, request):
        """
        通知を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_notification_client.control.CreateNotificationRequest.CreateNotificationRequest
        :return: 結果
        :rtype: gs2_notification_client.control.CreateNotificationResult.CreateNotificationResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.CreateNotificationRequest import CreateNotificationRequest
        from gs2_notification_client.control.CreateNotificationResult import CreateNotificationResult
        return CreateNotificationResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification",
            service=self.ENDPOINT,
            component=CreateNotificationRequest.Constant.MODULE,
            target_function=CreateNotificationRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_notification(self, request):
        """
        通知を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_notification_client.control.DeleteNotificationRequest.DeleteNotificationRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.DeleteNotificationRequest import DeleteNotificationRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "",
            service=self.ENDPOINT,
            component=DeleteNotificationRequest.Constant.MODULE,
            target_function=DeleteNotificationRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_notification(self, request):
        """
        通知の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_notification_client.control.DescribeNotificationRequest.DescribeNotificationRequest
        :return: 結果
        :rtype: gs2_notification_client.control.DescribeNotificationResult.DescribeNotificationResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.DescribeNotificationRequest import DescribeNotificationRequest

        from gs2_notification_client.control.DescribeNotificationResult import DescribeNotificationResult
        return DescribeNotificationResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification",
            service=self.ENDPOINT,
            component=DescribeNotificationRequest.Constant.MODULE,
            target_function=DescribeNotificationRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_notification(self, request):
        """
        通知を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_notification_client.control.GetNotificationRequest.GetNotificationRequest
        :return: 結果
        :rtype: gs2_notification_client.control.GetNotificationResult.GetNotificationResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.GetNotificationRequest import GetNotificationRequest

        from gs2_notification_client.control.GetNotificationResult import GetNotificationResult
        return GetNotificationResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "",
            service=self.ENDPOINT,
            component=GetNotificationRequest.Constant.MODULE,
            target_function=GetNotificationRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_notification(self, request):
        """
        通知を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_notification_client.control.UpdateNotificationRequest.UpdateNotificationRequest
        :return: 結果
        :rtype: gs2_notification_client.control.UpdateNotificationResult.UpdateNotificationResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.UpdateNotificationRequest import UpdateNotificationRequest
        from gs2_notification_client.control.UpdateNotificationResult import UpdateNotificationResult
        return UpdateNotificationResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "",
            service=self.ENDPOINT,
            component=UpdateNotificationRequest.Constant.MODULE,
            target_function=UpdateNotificationRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_subscribe(self, request):
        """
        購読を作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_notification_client.control.CreateSubscribeRequest.CreateSubscribeRequest
        :return: 結果
        :rtype: gs2_notification_client.control.CreateSubscribeResult.CreateSubscribeResult
        """
        body = { 
            "type": request.get_type(),
            "endpoint": request.get_endpoint(),
        }

        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.CreateSubscribeRequest import CreateSubscribeRequest
        from gs2_notification_client.control.CreateSubscribeResult import CreateSubscribeResult
        return CreateSubscribeResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "/subscribe",
            service=self.ENDPOINT,
            component=CreateSubscribeRequest.Constant.MODULE,
            target_function=CreateSubscribeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_subscribe(self, request):
        """
        購読を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_notification_client.control.DeleteSubscribeRequest.DeleteSubscribeRequest
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.DeleteSubscribeRequest import DeleteSubscribeRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "/subscribe/" + str(("null" if request.get_subscribe_id() is None or request.get_subscribe_id() == "" else request.get_subscribe_id())) + "",
            service=self.ENDPOINT,
            component=DeleteSubscribeRequest.Constant.MODULE,
            target_function=DeleteSubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_subscribe(self, request):
        """
        購読の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_notification_client.control.DescribeSubscribeRequest.DescribeSubscribeRequest
        :return: 結果
        :rtype: gs2_notification_client.control.DescribeSubscribeResult.DescribeSubscribeResult
        """
        query_strings = {}
        if request.get_page_token() is not None:
            query_strings['pageToken'] = request.get_page_token()
        if request.get_limit() is not None:
            query_strings['limit'] = request.get_limit()
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.DescribeSubscribeRequest import DescribeSubscribeRequest

        from gs2_notification_client.control.DescribeSubscribeResult import DescribeSubscribeResult
        return DescribeSubscribeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "/subscribe",
            service=self.ENDPOINT,
            component=DescribeSubscribeRequest.Constant.MODULE,
            target_function=DescribeSubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_subscribe(self, request):
        """
        購読を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_notification_client.control.GetSubscribeRequest.GetSubscribeRequest
        :return: 結果
        :rtype: gs2_notification_client.control.GetSubscribeResult.GetSubscribeResult
        """
        query_strings = {}
        headers = {}
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_notification_client.control.GetSubscribeRequest import GetSubscribeRequest

        from gs2_notification_client.control.GetSubscribeResult import GetSubscribeResult
        return GetSubscribeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/notification/" + str(("null" if request.get_notification_name() is None or request.get_notification_name() == "" else request.get_notification_name())) + "/subscribe/" + str(("null" if request.get_subscribe_id() is None or request.get_subscribe_id() == "" else request.get_subscribe_id())) + "",
            service=self.ENDPOINT,
            component=GetSubscribeRequest.Constant.MODULE,
            target_function=GetSubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
