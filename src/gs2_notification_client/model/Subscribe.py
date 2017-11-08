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

class Subscribe(object):

    def __init__(self, params=None):
        if params is None:
            self.__endpoint = None
            self.__type = None
            self.__owner_id = None
            self.__notification_id = None
            self.__subscribe_id = None
            self.__update_at = None
            self.__create_at = None
        else:
            self.set_endpoint(params['endpoint'] if 'endpoint' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_notification_id(params['notificationId'] if 'notificationId' in params.keys() else None)
            self.set_subscribe_id(params['subscribeId'] if 'subscribeId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)


    def get_endpoint(self):
        """
        type = email: メールアドレス
type = http/https: URL
を取得
        :return: type = email: メールアドレス
type = http/https: URL

        :rtype: unicode
        """
        return self.__endpoint

    def set_endpoint(self, endpoint):
        """
        type = email: メールアドレス
type = http/https: URL
を設定
        :param endpoint: type = email: メールアドレス
type = http/https: URL

        :type endpoint: unicode
        """
        self.__endpoint = endpoint

    def get_type(self):
        """
        通知方法を取得
        :return: 通知方法
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type):
        """
        通知方法を設定
        :param type: 通知方法
        :type type: unicode
        """
        self.__type = type

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_notification_id(self):
        """
        通知GRNを取得
        :return: 通知GRN
        :rtype: unicode
        """
        return self.__notification_id

    def set_notification_id(self, notification_id):
        """
        通知GRNを設定
        :param notification_id: 通知GRN
        :type notification_id: unicode
        """
        self.__notification_id = notification_id

    def get_subscribe_id(self):
        """
        購読GRNを取得
        :return: 購読GRN
        :rtype: unicode
        """
        return self.__subscribe_id

    def set_subscribe_id(self, subscribe_id):
        """
        購読GRNを設定
        :param subscribe_id: 購読GRN
        :type subscribe_id: unicode
        """
        self.__subscribe_id = subscribe_id

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def to_dict(self):
        return { 
            "endpoint": self.__endpoint,
            "type": self.__type,
            "ownerId": self.__owner_id,
            "notificationId": self.__notification_id,
            "subscribeId": self.__subscribe_id,
            "updateAt": self.__update_at,
            "createAt": self.__create_at,
        }