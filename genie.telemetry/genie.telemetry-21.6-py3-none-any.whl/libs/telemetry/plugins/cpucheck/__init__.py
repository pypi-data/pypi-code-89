# Enable abstraction; This is the root package.
from genie import abstract
abstract.declare_package(__name__)

from .plugin import Plugin
