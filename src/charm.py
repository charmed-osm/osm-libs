#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.


"""A placeholder charm for the Osm libs."""

from ops.charm import CharmBase
from ops.main import main


class OsmLibsCharm(CharmBase):
    """Placeholder charm for Osm libs."""

    pass


if __name__ == "__main__":
    main(OsmLibsCharm)
