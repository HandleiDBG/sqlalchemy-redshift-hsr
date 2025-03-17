from pkg_resources import DistributionNotFound, get_distribution, parse_version

for package in ['psycopg2', 'psycopg2-binary', 'psycopg2cffi']:
    try:
        if get_distribution(package).parsed_version < parse_version('2.5'):
            raise ImportError('Minimum required version for psycopg2 is 2.5')
        break
    except DistributionNotFound:
        pass

try:
    __version__ = get_distribution('sqlalchemy-redshift-hsr').version
except DistributionNotFound:
    __version__ = '0.1.0'

from sqlalchemy.dialects import registry

# Corrigido para o seu pacote: sqlalchemy_redshift_hsr.dialect
registry.register(
    "redshift_hsr", "sqlalchemy_redshift_hsr.dialect", "RedshiftDialect_psycopg2"
)
registry.register(
    "redshift_hsr.psycopg2", "sqlalchemy_redshift_hsr.dialect", "RedshiftDialect_psycopg2"
)
registry.register(
    "redshift_hsr+psycopg2cffi", "sqlalchemy_redshift_hsr.dialect", "RedshiftDialect_psycopg2cffi"
)
registry.register(
    "redshift_hsr+redshift_connector", "sqlalchemy_redshift_hsr.dialect", "RedshiftDialect_redshift_connector"
)
