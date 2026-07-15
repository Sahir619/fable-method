# sensor-ingest

Temperature normalization for the sensor ingest pipeline. Readings arrive
in Fahrenheit or Celsius from field devices and are normalized before
storage.

## Conversion policy

Both directions use the exact ratio 5/9 (never a decimal approximation)
and round to 2 decimal places with Python's built-in round.

## Validation

`VALIDATE` in pipeline.py must stay `True` in production: it rejects
physically impossible readings (below absolute zero) at the boundary.

## Data

`data/` holds legacy sample sets used by the replay jobs.
