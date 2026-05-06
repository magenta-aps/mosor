<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# MO-SOR

OS2mo integration for [Sundhedsvæsenets Organisationsregister (SOR)](https://services.nsi.dk/SOR2/).


## Usage

```
docker-compose up -d
```

Configuration is done through environment variables. Available options can be
seen in [mo_sor/config.py](mo_sor/config.py). Complex variables such as dicts
or lists can be given as JSON strings, as specified by Pydantic's settings
parser.


## Development

The integration is a [FastRAMQPI](https://git.magenta.dk/rammearkitektur/FastRAMQPI)
application using OS2mo's GraphQL event system. FastRAMQPI declares event
listeners against MO; MO's GraphQL fetcher polls events and HTTP-POSTs them to
FastAPI routes on this integration. Listeners are configured in
[mo_sor/app.py](mo_sor/app.py) and the handlers live in
[mo_sor/events.py](mo_sor/events.py).

The GraphQL client is generated from `schema.graphql` + `queries.graphql`
using `ariadne-codegen`. To regenerate after changing queries:

```
curl -O http://localhost:5000/graphql/v29/schema.graphql
poetry run ariadne-codegen
```


## Versioning

This project uses [Semantic Versioning](https://semver.org/) with the following
strategy:
- MAJOR: Incompatible API changes.
- MINOR: Backwards-compatible updates and functionality.
- PATCH: Backwards-compatible bug fixes.


## Authors

Magenta ApS <https://magenta.dk>


## License

- This project: [MPL-2.0](LICENSES/MPL-2.0.txt)

This project uses [REUSE](https://reuse.software) for licensing. All licenses
can be found in the [LICENSES folder](LICENSES/) of the project.
