"""Add my cool ppe assn table

Revision ID: a47a74d21b3f
Revises: 52aa9f44b6a7
Create Date: 2024-08-21 16:06:00.492205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a47a74d21b3f'
down_revision = '52aa9f44b6a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('out_eia__yearly_assn_plant_parts_plant_gen',
    sa.Column('record_id_eia', sa.Text(), nullable=False, comment='Identifier for EIA plant parts analysis records.'),
    sa.Column('record_id_eia_plant_gen', sa.Text(), nullable=False, comment='Identifier for EIA plant parts analysis records which is at the plant_part level of plant_gen - meaning each record pertains to one generator.'),
    sa.Column('report_date', sa.Date(), nullable=True, comment='Date reported.'),
    sa.Column('plant_id_eia', sa.Integer(), nullable=True, comment='The unique six-digit facility identification number, also called an ORISPL, assigned by the Energy Information Administration.'),
    sa.Column('utility_id_eia', sa.Integer(), nullable=True, comment='The EIA Utility Identification number.'),
    sa.Column('ownership_record_type', sa.Enum('owned', 'total'), nullable=True, comment='Whether each generator record is for one owner or represents a total of all ownerships.'),
    sa.Column('generator_id_plant_gen', sa.Text(), nullable=True, comment='Generator ID of the record_id_eia_plant_gen record. This is usually numeric, but sometimes includes letters. Make sure you treat it as a string!'),
    sa.Column('energy_source_code_1_plant_gen', sa.Text(), nullable=True, comment="Code representing the most predominant type of energy that fuels the record_id_eia_plant_gen's generator."),
    sa.Column('prime_mover_code_plant_gen', sa.Text(), nullable=True, comment='Code for the type of prime mover (e.g. CT, CG) associated with the record_id_eia_plant_gen.'),
    sa.Column('unit_id_pudl_plant_gen', sa.Integer(), nullable=True, comment='Dynamically assigned PUDL unit id of the record_id_eia_plant_gen. WARNING: This ID is not guaranteed to be static long term as the input data and algorithm may evolve over time.'),
    sa.Column('technology_description_plant_gen', sa.Text(), nullable=True, comment="High level description of the technology used by the record_id_eia_plant_gen's generator to produce electricity."),
    sa.Column('ferc_acct_name_plant_gen', sa.Enum('Hydraulic', 'Nuclear', 'Steam', 'Other'), nullable=True, comment='Name of FERC account, derived from technology description and prime mover code. This name is associated with the record_id_eia_plant_gen record.'),
    sa.Column('ferc1_generator_agg_id_plant_gen', sa.Integer(), nullable=True, comment='ID dynamically assigned by PUDL to EIA records with multiple matches to a single FERC ID in the FERC-EIA manual matching process. This ID is associated with the record_id_eia_plant_gen record.'),
    sa.Column('generator_operating_year_plant_gen', sa.Integer(), nullable=True, comment="The year an associated plant_gen's generator went into service."),
    sa.Column('operational_status_pudl_plant_gen', sa.Enum('operating', 'retired', 'proposed'), nullable=True, comment='The operating status of the asset using PUDL categories of the record_id_eia_plant_gen record .'),
    sa.Column('generators_number', sa.Integer(), nullable=True, comment='The number of generators associated with each ``record_id_eia``.'),
    sa.ForeignKeyConstraint(['plant_id_eia', 'report_date'], ['core_eia860__scd_plants.plant_id_eia', 'core_eia860__scd_plants.report_date'], name=op.f('fk_out_eia__yearly_assn_plant_parts_plant_gen_plant_id_eia_core_eia860__scd_plants')),
    sa.ForeignKeyConstraint(['record_id_eia'], ['out_eia__yearly_plant_parts.record_id_eia'], name=op.f('fk_out_eia__yearly_assn_plant_parts_plant_gen_record_id_eia_out_eia__yearly_plant_parts')),
    sa.ForeignKeyConstraint(['record_id_eia_plant_gen'], ['out_eia__yearly_plant_parts.record_id_eia'], name=op.f('fk_out_eia__yearly_assn_plant_parts_plant_gen_record_id_eia_plant_gen_out_eia__yearly_plant_parts')),
    sa.ForeignKeyConstraint(['utility_id_eia', 'report_date'], ['core_eia860__scd_utilities.utility_id_eia', 'core_eia860__scd_utilities.report_date'], name=op.f('fk_out_eia__yearly_assn_plant_parts_plant_gen_utility_id_eia_core_eia860__scd_utilities')),
    sa.PrimaryKeyConstraint('record_id_eia', 'record_id_eia_plant_gen', name=op.f('pk_out_eia__yearly_assn_plant_parts_plant_gen'))
    )
    with op.batch_alter_table('out_pudl__yearly_assn_eia_ferc1_plant_parts', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_out_pudl__yearly_assn_eia_ferc1_plant_parts_record_id_eia_out_eia__yearly_plant_parts'), 'out_eia__yearly_plant_parts', ['record_id_eia'], ['record_id_eia'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('out_pudl__yearly_assn_eia_ferc1_plant_parts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_out_pudl__yearly_assn_eia_ferc1_plant_parts_record_id_eia_out_eia__yearly_plant_parts'), type_='foreignkey')

    op.drop_table('out_eia__yearly_assn_plant_parts_plant_gen')
    # ### end Alembic commands ###
