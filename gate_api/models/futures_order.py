# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.6.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FuturesOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'user': 'int',
        'create_time': 'float',
        'finish_time': 'float',
        'finish_as': 'str',
        'status': 'str',
        'contract': 'str',
        'size': 'int',
        'iceberg': 'int',
        'price': 'str',
        'close': 'bool',
        'is_close': 'bool',
        'reduce_only': 'bool',
        'is_reduce_only': 'bool',
        'is_liq': 'bool',
        'tif': 'str',
        'left': 'int',
        'fill_price': 'str',
        'text': 'str',
        'tkfr': 'str',
        'mkfr': 'str',
        'refu': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'finish_as': 'finish_as',
        'status': 'status',
        'contract': 'contract',
        'size': 'size',
        'iceberg': 'iceberg',
        'price': 'price',
        'close': 'close',
        'is_close': 'is_close',
        'reduce_only': 'reduce_only',
        'is_reduce_only': 'is_reduce_only',
        'is_liq': 'is_liq',
        'tif': 'tif',
        'left': 'left',
        'fill_price': 'fill_price',
        'text': 'text',
        'tkfr': 'tkfr',
        'mkfr': 'mkfr',
        'refu': 'refu'
    }

    def __init__(self, id=None, user=None, create_time=None, finish_time=None, finish_as=None, status=None, contract=None, size=None, iceberg=None, price=None, close=False, is_close=None, reduce_only=False, is_reduce_only=None, is_liq=None, tif='gtc', left=None, fill_price=None, text=None, tkfr=None, mkfr=None, refu=None):  # noqa: E501
        """FuturesOrder - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._user = None
        self._create_time = None
        self._finish_time = None
        self._finish_as = None
        self._status = None
        self._contract = None
        self._size = None
        self._iceberg = None
        self._price = None
        self._close = None
        self._is_close = None
        self._reduce_only = None
        self._is_reduce_only = None
        self._is_liq = None
        self._tif = None
        self._left = None
        self._fill_price = None
        self._text = None
        self._tkfr = None
        self._mkfr = None
        self._refu = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if finish_as is not None:
            self.finish_as = finish_as
        if status is not None:
            self.status = status
        self.contract = contract
        if size is not None:
            self.size = size
        if iceberg is not None:
            self.iceberg = iceberg
        if price is not None:
            self.price = price
        if close is not None:
            self.close = close
        if is_close is not None:
            self.is_close = is_close
        if reduce_only is not None:
            self.reduce_only = reduce_only
        if is_reduce_only is not None:
            self.is_reduce_only = is_reduce_only
        if is_liq is not None:
            self.is_liq = is_liq
        if tif is not None:
            self.tif = tif
        if left is not None:
            self.left = left
        if fill_price is not None:
            self.fill_price = fill_price
        if text is not None:
            self.text = text
        if tkfr is not None:
            self.tkfr = tkfr
        if mkfr is not None:
            self.mkfr = mkfr
        if refu is not None:
            self.refu = refu

    @property
    def id(self):
        """Gets the id of this FuturesOrder.  # noqa: E501

        Futures order ID  # noqa: E501

        :return: The id of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FuturesOrder.

        Futures order ID  # noqa: E501

        :param id: The id of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this FuturesOrder.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FuturesOrder.

        User ID  # noqa: E501

        :param user: The user of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def create_time(self):
        """Gets the create_time of this FuturesOrder.  # noqa: E501

        Order creation time  # noqa: E501

        :return: The create_time of this FuturesOrder.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FuturesOrder.

        Order creation time  # noqa: E501

        :param create_time: The create_time of this FuturesOrder.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this FuturesOrder.  # noqa: E501

        Order finished time. Not returned if order is open  # noqa: E501

        :return: The finish_time of this FuturesOrder.  # noqa: E501
        :rtype: float
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this FuturesOrder.

        Order finished time. Not returned if order is open  # noqa: E501

        :param finish_time: The finish_time of this FuturesOrder.  # noqa: E501
        :type: float
        """

        self._finish_time = finish_time

    @property
    def finish_as(self):
        """Gets the finish_as of this FuturesOrder.  # noqa: E501

        How the order is finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is `IOC`, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while `reduce-only` set  # noqa: E501

        :return: The finish_as of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._finish_as

    @finish_as.setter
    def finish_as(self, finish_as):
        """Sets the finish_as of this FuturesOrder.

        How the order is finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is `IOC`, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while `reduce-only` set  # noqa: E501

        :param finish_as: The finish_as of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["filled", "cancelled", "liquidated", "ioc", "auto_deleveraged", "reduce_only"]  # noqa: E501
        if finish_as not in allowed_values:
            raise ValueError(
                "Invalid value for `finish_as` ({0}), must be one of {1}"  # noqa: E501
                .format(finish_as, allowed_values)
            )

        self._finish_as = finish_as

    @property
    def status(self):
        """Gets the status of this FuturesOrder.  # noqa: E501

        Order status  - `open`: waiting to be traded - `finished`: finished  # noqa: E501

        :return: The status of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FuturesOrder.

        Order status  - `open`: waiting to be traded - `finished`: finished  # noqa: E501

        :param status: The status of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "finished"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def contract(self):
        """Gets the contract of this FuturesOrder.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this FuturesOrder.

        Futures contract  # noqa: E501

        :param contract: The contract of this FuturesOrder.  # noqa: E501
        :type: str
        """
        if contract is None:
            raise ValueError("Invalid value for `contract`, must not be `None`")  # noqa: E501

        self._contract = contract

    @property
    def size(self):
        """Gets the size of this FuturesOrder.  # noqa: E501

        Order size. Specify positive number to make a bid, and negative number to ask  # noqa: E501

        :return: The size of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FuturesOrder.

        Order size. Specify positive number to make a bid, and negative number to ask  # noqa: E501

        :param size: The size of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def iceberg(self):
        """Gets the iceberg of this FuturesOrder.  # noqa: E501

        Display size for iceberg order. 0 for non-iceberg. Note that you would pay the taker fee for the hidden size  # noqa: E501

        :return: The iceberg of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._iceberg

    @iceberg.setter
    def iceberg(self, iceberg):
        """Sets the iceberg of this FuturesOrder.

        Display size for iceberg order. 0 for non-iceberg. Note that you would pay the taker fee for the hidden size  # noqa: E501

        :param iceberg: The iceberg of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._iceberg = iceberg

    @property
    def price(self):
        """Gets the price of this FuturesOrder.  # noqa: E501

        Order price. 0 for market order with `tif` set as `ioc`  # noqa: E501

        :return: The price of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this FuturesOrder.

        Order price. 0 for market order with `tif` set as `ioc`  # noqa: E501

        :param price: The price of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def close(self):
        """Gets the close of this FuturesOrder.  # noqa: E501

        Set as `true` to close the position, with `size` set to 0  # noqa: E501

        :return: The close of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this FuturesOrder.

        Set as `true` to close the position, with `size` set to 0  # noqa: E501

        :param close: The close of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._close = close

    @property
    def is_close(self):
        """Gets the is_close of this FuturesOrder.  # noqa: E501

        Is the order to close position  # noqa: E501

        :return: The is_close of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_close

    @is_close.setter
    def is_close(self, is_close):
        """Sets the is_close of this FuturesOrder.

        Is the order to close position  # noqa: E501

        :param is_close: The is_close of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_close = is_close

    @property
    def reduce_only(self):
        """Gets the reduce_only of this FuturesOrder.  # noqa: E501

        Set as `true` to be post-only order  # noqa: E501

        :return: The reduce_only of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._reduce_only

    @reduce_only.setter
    def reduce_only(self, reduce_only):
        """Sets the reduce_only of this FuturesOrder.

        Set as `true` to be post-only order  # noqa: E501

        :param reduce_only: The reduce_only of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._reduce_only = reduce_only

    @property
    def is_reduce_only(self):
        """Gets the is_reduce_only of this FuturesOrder.  # noqa: E501

        Is the order post-only  # noqa: E501

        :return: The is_reduce_only of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_reduce_only

    @is_reduce_only.setter
    def is_reduce_only(self, is_reduce_only):
        """Sets the is_reduce_only of this FuturesOrder.

        Is the order post-only  # noqa: E501

        :param is_reduce_only: The is_reduce_only of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_reduce_only = is_reduce_only

    @property
    def is_liq(self):
        """Gets the is_liq of this FuturesOrder.  # noqa: E501

        Is the order for liquidation  # noqa: E501

        :return: The is_liq of this FuturesOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_liq

    @is_liq.setter
    def is_liq(self, is_liq):
        """Sets the is_liq of this FuturesOrder.

        Is the order for liquidation  # noqa: E501

        :param is_liq: The is_liq of this FuturesOrder.  # noqa: E501
        :type: bool
        """

        self._is_liq = is_liq

    @property
    def tif(self):
        """Gets the tif of this FuturesOrder.  # noqa: E501

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, post-only  # noqa: E501

        :return: The tif of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._tif

    @tif.setter
    def tif(self, tif):
        """Sets the tif of this FuturesOrder.

        Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, post-only  # noqa: E501

        :param tif: The tif of this FuturesOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["gtc", "ioc", "poc"]  # noqa: E501
        if tif not in allowed_values:
            raise ValueError(
                "Invalid value for `tif` ({0}), must be one of {1}"  # noqa: E501
                .format(tif, allowed_values)
            )

        self._tif = tif

    @property
    def left(self):
        """Gets the left of this FuturesOrder.  # noqa: E501

        Size left to be traded  # noqa: E501

        :return: The left of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this FuturesOrder.

        Size left to be traded  # noqa: E501

        :param left: The left of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._left = left

    @property
    def fill_price(self):
        """Gets the fill_price of this FuturesOrder.  # noqa: E501

        Fill price of the order  # noqa: E501

        :return: The fill_price of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._fill_price

    @fill_price.setter
    def fill_price(self, fill_price):
        """Sets the fill_price of this FuturesOrder.

        Fill price of the order  # noqa: E501

        :param fill_price: The fill_price of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._fill_price = fill_price

    @property
    def text(self):
        """Gets the text of this FuturesOrder.  # noqa: E501

        How order is created  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance   # noqa: E501

        :return: The text of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FuturesOrder.

        How order is created  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance   # noqa: E501

        :param text: The text of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def tkfr(self):
        """Gets the tkfr of this FuturesOrder.  # noqa: E501

        Taker fee  # noqa: E501

        :return: The tkfr of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._tkfr

    @tkfr.setter
    def tkfr(self, tkfr):
        """Sets the tkfr of this FuturesOrder.

        Taker fee  # noqa: E501

        :param tkfr: The tkfr of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._tkfr = tkfr

    @property
    def mkfr(self):
        """Gets the mkfr of this FuturesOrder.  # noqa: E501

        Maker fee  # noqa: E501

        :return: The mkfr of this FuturesOrder.  # noqa: E501
        :rtype: str
        """
        return self._mkfr

    @mkfr.setter
    def mkfr(self, mkfr):
        """Sets the mkfr of this FuturesOrder.

        Maker fee  # noqa: E501

        :param mkfr: The mkfr of this FuturesOrder.  # noqa: E501
        :type: str
        """

        self._mkfr = mkfr

    @property
    def refu(self):
        """Gets the refu of this FuturesOrder.  # noqa: E501

        Reference user ID  # noqa: E501

        :return: The refu of this FuturesOrder.  # noqa: E501
        :rtype: int
        """
        return self._refu

    @refu.setter
    def refu(self, refu):
        """Sets the refu of this FuturesOrder.

        Reference user ID  # noqa: E501

        :param refu: The refu of this FuturesOrder.  # noqa: E501
        :type: int
        """

        self._refu = refu

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FuturesOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
