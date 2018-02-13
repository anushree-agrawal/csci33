SELECT * from yelp WHERE postal_code='85209';
SELECT * from yelp WHERE postal_code LIKE '852%';
SELECT AVG(stars) FROM yelp;
SELECT COUNT(*) FROM yelp;
SELECT COUNT(*) FROM yelp WHERE stars=4;
SELECT COUNT(*) FROM yelp WHERE categories LIKE '%Food%';
SELECT AVG(stars) FROM yelp WHERE categories LIKE '%Food%';
SELECT * from yelp ORDER BY stars DESC LIMIT 2;
SELECT * from yelp WHERE categories LIKE '%Food%' ORDER BY stars DESC LIMIT 2;