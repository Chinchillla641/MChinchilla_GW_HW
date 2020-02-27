ALTER DATABASE dfdejcj5u03mo2 OWNER TO vqaaeqeiojsagw;

-- Create Table "Measels_Data"
CREATE TABLE public."Measels_Data"
(
)
;
ALTER TABLE public."Measels_Data"
    OWNER to vqaaeqeiojsagw;
	
-- Generate columns
ALTER TABLE public."Measels_Data"
    ADD COLUMN "State" char(15);
ALTER TABLE public."Measels_Data"
    ADD COLUMN "Count" integer;

-- Create Table "Vaccines"
CREATE TABLE public."Vaccines"
(
)
;
ALTER TABLE public."Vaccines"
    OWNER to vqaaeqeiojsagw;

-- Generate columns
ALTER TABLE public."Vaccines"
    ADD COLUMN "State" char(15);
ALTER TABLE public."Vaccines"
    ADD COLUMN "Measles_cases_2019" integer;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Mumps_cases_2019" text;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Pertussis_cases_2018" integer;
ALTER TABLE public."Vaccines"
    ADD COLUMN "Religious_Exemption" char(10);
ALTER TABLE public."Vaccines"
    ADD COLUMN "Philosophical_Exemption" char(10);
	
-- Create Table "Measels 24months-2016"
CREATE TABLE public."Measels_24months_2016"
(
)
;
ALTER TABLE public."Measels_24months_2016"
    OWNER to vqaaeqeiojsagw;

-- Generate columns
ALTER TABLE public."Measels_24months_2016"
    ADD COLUMN "State" char(20);
ALTER TABLE public."Measels_24months_2016"
    ADD COLUMN "_2016" decimal(3,1);