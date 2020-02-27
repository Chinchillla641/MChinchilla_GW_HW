ALTER DATABASE de8vg0eb5jkmn0 OWNER TO ceqpjjmbiuiqtz;

-- Create Table "Measels Data"
CREATE TABLE public."Measels Data"
(
)
;
ALTER TABLE public."Measels Data"
    OWNER to ceqpjjmbiuiqtz;
	
-- Generate columns
ALTER TABLE public."Measels Data"
    ADD COLUMN "State" char(15);
ALTER TABLE public."Measels Data"
    ADD COLUMN "Count" integer;

-- Create Table "Vaccines"
CREATE TABLE public."Vaccines"
(
)
;
ALTER TABLE public."Vaccines"
    OWNER to ceqpjjmbiuiqtz;

-- Generate columns
ALTER TABLE public."Vaccines"
    ADD COLUMN "State" char(15);
ALTER TABLE public."Vaccines"
    ADD COLUMN "Measles cases (2019)" integer;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Mumps cases (2019)" text;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Pertussis cases (2018)" integer;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Religious Exemption" char(10);
ALTER TABLE public."Vaccines"
    ADD COLUMN "Philosophical Exemption" char(10);
	
-- Create Table "Measels 24months-2016"
CREATE TABLE public."Measels 24months-2016"
(
)
;
ALTER TABLE public."Measels 24months-2016"
    OWNER to ceqpjjmbiuiqtz;

-- Generate columns
ALTER TABLE public."Measels 24months-2016"
    ADD COLUMN "State" char(20);
ALTER TABLE public."Measels 24months-2016"
    ADD COLUMN "2016" decimal(3,1);