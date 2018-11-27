# -*- coding: utf-8 -*-
"""Test the tcex.utils package."""

import datetime
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import utility


def test_date_to_datetime():
    starting_date = datetime.datetime.now()
    tcex_instance = utility.init_tcex(clean_data=False)
    new_date = tcex_instance.utils.date_to_datetime(str(starting_date))
    assert new_date.year == starting_date.year
    assert new_date.month == starting_date.month
    assert new_date.day == starting_date.day
    assert new_date.hour == starting_date.hour

    # try the same thing again with a different timezone
    tcex_instance = utility.init_tcex(clean_data=False)
    new_date = tcex_instance.utils.date_to_datetime(str(datetime.datetime.now()), tz='UTC')
    # make sure the hour is different b/c of the different timezone
    assert new_date.hour != starting_date.hour


def test_date_to_datetime_with_bad_timezone():
    starting_date = datetime.datetime.now()
    tcex_instance = utility.init_tcex(clean_data=False)
    new_date = tcex_instance.utils.date_to_datetime(str(datetime.datetime.now()), tz='local')
    assert new_date.hour == starting_date.hour
