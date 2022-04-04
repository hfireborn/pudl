"""Tests for merging datasets at different temporal frequencies."""
import pandas as pd

import pudl.helpers

MONTHLY_GEN_FUEL = pd.DataFrame(
    {
        "report_date": [
            "2019-12-01",
            "2020-10-01",
            "2019-01-01",
            "2019-06-01",
            "2018-07-01",
        ],
        "plant_id_eia": [2, 2, 3, 3, 3],
        "prime_mover_code": ["HY", "ST", "HY", "CT", "HY"],
        "fuel_consumed_units": [0.0, 98085.0, 0.0, 4800000.0, 0.0],
    }
).astype({"report_date": "datetime64[ns]"})

ANNUAL_PLANTS_UTIL = pd.DataFrame(
    {
        "report_date": [
            "2020-01-01",
            "2020-01-01",
            "2019-01-01",
            "2018-01-01",
            "2020-01-01",
            "2019-01-01",
            "2018-01-01",
        ],
        "plant_id_eia": [1, 2, 2, 2, 3, 3, 3],
        "plant_name_eia": [
            "Sand Point",
            "Bankhead",
            "Bankhead Dam",
            "Bankhead Dam",
            "Barry",
            "Barry",
            "Barry",
        ],
        "utility_id_eia": [63560, 195, 195, 195, 16, 16, 16],
    }
).astype({"report_date": "datetime64[ns]"})

MONTHLY_OTHER = pd.DataFrame(
    {
        "report_date": ["2019-10-01", "2020-10-01", "2019-01-01", "2018-02-01"],
        "plant_id_eia": [2, 2, 3, 3],
        "energy_source_code": ["DFO", "WND", "WND", "DFO"],
    }
).astype({"report_date": "datetime64[ns]"})

DAILY_DATA = pd.DataFrame(
    {
        "date": ["2019-10-12", "2019-10-13", "2019-12-01", "2018-02-03"],
        "plant_id_eia": [2, 2, 2, 3],
        "daily_data": [1, 2, 3, 4],
    }
).astype({"date": "datetime64[ns]"})


def test_annual_attribute_merge():
    """Test merging annual attributes onto monthly data with a sparse report date.

    The left and right merges in this case is a one to many merge and should
    yield an output table with the exact same data records as the
    input data table.

    The inner merge case loses records. The outer merge case creates extra
    records with NA values.
    """
    out_expected_left = pd.DataFrame(
        {
            "report_date": [
                "2019-12-01",
                "2020-10-01",
                "2019-01-01",
                "2019-06-01",
                "2018-07-01",
            ],
            "plant_id_eia": [2, 2, 3, 3, 3],
            "prime_mover_code": ["HY", "ST", "HY", "CT", "HY"],
            "fuel_consumed_units": [0.0, 98085.0, 0.0, 4800000.0, 0.0],
            "plant_name_eia": ["Bankhead Dam", "Bankhead", "Barry", "Barry", "Barry"],
            "utility_id_eia": [195, 195, 16, 16, 16],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out_left = pudl.helpers.mixed_temporal_gran_merge(
        left=MONTHLY_GEN_FUEL,
        right=ANNUAL_PLANTS_UTIL,
        shared_merge_cols=["plant_id_eia"],
        merge_type="left",
    )

    pd.testing.assert_frame_equal(out_left, out_expected_left)

    out_expected_right = pd.DataFrame(
        {
            "report_date": [
                "2019-12-01",
                "2020-10-01",
                "2019-01-01",
                "2019-06-01",
                "2018-07-01",
            ],
            "plant_id_eia": [2, 2, 3, 3, 3],
            "plant_name_eia": ["Bankhead Dam", "Bankhead", "Barry", "Barry", "Barry"],
            "utility_id_eia": [195, 195, 16, 16, 16],
            "prime_mover_code": ["HY", "ST", "HY", "CT", "HY"],
            "fuel_consumed_units": [0.0, 98085.0, 0.0, 4800000.0, 0.0],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out_right = pudl.helpers.mixed_temporal_gran_merge(
        left=ANNUAL_PLANTS_UTIL,
        right=MONTHLY_GEN_FUEL,
        shared_merge_cols=["plant_id_eia"],
        merge_type="right",
    )

    pd.testing.assert_frame_equal(out_right, out_expected_right)

    out_expected_inner = pd.DataFrame(
        {
            "report_date": [
                "2019-12-01",
                "2020-10-01",
                "2019-01-01",
                "2019-06-01",
                "2018-07-01",
            ],
            "plant_id_eia": [2, 2, 3, 3, 3],
            "prime_mover_code": ["HY", "ST", "HY", "CT", "HY"],
            "fuel_consumed_units": [0.0, 98085.0, 0.0, 4800000.0, 0.0],
            "plant_name_eia": ["Bankhead Dam", "Bankhead", "Barry", "Barry", "Barry"],
            "utility_id_eia": [195, 195, 16, 16, 16],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out_inner = pudl.helpers.mixed_temporal_gran_merge(
        left=MONTHLY_GEN_FUEL,
        right=ANNUAL_PLANTS_UTIL,
        shared_merge_cols=["plant_id_eia"],
        merge_type="inner",
    )

    pd.testing.assert_frame_equal(out_inner, out_expected_inner)

    out_expected_outer = pd.DataFrame(
        {
            "report_date": [
                "2019-12-01",
                "2020-10-01",
                "2019-01-01",
                "2019-06-01",
                "2018-07-01",
                "2020-01-01",
                "2018-01-01",
                "2020-01-01",
            ],
            "plant_id_eia": [2, 2, 3, 3, 3, 1, 2, 3],
            "prime_mover_code": ["HY", "ST", "HY", "CT", "HY", None, None, None],
            "fuel_consumed_units": [
                0.0,
                98085.0,
                0.0,
                4800000.0,
                0.0,
                None,
                None,
                None,
            ],
            "plant_name_eia": [
                "Bankhead Dam",
                "Bankhead",
                "Barry",
                "Barry",
                "Barry",
                "Sand Point",
                "Bankhead Dam",
                "Barry",
            ],
            "utility_id_eia": [195, 195, 16, 16, 16, 63560, 195, 16],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out_outer = pudl.helpers.mixed_temporal_gran_merge(
        left=MONTHLY_GEN_FUEL,
        right=ANNUAL_PLANTS_UTIL,
        shared_merge_cols=["plant_id_eia"],
        merge_type="outer",
    )

    pd.testing.assert_frame_equal(out_outer, out_expected_outer)


def test_monthly_attribute_merge():
    """Test merging monthly attributes onto daily data with a sparse report date."""
    out_expected = pd.DataFrame(
        {
            "report_date": ["2019-10-12", "2019-10-13", "2019-12-01", "2018-02-03"],
            "plant_id_eia": [2, 2, 2, 3],
            "daily_data": [1, 2, 3, 4],
            "energy_source_code": ["DFO", "DFO", None, "DFO"],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out = pudl.helpers.mixed_temporal_gran_merge(
        left=DAILY_DATA,
        right=MONTHLY_OTHER,
        left_date_col="date",
        shared_merge_cols=["plant_id_eia"],
        temporal_merge_cols=["year", "month"],
        merge_type="left",
    )

    pd.testing.assert_frame_equal(out, out_expected)


def test_same_temporal_gran():
    """Test merging tables with the same temporal granularity.

    In this case, this yields the same results as ``pd.merge``.
    """
    out_expected = pd.DataFrame(
        {
            "report_date": [
                "2019-12-01",
                "2020-10-01",
                "2019-01-01",
                "2019-06-01",
                "2018-07-01",
            ],
            "plant_id_eia": [2, 2, 3, 3, 3],
            "prime_mover_code": ["HY", "ST", "HY", "CT", "HY"],
            "fuel_consumed_units": [0.0, 98085.0, 0.0, 4800000.0, 0.0],
            "energy_source_code": [None, "WND", "WND", None, None],
        }
    ).astype({"report_date": "datetime64[ns]"})

    """
    out_expected = MONTHLY_GEN_FUEL.merge(
        MONTHLY_OTHER,
        how="left",
        on=["report_date", "plant_id_eia"],
    )
    """

    out = pudl.helpers.mixed_temporal_gran_merge(
        left=MONTHLY_GEN_FUEL,
        right=MONTHLY_OTHER,
        shared_merge_cols=["plant_id_eia"],
        temporal_merge_cols=["year", "month"],
        merge_type="left",
    ).astype({"report_date": "datetime64[ns]"})
    pd.testing.assert_frame_equal(out, out_expected)


def test_timeseries_fillin():
    """Test filling in tables to a full timeseries."""
    input_df = pd.DataFrame(
        {
            "report_date": [
                "2019-02-01",
                "2020-01-01",
                "2020-02-01",
                "2019-03-01",
                "2019-10-01",
                "2020-02-01",
            ],
            "plant_id_eia": [1, 1, 1, 1, 2, 2],
            "data": [2, 1, 2, 3, 10, 2],
        }
    ).astype({"report_date": "datetime64[ns]"})

    expected_out = pd.DataFrame(
        {
            "report_date": [
                "2019-02-01",
                "2019-03-01",
                "2019-04-01",
                "2019-05-01",
                "2019-06-01",
                "2019-07-01",
                "2019-08-01",
                "2019-09-01",
                "2019-10-01",
                "2019-11-01",
                "2019-12-01",
                "2020-01-01",
                "2020-02-01",
            ]
            * 2,
            "plant_id_eia": [1] * 13 + [2] * 13,
            "data": [2] + [3] * 10 + [1] + [2] + [None] * 8 + [10] * 4 + [2],
        }
    ).astype({"report_date": "datetime64[ns]"})

    out = pudl.helpers.expand_timeseries(input_df, id_cols=["plant_id_eia"])
    pd.testing.assert_frame_equal(expected_out, out)
