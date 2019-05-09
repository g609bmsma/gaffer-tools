#
# Copyright 2016-2019 Crown Copyright
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

from gafferpy_core import gaffer_utils as u
from pyspark.context import SparkContext
from gafferpy_core import gaffer_session as Session

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class GafferPysparkSession(metaclass=Singleton):
    """

    """

    # #general things
    _java_gaffer_session = None
    _java_gateway = None
    _java_server_process = None

    _user = None

    #pyspark things
    _spark_context = None


    def __init__(self):
        self._spark_context = SparkContext.getOrCreate()

    def create_session(self):

        """
        A public method for creating a python gaffer session.
        """

        global gaffer_session
        self.__start_session()
        gaffer_session = self

    def connect_to_session(self, address="172.0.0.1", port="25333"):
        self._java_gaffer_session = Session.GafferPythonSession().connect_to_session(address, port)
        if self._java_gaffer_session.getStatusCode() == 1:
            logger.info("In a pyspark environment. Using SparkSession as the Gaffer Session")
        else:
            msg = "failed to create gaffer session from a pyspark context"
            logger.error(msg)
            raise ValueError(msg)

    def __start_session(self):

        """
        A private method used for instantiating a java Gaffer session
        """

        self._java_gaffer_session = self._spark_context._jvm.uk.gov.gchq.gaffer.python.controllers.SessionManager.getInstance().sessionFactory()
        self._java_gaffer_session.run()
        if self._java_gaffer_session.getStatusCode() == 1:
            logger.info("In a pyspark environment. Using SparkSession as the Gaffer Session")
        else:
            msg = "failed to create gaffer session from a pyspark context"
            logger.error(msg)
            raise ValueError(msg)

    def getSparkContext(self):
        return self._spark_context

    def getGafferSession(self):
        return self._java_gaffer_session