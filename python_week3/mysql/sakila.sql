#1
select customer.first_name, customer.last_name, customer.email, address.address from customer
join address on address.address_id = customer.address_id
where city_id = 312;

#2
select film.title, film.description, film.release_year,film.special_features, film.rating, category.name
from film
join film_category
on film.film_id = film_category.film_id
join category
on category.category_id = film_category.category_id
where category.category_id = 5;

#3
select film.title, film.description, film.release_year
from film
join film_actor
on film.film_id = film_actor.film_id
join actor
on actor.actor_id = film_actor.actor_id
where actor.actor_id = 5

#4
select customer.first_name, customer.last_name, customer.email, address.address, customer.store_id, address.city_id
from customer
join address
on address.address_id = customer.address_id
join city
on city.city_id = address.city_id
where customer.store_id = 1
and (address.city_id = 1 or address.city_id = 42  or address.city_id = 312 or address.city_id = 459);

#5
select film.title, film.rating, film.description, film.special_features, actor.first_name, actor.last_name
from film
join film_actor
on film.film_id = film_actor.film_id
join actor
on actor.actor_id = film_actor.actor_id
where film.rating = 'G' and actor.actor_id = 15;

#6
select film.title, film.rating, film.description, film.special_features, actor.first_name, actor.last_name
from film
join film_actor
on film.film_id = film_actor.film_id
join actor
on actor.actor_id = film_actor.actor_id
where film.film_id = 369;

#7
select film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, film.rental_rate, category.category_id
from film
join film_category
on film.film_id = film_category.film_id
join category
on category.category_id = film_category.category_id
where category.category_id = 7 and film.rental_rate = 2.99;

#8
select film.film_id, film.title, film.description, film.release_year, film.special_features, film.rating
from film
join film_category
on film.film_id = film_category.film_id
join category
on category.category_id = film_category.category_id
join film_actor
on film.film_id = film_actor.film_id
join actor
on actor.actor_id = film_actor.actor_id
where category.name LIKE 'Action'
and actor.first_name = 'SANDRA'
and actor.last_name = 'KILMER';
