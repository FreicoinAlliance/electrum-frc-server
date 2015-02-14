from setuptools import setup

setup(
    name="electrum-frc-server",
    version="0.9",
    scripts=['run_electrum_frc_server','electrum-frc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumfrcserver':'src'
        },
    py_modules=[
        'electrumfrcserver.__init__',
        'electrumfrcserver.utils',
        'electrumfrcserver.storage',
        'electrumfrcserver.deserialize',
        'electrumfrcserver.networks',
        'electrumfrcserver.blockchain_processor',
        'electrumfrcserver.server_processor',
        'electrumfrcserver.processor',
        'electrumfrcserver.version',
        'electrumfrcserver.ircthread',
        'electrumfrcserver.stratum_tcp',
        'electrumfrcserver.stratum_http'
    ],
    description="Freicoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum-FRC Lightweight Freicoin Wallet"""
)


