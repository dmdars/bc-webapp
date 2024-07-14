# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import numpy as np
from streamlit import session_state as state
import access_page
import main

LOGGER = get_logger(__name__)


def run():
    if 'page' not in state:
        state.page = 'main'

    if 'access_notif_clicked' not in state:
        state.access_notif_clicked = False
    if state.page == 'main':
        main.main()
    elif state.page == 'access_page':
        access_page.access_page()


if __name__ == "__main__":
    run()