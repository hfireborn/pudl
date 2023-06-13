"""Extract FERC Form 2 data from SQLite DBs derived from original DBF files.

The Form No. 2 is a compilation of financial and operational information from major
interstate natural gas pipelines subject to the jurisdiction of the FERC. The form
contains data for a calendar year. Among other things, the form contains a Comparative
Balance Sheet, Statement of Income, Statement of Retained Earnings, Statement of Cash
Flows, and Notes to Financial Statements.

Major is defined as having combined gas transported or stored for a fee that exceeds 50
million dekatherms.
"""

from typing import Any, Self

import pandas as pd
import sqlalchemy as sa

import pudl
from pudl.extract.dbf import AbstractFercDbfReader, FercDbfExtractor, FercDbfReader
from pudl.extract.ferc import add_key_constraints
from pudl.settings import FercToSqliteSettings, GenericDatasetSettings
from pudl.workspace.datastore import Datastore

logger = pudl.logging_helpers.get_logger(__name__)


class Ferc2DbfExtractor(FercDbfExtractor):
    """Wrapper for running the foxpro to sqlite conversion of FERC1 dataset."""

    DATASET = "ferc2"
    DATABASE_NAME = "ferc2.sqlite"

    def get_settings(
        self: Self, global_settings: FercToSqliteSettings
    ) -> GenericDatasetSettings:
        """Returns settings for FERC Form 1 DBF dataset."""
        return global_settings.ferc2_dbf_to_sqlite_settings

    def finalize_schema(self: Self, meta: sa.MetaData) -> sa.MetaData:
        """Add primary and foreign keys for respondent_id."""
        return add_key_constraints(
            meta, pk_table="f2_s0_respondent_id", column="respondent_id"
        )

    def transform_table(
        self: Self, table_name: str, in_df: pd.DataFrame
    ) -> pd.DataFrame:
        """FERC Form 2 specific table transformations.

        Remove duplicate IDs from the table enumerating all respondents, retaining the
        most recently reported version of the record. Assumes that records have been
        added to the DB in chronological order.
        """
        if table_name == "f2_s0_respondent_id":
            return (
                in_df.sort_values(by=["report_yr", "respondent_id"])
                .drop_duplicates(subset="respondent_id", keep="last")
                .drop(columns="report_yr")
            )
        else:
            return in_df

    @staticmethod
    def is_valid_partition(fl: dict[str, Any]):
        """Returns False if part key has value other than None.

        This eliminates partitions with part=1 or part=2.
        """
        return fl.get("part", None) is None

    def get_dbf_reader(self: Self, datastore: Datastore) -> AbstractFercDbfReader:
        """Returns appropriate instance of AbstractFercDbfReader to access the data."""
        return Ferc2DbfReader(datastore, dataset=self.DATASET)


class Ferc2DbfReader(FercDbfReader):
    """A FercDbfReader specific to the FERC Form 2."""

    def transform_table_part(
        self: Self, table_part: pd.DataFrame, table_name: str, partition: dict[str, Any]
    ) -> pd.DataFrame:
        """Add report_yr to respondent_id table so we can deduplicate later."""
        table_part = super().transform_table_part(table_part, table_name, partition)
        if table_name == "f2_s0_respondent_id":
            table_part["report_yr"] = partition["year"]
        return table_part
