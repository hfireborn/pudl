"""Add EIA860 storage and coding tables

Revision ID: c0841f4c5e4f
Revises: 49387e87e70a
Create Date: 2024-04-02 16:37:44.763562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0841f4c5e4f'
down_revision = '49387e87e70a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('core_eia__codes_storage_enclosure_types',
    sa.Column('code', sa.Text(), nullable=False, comment='Originally reported short code.'),
    sa.Column('label', sa.Text(), nullable=True, comment='Longer human-readable code using snake_case'),
    sa.Column('description', sa.Text(), nullable=True, comment='Long human-readable description of the meaning of a code/label.'),
    sa.PrimaryKeyConstraint('code', name=op.f('pk_core_eia__codes_storage_enclosure_types'))
    )
    op.create_table('core_eia__codes_storage_technology_types',
    sa.Column('code', sa.Text(), nullable=False, comment='Originally reported short code.'),
    sa.Column('label', sa.Text(), nullable=True, comment='Longer human-readable code using snake_case'),
    sa.Column('description', sa.Text(), nullable=True, comment='Long human-readable description of the meaning of a code/label.'),
    sa.PrimaryKeyConstraint('code', name=op.f('pk_core_eia__codes_storage_technology_types'))
    )
    op.create_table('core_eia860__scd_generators_energy_storage',
    sa.Column('plant_id_eia', sa.Integer(), nullable=False, comment='The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.'),
    sa.Column('generator_id', sa.Text(), nullable=False, comment='Generator ID is usually numeric, but sometimes includes letters. Make sure you treat it as a string!'),
    sa.Column('report_date', sa.Date(), nullable=False, comment='Date reported.'),
    sa.Column('max_charge_rate_mw', sa.Float(), nullable=True, comment='Maximum charge rate in MW.'),
    sa.Column('max_discharge_rate_mw', sa.Float(), nullable=True, comment='Maximum discharge rate in MW.'),
    sa.Column('storage_enclosure_code', sa.Enum('BL', 'CS', 'OT', 'CT'), nullable=True, comment='A code representing the enclosure type that best describes where the generator is located.'),
    sa.Column('storage_technology_code_1', sa.Enum('OTH', 'ECC', 'MAB', 'LIB', 'PBB', 'NAB', 'FLB', 'NIB'), nullable=True, comment='The electro-chemical storage technology used for this battery applications.'),
    sa.Column('storage_technology_code_2', sa.Enum('OTH', 'ECC', 'MAB', 'LIB', 'PBB', 'NAB', 'FLB', 'NIB'), nullable=True, comment='The electro-chemical storage technology used for this battery applications.'),
    sa.Column('storage_technology_code_3', sa.Enum('OTH', 'ECC', 'MAB', 'LIB', 'PBB', 'NAB', 'FLB', 'NIB'), nullable=True, comment='The electro-chemical storage technology used for this battery applications.'),
    sa.Column('storage_technology_code_4', sa.Enum('OTH', 'ECC', 'MAB', 'LIB', 'PBB', 'NAB', 'FLB', 'NIB'), nullable=True, comment='The electro-chemical storage technology used for this battery applications.'),
    sa.Column('served_arbitrage', sa.Boolean(), nullable=True, comment='Whether the energy storage device served arbitrage applications during the reporting year'),
    sa.Column('served_backup_power', sa.Boolean(), nullable=True, comment='Whether the energy storage device served backup power applications during the reporting year.'),
    sa.Column('served_co_located_renewable_firming', sa.Boolean(), nullable=True, comment='Whether the energy storage device served renewable firming applications during the reporting year.'),
    sa.Column('served_frequency_regulation', sa.Boolean(), nullable=True, comment='Whether the energy storage device served frequency regulation applications during the reporting year.'),
    sa.Column('served_load_following', sa.Boolean(), nullable=True, comment='Whether the energy storage device served load following applications during the reporting year.'),
    sa.Column('served_load_management', sa.Boolean(), nullable=True, comment='Whether the energy storage device served load management applications during the reporting year.'),
    sa.Column('served_ramping_spinning_reserve', sa.Boolean(), nullable=True, comment='Whether the this energy storage device served ramping / spinning reserve applications during the reporting year.'),
    sa.Column('served_system_peak_shaving', sa.Boolean(), nullable=True, comment='Whether the energy storage device served system peak shaving applications during the reporting year.'),
    sa.Column('served_transmission_and_distribution_deferral', sa.Boolean(), nullable=True, comment='Whether the energy storage device served renewable firming applications during the reporting year.'),
    sa.Column('served_voltage_or_reactive_power_support', sa.Boolean(), nullable=True, comment='Whether the energy storage device served voltage or reactive power support applications during the reporting year.'),
    sa.Column('stored_excess_wind_and_solar_generation', sa.Boolean(), nullable=True, comment='Whether the energy storage device was used to store excess wind/solar generation during the reporting year.'),
    sa.ForeignKeyConstraint(['plant_id_eia', 'generator_id', 'report_date'], ['core_eia860__scd_generators.plant_id_eia', 'core_eia860__scd_generators.generator_id', 'core_eia860__scd_generators.report_date'], name=op.f('fk_core_eia860__scd_generators_energy_storage_plant_id_eia_core_eia860__scd_generators')),
    sa.PrimaryKeyConstraint('plant_id_eia', 'generator_id', 'report_date', name=op.f('pk_core_eia860__scd_generators_energy_storage'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('core_eia860__scd_generators_energy_storage')
    op.drop_table('core_eia__codes_storage_technology_types')
    op.drop_table('core_eia__codes_storage_enclosure_types')
    # ### end Alembic commands ###
