"""Add my cool ferc1_eia table

Revision ID: f11241c9292d
Revises: 7fa2763bd630
Create Date: 2023-10-16 11:02:01.595978

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f11241c9292d"
down_revision = "7fa2763bd630"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "out__yearly_plants_all_ferc1_plant_parts_eia",
        sa.Column(
            "record_id_ferc1",
            sa.Text(),
            nullable=False,
            comment="Identifier indicating original FERC Form 1 source record. format: {table_name}_{report_year}_{report_prd}_{respondent_id}_{spplmnt_num}_{row_number}. Unique within FERC Form 1 DB tables which are not row-mapped.",
        ),
        sa.Column(
            "record_id_eia",
            sa.Text(),
            nullable=True,
            comment="Identifier for EIA plant parts analysis records.",
        ),
        sa.Column(
            "match_type",
            sa.Text(),
            nullable=True,
            comment="Indicates the source and validation of the match between EIA and FERC. Match types include matches was generated from the model, verified by the training data, overridden by the training data, etc.",
        ),
        sa.Column(
            "plant_name_ppe",
            sa.Text(),
            nullable=True,
            comment="Derived plant name that includes EIA plant name and other strings associated with ID and PK columns of the plant part.",
        ),
        sa.Column(
            "plant_part",
            sa.Enum(
                "plant_prime_fuel",
                "plant_unit",
                "plant_gen",
                "plant",
                "plant_ferc_acct",
                "plant_operating_year",
                "plant_technology",
                "plant_match_ferc1",
                "plant_prime_mover",
            ),
            nullable=True,
            comment="The part of the plant a record corresponds to.",
        ),
        sa.Column(
            "report_year",
            sa.Integer(),
            nullable=True,
            comment="Four-digit year in which the data was reported.",
        ),
        sa.Column("report_date", sa.Date(), nullable=True, comment="Date reported."),
        sa.Column(
            "ownership_record_type",
            sa.Enum("owned", "total"),
            nullable=True,
            comment="Whether each generator record is for one owner or represents a total of all ownerships.",
        ),
        sa.Column("plant_name_eia", sa.Text(), nullable=True, comment="Plant name."),
        sa.Column(
            "plant_id_eia",
            sa.Integer(),
            nullable=True,
            comment="The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.",
        ),
        sa.Column(
            "generator_id",
            sa.Text(),
            nullable=True,
            comment="Generator ID is usually numeric, but sometimes includes letters. Make sure you treat it as a string!",
        ),
        sa.Column(
            "unit_id_pudl",
            sa.Integer(),
            nullable=True,
            comment="Dynamically assigned PUDL unit id. WARNING: This ID is not guaranteed to be static long term as the input data and algorithm may evolve over time.",
        ),
        sa.Column(
            "prime_mover_code",
            sa.Text(),
            nullable=True,
            comment="Code for the type of prime mover (e.g. CT, CG)",
        ),
        sa.Column(
            "energy_source_code_1",
            sa.Text(),
            nullable=True,
            comment="The code representing the most predominant type of energy that fuels the generator.",
        ),
        sa.Column(
            "technology_description",
            sa.Text(),
            nullable=True,
            comment="High level description of the technology used by the generator to produce electricity.",
        ),
        sa.Column(
            "ferc_acct_name",
            sa.Enum("Hydraulic", "Nuclear", "Steam", "Other"),
            nullable=True,
            comment="Name of FERC account, derived from technology description and prime mover code.",
        ),
        sa.Column(
            "generator_operating_year",
            sa.Integer(),
            nullable=True,
            comment="Year a generator went into service.",
        ),
        sa.Column(
            "utility_id_eia",
            sa.Integer(),
            nullable=True,
            comment="The EIA Utility Identification number.",
        ),
        sa.Column(
            "utility_id_pudl",
            sa.Integer(),
            nullable=True,
            comment="A manually assigned PUDL utility ID. May not be stable over time.",
        ),
        sa.Column(
            "true_gran",
            sa.Boolean(),
            nullable=True,
            comment="Indicates whether a plant part list record is associated with the highest priority plant part for all identical records.",
        ),
        sa.Column(
            "appro_part_label",
            sa.Enum(
                "plant_prime_fuel",
                "plant_unit",
                "plant_gen",
                "plant",
                "plant_ferc_acct",
                "plant_operating_year",
                "plant_technology",
                "plant_match_ferc1",
                "plant_prime_mover",
            ),
            nullable=True,
            comment="Plant part of the associated true granularity record.",
        ),
        sa.Column(
            "appro_record_id_eia",
            sa.Text(),
            nullable=True,
            comment="EIA record ID of the associated true granularity record.",
        ),
        sa.Column(
            "record_count",
            sa.Integer(),
            nullable=True,
            comment="Number of distinct generator IDs that partcipated in the aggregation for a plant part list record.",
        ),
        sa.Column(
            "fraction_owned",
            sa.Float(),
            nullable=True,
            comment="Proportion of generator ownership attributable to this utility.",
        ),
        sa.Column(
            "ownership_dupe",
            sa.Boolean(),
            nullable=True,
            comment="Whether a plant part record has a duplicate record with different ownership status.",
        ),
        sa.Column(
            "operational_status",
            sa.Text(),
            nullable=True,
            comment="The operating status of the asset. For generators this is based on which tab the generator was listed in in EIA 860.",
        ),
        sa.Column(
            "operational_status_pudl",
            sa.Enum("operating", "retired", "proposed"),
            nullable=True,
            comment="The operating status of the asset using PUDL categories.",
        ),
        sa.Column(
            "plant_id_pudl",
            sa.Integer(),
            nullable=True,
            comment="A manually assigned PUDL plant ID. May not be constant over time.",
        ),
        sa.Column(
            "total_fuel_cost_eia",
            sa.Float(),
            nullable=True,
            comment="Total annual reported fuel costs for the plant part. Includes costs from all fuels.",
        ),
        sa.Column(
            "fuel_cost_per_mmbtu_eia",
            sa.Float(),
            nullable=True,
            comment="Average fuel cost per mmBTU of heat content in nominal USD.",
        ),
        sa.Column(
            "net_generation_mwh_eia",
            sa.Float(),
            nullable=True,
            comment="Net electricity generation for the specified period in megawatt-hours (MWh).",
        ),
        sa.Column(
            "capacity_mw_eia",
            sa.Float(),
            nullable=True,
            comment="Total installed (nameplate) capacity, in megawatts.",
        ),
        sa.Column(
            "capacity_factor_eia",
            sa.Float(),
            nullable=True,
            comment="Fraction of potential generation that was actually reported for a plant part.",
        ),
        sa.Column(
            "total_mmbtu_eia",
            sa.Float(),
            nullable=True,
            comment="Total annual heat content of fuel consumed by a plant part record in the plant parts list.",
        ),
        sa.Column(
            "heat_rate_mmbtu_mwh_eia",
            sa.Float(),
            nullable=True,
            comment="Fuel content per unit of electricity generated. Coming from MCOE calculation.",
        ),
        sa.Column(
            "fuel_type_code_pudl_eia",
            sa.Enum(
                "coal",
                "gas",
                "hydro",
                "nuclear",
                "oil",
                "other",
                "solar",
                "waste",
                "wind",
            ),
            nullable=True,
            comment="Simplified fuel type code used in PUDL",
        ),
        sa.Column(
            "installation_year_eia",
            sa.Integer(),
            nullable=True,
            comment="Year the plant's most recently built unit was installed.",
        ),
        sa.Column(
            "plant_part_id_eia",
            sa.Text(),
            nullable=True,
            comment="Contains EIA plant ID, plant part, ownership, and EIA utility id",
        ),
        sa.Column(
            "utility_id_ferc1",
            sa.Integer(),
            nullable=True,
            comment="PUDL-assigned utility ID, identifying a FERC1 utility. This is an auto-incremented ID and is not expected to be stable from year to year.",
        ),
        sa.Column(
            "utility_name_ferc1",
            sa.Text(),
            nullable=True,
            comment="Name of the responding utility, as it is reported in FERC Form 1. For human readability only.",
        ),
        sa.Column(
            "plant_id_ferc1",
            sa.Integer(),
            nullable=True,
            comment="Algorithmically assigned PUDL FERC Plant ID. WARNING: NOT STABLE BETWEEN PUDL DB INITIALIZATIONS.",
        ),
        sa.Column(
            "plant_name_ferc1",
            sa.Text(),
            nullable=True,
            comment="Name of the plant, as reported to FERC. This is a freeform string, not guaranteed to be consistent across references to the same plant.",
        ),
        sa.Column(
            "asset_retirement_cost",
            sa.Float(),
            nullable=True,
            comment="Asset retirement cost (USD).",
        ),
        sa.Column("avg_num_employees", sa.Float(), nullable=True),
        sa.Column(
            "capacity_factor_ferc1",
            sa.Float(),
            nullable=True,
            comment="Fraction of potential generation that was actually reported for a plant part.",
        ),
        sa.Column(
            "capacity_mw_ferc1",
            sa.Float(),
            nullable=True,
            comment="Total installed (nameplate) capacity, in megawatts.",
        ),
        sa.Column(
            "capex_annual_addition",
            sa.Float(),
            nullable=True,
            comment="Annual capital addition into `capex_total`.",
        ),
        sa.Column(
            "capex_annual_addition_rolling",
            sa.Float(),
            nullable=True,
            comment="Year-to-date capital addition into `capex_total`.",
        ),
        sa.Column(
            "capex_annual_per_kw",
            sa.Float(),
            nullable=True,
            comment="Annual capital addition into `capex_total` per kw.",
        ),
        sa.Column(
            "capex_annual_per_mw",
            sa.Float(),
            nullable=True,
            comment="Annual capital addition into `capex_total` per MW.",
        ),
        sa.Column(
            "capex_annual_per_mw_rolling",
            sa.Float(),
            nullable=True,
            comment="Year-to-date capital addition into `capex_total` per MW.",
        ),
        sa.Column(
            "capex_annual_per_mwh",
            sa.Float(),
            nullable=True,
            comment="Annual capital addition into `capex_total` per MWh.",
        ),
        sa.Column(
            "capex_annual_per_mwh_rolling",
            sa.Float(),
            nullable=True,
            comment="Year-to-date capital addition into `capex_total` per MWh.",
        ),
        sa.Column(
            "capex_equipment",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: equipment (USD).",
        ),
        sa.Column(
            "capex_land",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: land and land rights (USD).",
        ),
        sa.Column(
            "capex_per_mw",
            sa.Float(),
            nullable=True,
            comment="Cost of plant per megawatt of installed (nameplate) capacity. Nominal USD.",
        ),
        sa.Column(
            "capex_structures",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: structures and improvements (USD).",
        ),
        sa.Column(
            "capex_total",
            sa.Float(),
            nullable=True,
            comment="Total cost of plant (USD).",
        ),
        sa.Column(
            "capex_wo_retirement_total",
            sa.Float(),
            nullable=True,
            comment="Total cost of plant (USD) without retirements.",
        ),
        sa.Column(
            "construction_type",
            sa.Enum("conventional", "outdoor", "semioutdoor"),
            nullable=True,
            comment="Type of plant construction ('outdoor', 'semioutdoor', or 'conventional'). Categorized by PUDL based on our best guess of intended value in FERC1 freeform strings.",
        ),
        sa.Column(
            "construction_year_eia",
            sa.Integer(),
            nullable=True,
            comment="Year the plant's oldest still operational unit was built.",
        ),
        sa.Column(
            "construction_year_ferc1",
            sa.Integer(),
            nullable=True,
            comment="Year the plant's oldest still operational unit was built.",
        ),
        sa.Column(
            "installation_year_ferc1",
            sa.Integer(),
            nullable=True,
            comment="Year the plant's most recently built unit was installed.",
        ),
        sa.Column(
            "net_generation_mwh_ferc1",
            sa.Float(),
            nullable=True,
            comment="Net electricity generation for the specified period in megawatt-hours (MWh).",
        ),
        sa.Column(
            "not_water_limited_capacity_mw",
            sa.Float(),
            nullable=True,
            comment="Plant capacity in MW when not limited by condenser water.",
        ),
        sa.Column("opex_allowances", sa.Float(), nullable=True, comment="Allowances."),
        sa.Column(
            "opex_boiler",
            sa.Float(),
            nullable=True,
            comment="Maintenance of boiler (or reactor) plant.",
        ),
        sa.Column(
            "opex_coolants",
            sa.Float(),
            nullable=True,
            comment="Cost of coolants and water (nuclear plants only)",
        ),
        sa.Column(
            "opex_electric",
            sa.Float(),
            nullable=True,
            comment="Production expenses: electric expenses (USD).",
        ),
        sa.Column(
            "opex_engineering",
            sa.Float(),
            nullable=True,
            comment="Production expenses: maintenance, supervision, and engineering (USD).",
        ),
        sa.Column(
            "opex_fuel",
            sa.Float(),
            nullable=True,
            comment="Production expenses: fuel (USD).",
        ),
        sa.Column(
            "fuel_cost_per_mwh_eia",
            sa.Float(),
            nullable=True,
            comment="Derived from MCOE, a unit level value. Average fuel cost per MWh of heat content in nominal USD.",
        ),
        sa.Column(
            "fuel_cost_per_mwh_ferc1",
            sa.Float(),
            nullable=True,
            comment="Derived from MCOE, a unit level value. Average fuel cost per MWh of heat content in nominal USD.",
        ),
        sa.Column(
            "opex_misc_power",
            sa.Float(),
            nullable=True,
            comment="Miscellaneous steam (or nuclear) expenses.",
        ),
        sa.Column(
            "opex_misc_steam",
            sa.Float(),
            nullable=True,
            comment="Maintenance of miscellaneous steam (or nuclear) plant.",
        ),
        sa.Column(
            "opex_nonfuel_per_mwh",
            sa.Float(),
            nullable=True,
            comment="Investments in non-fuel production expenses per Mwh.",
        ),
        sa.Column(
            "opex_operations",
            sa.Float(),
            nullable=True,
            comment="Production expenses: operations, supervision, and engineering (USD).",
        ),
        sa.Column(
            "opex_per_mwh",
            sa.Float(),
            nullable=True,
            comment="Total production expenses (USD per MWh generated).",
        ),
        sa.Column(
            "opex_plant",
            sa.Float(),
            nullable=True,
            comment="Production expenses: maintenance of electric plant (USD).",
        ),
        sa.Column(
            "opex_production_total",
            sa.Float(),
            nullable=True,
            comment="Total operating expenses.",
        ),
        sa.Column(
            "opex_rents",
            sa.Float(),
            nullable=True,
            comment="Production expenses: rents (USD).",
        ),
        sa.Column("opex_steam", sa.Float(), nullable=True, comment="Steam expenses."),
        sa.Column(
            "opex_steam_other",
            sa.Float(),
            nullable=True,
            comment="Steam from other sources.",
        ),
        sa.Column(
            "opex_structures",
            sa.Float(),
            nullable=True,
            comment="Production expenses: maintenance of structures (USD).",
        ),
        sa.Column(
            "opex_total_nonfuel",
            sa.Float(),
            nullable=True,
            comment="Total production expenses, excluding fuel (USD).",
        ),
        sa.Column(
            "opex_transfer",
            sa.Float(),
            nullable=True,
            comment="Steam transferred (Credit).",
        ),
        sa.Column(
            "peak_demand_mw",
            sa.Float(),
            nullable=True,
            comment="Net peak demand for 60 minutes. Note: in some cases peak demand for other time periods may have been reported instead, if hourly peak demand was unavailable.",
        ),
        sa.Column(
            "plant_capability_mw",
            sa.Float(),
            nullable=True,
            comment="Net plant capability in megawatts.",
        ),
        sa.Column(
            "plant_hours_connected_while_generating",
            sa.Float(),
            nullable=True,
            comment="Hours the plant was connected to load while generating in the report year.",
        ),
        sa.Column("plant_type", sa.Text(), nullable=True),
        sa.Column(
            "water_limited_capacity_mw",
            sa.Float(),
            nullable=True,
            comment="Plant capacity in MW when limited by condenser water.",
        ),
        sa.Column(
            "fuel_cost_per_mmbtu_ferc1",
            sa.Float(),
            nullable=True,
            comment="Average fuel cost per mmBTU of heat content in nominal USD.",
        ),
        sa.Column("fuel_type", sa.Text(), nullable=True),
        sa.Column(
            "license_id_ferc1",
            sa.Integer(),
            nullable=True,
            comment="FERC issued operating license ID for the facility, if available. This value is extracted from the original plant name where possible.",
        ),
        sa.Column(
            "opex_maintenance",
            sa.Float(),
            nullable=True,
            comment="Production expenses: Maintenance (USD).",
        ),
        sa.Column(
            "opex_total",
            sa.Float(),
            nullable=True,
            comment="Total production expenses, excluding fuel (USD).",
        ),
        sa.Column(
            "capex_facilities",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: reservoirs, dams, and waterways (USD).",
        ),
        sa.Column(
            "capex_roads",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: roads, railroads, and bridges (USD).",
        ),
        sa.Column(
            "net_capacity_adverse_conditions_mw",
            sa.Float(),
            nullable=True,
            comment="Net plant capability under the least favorable operating conditions, in megawatts.",
        ),
        sa.Column(
            "net_capacity_favorable_conditions_mw",
            sa.Float(),
            nullable=True,
            comment="Net plant capability under the most favorable operating conditions, in megawatts.",
        ),
        sa.Column(
            "opex_dams",
            sa.Float(),
            nullable=True,
            comment="Production expenses: maintenance of reservoirs, dams, and waterways (USD).",
        ),
        sa.Column(
            "opex_generation_misc",
            sa.Float(),
            nullable=True,
            comment="Production expenses: miscellaneous power generation expenses (USD).",
        ),
        sa.Column(
            "opex_hydraulic",
            sa.Float(),
            nullable=True,
            comment="Production expenses: hydraulic expenses (USD).",
        ),
        sa.Column(
            "opex_misc_plant",
            sa.Float(),
            nullable=True,
            comment="Production expenses: maintenance of miscellaneous hydraulic plant (USD).",
        ),
        sa.Column(
            "opex_water_for_power",
            sa.Float(),
            nullable=True,
            comment="Production expenses: water for power (USD).",
        ),
        sa.Column(
            "ferc_license_id",
            sa.Text(),
            nullable=True,
            comment="The FERC license ID of a project.",
        ),
        sa.Column(
            "capex_equipment_electric",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: accessory electric equipment (USD).",
        ),
        sa.Column(
            "capex_equipment_misc",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: miscellaneous power plant equipment (USD).",
        ),
        sa.Column(
            "capex_wheels_turbines_generators",
            sa.Float(),
            nullable=True,
            comment="Cost of plant: water wheels, turbines, and generators (USD).",
        ),
        sa.Column(
            "energy_used_for_pumping_mwh",
            sa.Float(),
            nullable=True,
            comment="Energy used for pumping, in megawatt-hours.",
        ),
        sa.Column(
            "net_load_mwh",
            sa.Float(),
            nullable=True,
            comment="Net output for load (net generation - energy used for pumping) in megawatt-hours.",
        ),
        sa.Column(
            "opex_production_before_pumping",
            sa.Float(),
            nullable=True,
            comment="Total production expenses before pumping (USD).",
        ),
        sa.Column(
            "opex_pumped_storage",
            sa.Float(),
            nullable=True,
            comment="Production expenses: pumped storage (USD).",
        ),
        sa.Column(
            "opex_pumping",
            sa.Float(),
            nullable=True,
            comment="Production expenses: We are here to PUMP YOU UP! (USD).",
        ),
        sa.Column(
            "total_fuel_cost_ferc1",
            sa.Float(),
            nullable=True,
            comment="Total annual reported fuel costs for the plant part. Includes costs from all fuels.",
        ),
        sa.Column(
            "total_mmbtu_ferc1",
            sa.Float(),
            nullable=True,
            comment="Total annual heat content of fuel consumed by a plant part record in the plant parts list.",
        ),
        sa.Column(
            "fuel_type_code_pudl_ferc1",
            sa.Enum(
                "coal",
                "gas",
                "hydro",
                "nuclear",
                "oil",
                "other",
                "solar",
                "waste",
                "wind",
            ),
            nullable=True,
            comment="Simplified fuel type code used in PUDL",
        ),
        sa.Column(
            "heat_rate_mmbtu_mwh_ferc1",
            sa.Float(),
            nullable=True,
            comment="Fuel content per unit of electricity generated. Calculated from FERC reported fuel consumption and net generation.",
        ),
        sa.ForeignKeyConstraint(
            ["energy_source_code_1"],
            ["energy_sources_eia.code"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_energy_source_code_1_energy_sources_eia"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_eia", "generator_id", "report_date"],
            [
                "generators_eia860.plant_id_eia",
                "generators_eia860.generator_id",
                "generators_eia860.report_date",
            ],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_plant_id_eia_generators_eia860"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["plant_id_pudl"],
            ["plants_pudl.plant_id_pudl"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_plant_id_pudl_plants_pudl"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["prime_mover_code"],
            ["prime_movers_eia.code"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_prime_mover_code_prime_movers_eia"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["utility_id_eia", "report_date"],
            ["utilities_eia860.utility_id_eia", "utilities_eia860.report_date"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_utility_id_eia_utilities_eia860"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["utility_id_ferc1", "plant_name_ferc1"],
            ["plants_ferc1.utility_id_ferc1", "plants_ferc1.plant_name_ferc1"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_utility_id_ferc1_plants_ferc1"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["utility_id_pudl"],
            ["utilities_pudl.utility_id_pudl"],
            name=op.f(
                "fk_out__yearly_plants_all_ferc1_plant_parts_eia_utility_id_pudl_utilities_pudl"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "record_id_ferc1",
            name=op.f("pk_out__yearly_plants_all_ferc1_plant_parts_eia"),
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("out__yearly_plants_all_ferc1_plant_parts_eia")
    # ### end Alembic commands ###