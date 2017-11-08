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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_notification_client.Gs2Notification import Gs2Notification


class DeleteSubscribeRequest(Gs2BasicRequest):

    class Constant(Gs2Notification):
        FUNCTION = "DeleteSubscribe"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteSubscribeRequest, self).__init__(params)
        if params is None:
            self.__notification_name = None
            self.__subscribe_id = None
        else:
            self.set_notification_name(params['notificationName'] if 'notificationName' in params.keys() else None)
            self.set_subscribe_id(params['subscribeId'] if 'subscribeId' in params.keys() else None)

    def get_notification_name(self):
        """
        通知の名前を指定します。を取得
        :return: 通知の名前を指定します。
        :rtype: unicode
        """
        return self.__notification_name

    def set_notification_name(self, notification_name):
        """
        通知の名前を指定します。を設定
        :param notification_name: 通知の名前を指定します。
        :type notification_name: unicode
        """
        self.__notification_name = notification_name

    def with_notification_name(self, notification_name):
        """
        通知の名前を指定します。を設定
        :param notification_name: 通知の名前を指定します。
        :type notification_name: unicode
        :return: this
        :rtype: DeleteSubscribeRequest
        """
        self.set_notification_name(notification_name)
        return self

    def get_subscribe_id(self):
        """
        削除する購読IDを指定します。を取得
        :return: 削除する購読IDを指定します。
        :rtype: unicode
        """
        return self.__subscribe_id

    def set_subscribe_id(self, subscribe_id):
        """
        削除する購読IDを指定します。を設定
        :param subscribe_id: 削除する購読IDを指定します。
        :type subscribe_id: unicode
        """
        self.__subscribe_id = subscribe_id

    def with_subscribe_id(self, subscribe_id):
        """
        削除する購読IDを指定します。を設定
        :param subscribe_id: 削除する購読IDを指定します。
        :type subscribe_id: unicode
        :return: this
        :rtype: DeleteSubscribeRequest
        """
        self.set_subscribe_id(subscribe_id)
        return self
