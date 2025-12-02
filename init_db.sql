CREATE TABLE IF NOT EXISTS ohlcv (
    datetime TIMESTAMPTZ PRIMARY KEY,
    open     NUMERIC(12,4) NOT NULL,
    high     NUMERIC(12,4) NOT NULL,
    low      NUMERIC(12,4) NOT NULL,
    close    NUMERIC(12,4) NOT NULL,
    volume   BIGINT        NOT NULL
);
