CREATE (:User {id: 4112, completion_percentage: 14, gender: "man", age: 26}) FOR VT FROM "-INF" TO "1980-01-01T00:00:00";
CREATE (:User {id: 1075, completion_percentage: 38, gender: "man", age: 29}) FOR VT FROM "-INF" TO "1989-01-01T00:00:00";
MATCH (n:User {id: 4112}), (m:User {id: 1075}) CREATE (n)-[e: Friend]->(m);


