from setuptools import setup, find_packages

setup(
    name="sqlalchemy-redshift-hsr",
    version="0.1.0",
    description="Compatibilidade Redshift com SQLAlchemy 2+",
    long_description="Compatibilidade Redshift com SQLAlchemy 2+",
    author="Handlei",
    author_email="handlei.rodrigues@gmail.com",
    packages=find_packages(include=['sqlalchemy_redshift_hsr', 'sqlalchemy_redshift_hsr.*']),
    include_package_data=True,
    install_requires=[
        "sqlalchemy>=2.0",
        "psycopg2>=2.5",
    ],
    entry_points={
        'sqlalchemy.dialects': [
            'redshift_hsr = sqlalchemy_redshift_hsr.dialect:RedshiftDialect_psycopg2',
            'redshift_hsr.psycopg2 = sqlalchemy_redshift_hsr.dialect:RedshiftDialect_psycopg2',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
)
