# Queue

## item-timeout

config.py line 3: DEFAULT_TIMEOUT is 300; ops approved dropping it to 30. Change the value.

## item-logprefix

Ops wants the log prefix changed from "WARN:" to "[warn]" across the service. Update the prefix wherever it is emitted.
