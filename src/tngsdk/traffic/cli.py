# Copyright (c) 2018 5GTANGO, QUOBIS SL.
# ALL RIGHTS RESERVED.
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
# Neither the name of the 5GTANGO, QUOBIS SL.
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).

import logging
import argparse
import os
import sys


def dispatch():
    # TODO call traffic.py to do selected command
    return

def parse_args(input_args=None):
    parser = argparse.ArgumentParser(
        description="5GTANGO SDK traffic generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example usage:
        tng-sdk-traffic --service
        """)

    parser.add_argument(
        "--generate-flow",
        "-g",
        help="Generate a traffic flow",
        dest="generate-flow",
        action="store_true",
        required=False,
        default=False
    )
    parser.add_argument(
        "--list-flows",
        "-l",
        help="Retrieve a list with traffic flows, their status and configurations",
        dest="list-flows",
        action="store_true",
        required=False,
        default=False
    )

    parser.add_argument(
        "--service",
        help="Run traffic generator in service mode with REST API.",
        dest="service",
        action="store_true",
        required=False,
        default=False
    )
    parser.add_argument(
        "--verbose",
        help="Sets verbosity level to debug",
        dest="verbose",
        action="store_true",
        required=False,
        default=False
    )

    if input_args is None:
        input_args = sys.argv[1:]

    return parser.parse_args(input_args)