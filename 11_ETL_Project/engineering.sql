-- Create tables for raw data to be loaded into
CREATE TABLE battle_weather (
	isqno CHAR(40) NOT NULL PRIMARY KEY,
	"War" TEXT,
	"Battle Name" TEXT,
	"Location" TEXT,
	"Campaign" TEXT,
	"Attacker Win" TEXT,
	"Dry/Wet" TEXT,
	"High/Low Precipitaton/Sunny/Cloudy" TEXT,
	"Temperature (Hot, Cold, Temperate)" TEXT,
	"Season" TEXT,
	"Tropical/Desert/Temperate" TEXT,
	"Attacker 1" TEXT,
	"Actor 1" TEXT,
	"Attacker 2" TEXT,
	"Actor 2" TEXT,
	"Attacker 3" TEXT DEFAULT 'NULL',
	"Actor 3" TEXT DEFAULT 'NULL',
	"Attacker 4" TEXT DEFAULT 'NULL',
	"Actor 4" TEXT DEFAULT 'NULL'
);