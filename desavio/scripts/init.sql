create database desafio;

\c desafio

create table MKTP (
    id serial not null,
    "Country Name"          varchar(1000),
    "Country Code"          varchar(1000),
    "Indicator Name"        varchar(1000),
    "Indicator Code"        varchar(1000),
	"1960"NUMERIC,
    "1961" NUMERIC,
    "1962" NUMERIC,
    "1963" NUMERIC,
    "1964" NUMERIC,
    "1965" NUMERIC,
    "1966" NUMERIC,
    "1967" NUMERIC,
    "1968" NUMERIC,
    "1969" NUMERIC,
    "1970" NUMERIC,
    "1971" NUMERIC,
    "1972" NUMERIC,
    "1973" NUMERIC,
    "1974" NUMERIC,
    "1975" NUMERIC,
    "1976" NUMERIC,
    "1977" NUMERIC,
    "1978" NUMERIC,
    "1979" NUMERIC,
    "1980" NUMERIC,
    "1981" NUMERIC,
    "1982" NUMERIC,
    "1983" NUMERIC,
    "1984" NUMERIC,
    "1985" NUMERIC,
    "1986" NUMERIC,
    "1987" NUMERIC,
    "1988" NUMERIC,
    "1989" NUMERIC,
    "1990" NUMERIC,
    "1991" NUMERIC,
    "1992" NUMERIC,
    "1993" NUMERIC,
    "1994" NUMERIC,
    "1995" NUMERIC,
    "1996" NUMERIC,
    "1997" NUMERIC,
    "1998" NUMERIC,
    "1999" NUMERIC,
    "2000" NUMERIC,
    "2001" NUMERIC,
    "2002" NUMERIC,
    "2003" NUMERIC,
    "2004" NUMERIC,
    "2005" NUMERIC,
    "2006" NUMERIC,
    "2007" NUMERIC,
    "2008" NUMERIC,
    "2009" NUMERIC,
    "2010" NUMERIC,
    "2011" NUMERIC,
    "2012" NUMERIC,
    "2013" NUMERIC,
    "2014" NUMERIC,
    "2015" NUMERIC,
    "2016" NUMERIC,
    "2017" NUMERIC,
    "2018" NUMERIC,
    "2019" NUMERIC,
    "2020" NUMERIC,
    "2021" NUMERIC

);

CREATE TABLE COUNTRY(
"Country Code" 	varchar(100) null,
region			varchar(1000) null,
incomeGroup		varchar(1000) null,
specialNotes	varchar(8000) null,
tableName		varchar(1000) null
);

CREATE TABLE INDICADOR(
	"INDICATOR_CODE" VARCHAR(100)
	,"INDICATOR_NAME" VARCHAR(200)
	,"SOURCE_NOTE" VARCHAR(8000)
	,"SOURCE_ORGANIZATION" VARCHAR(1000)
);



CREATE TABLE MKTP_TRAT(
	ID SERIAL,
	"Country Name"          varchar(1000) null,
    "Country Code"          varchar(1000) null,
    "Indicator Name"        varchar(1000) null,
    "Indicator Code"        varchar(1000) null,
	ANO NUMERIC,
	VALOR_PIB NUMERIC
);