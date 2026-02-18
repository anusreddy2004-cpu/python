# Write your MySQL query statement below
    select p.firstname,p.lastname,a.city,a.state
    From person p
    LEFT JOIN address a
    on p.personId = a.personId