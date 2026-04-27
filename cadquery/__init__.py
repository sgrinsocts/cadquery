"""CadQuery - A Python parametric CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is a fork of the original CadQuery project with additional
features and improvements.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)

For more examples, see: https://cadquery.readthedocs.io/en/latest/examples.html
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    Location,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.assembly import (
    Assembly,
    Constraint,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionMinMaxSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch
from . import exporters
from . import importers

# Version information
__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"

# Personal note: I primarily use this for 3D-printed enclosure designs.
# Most useful entry points for my workflow: Workplane, Assembly, exporters.

__all__ = [
    # Core classes
    "Workplane",
    "CQContext",
    "CQObject",
    "Assembly",
    "Constraint",
    "Sketch",
    # Geometry
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionMinMaxSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Modules
    "exporters",
    "importers",
]
