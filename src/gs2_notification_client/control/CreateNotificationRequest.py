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


class CreateNotificationRequest(Gs2BasicRequest):

    class Constant(Gs2Notification):
        FUNCTION = "CreateNotification"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateNotificationRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_name(self):
        """
        通知の名前を取得
        :return: 通知の名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        通知の名前を設定
        :param name: 通知の名前
        :type name: unicode
        """
        if name is not None and not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        通知の名前を設定
        :param name: 通知の名前
        :type name: unicode
        :return: this
        :rtype: CreateNotificationRequest
        """
        self.set_name(name)
        return self

    def get_description(self):
        """
        通知の説明を取得
        :return: 通知の説明
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        通知の説明を設定
        :param description: 通知の説明
        :type description: unicode
        """
        if description is not None and not (isinstance(description, str) or isinstance(description, unicode)):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        通知の説明を設定
        :param description: 通知の説明
        :type description: unicode
        :return: this
        :rtype: CreateNotificationRequest
        """
        self.set_description(description)
        return self
