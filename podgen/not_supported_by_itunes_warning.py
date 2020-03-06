# Kept for backwards compatibility
from podgen.warnings import NotSupportedByItunesWarning

import warnings
warnings.warn(
    "NotSupportedByItunesWarning should be imported from podgen. Support for "
    "importing from podgen.not_supported_by_itunes_warning will be dropped in "
    "v2.0.0.",
    category=DeprecationWarning,
    stacklevel=2
)
