#1
select countries.name, languages.language, languages.percentage
from countries, languages
where language = 'Slovene'
order by languages.percentage DESC;

#2
select countries.name, COUNT(*) as city_count
from countries
join cities
on countries.id = cities.country_id
group by cities.country_id
order by city_count DESC;


#3
select countries.name, cities.name, cities.population
from cities
join countries
on countries.id = cities.country_id
where countries.name = 'Mexico'
and cities.population > 500000
order by population DESC;

#4
select countries.name, languages.language, languages.percentage
from languages
join countries
on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage DESC;


#5
select countries.name, countries.population, countries.surface_area
from countries
where countries.surface_area <= 501
and countries.population > 100000;

#6
select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where countries.government_form = "Constitutional Monarchy"
and  countries.capital > 200
and countries.life_expectancy > 75;

#7
select cities.district, cities.name, cities.population, countries.name
from cities
join countries
on countries.id = cities.country_id
where cities.district = 'Buenos Aires'
and cities.population > 500000;

#8
select countries.region, COUNT(*) as country_count
from countries
group by countries.region
order by country_count DESC;
