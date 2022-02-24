create table Credits(
   cred_cast text,
   crew text,
   id int  
);

create table Keywords(
   id int,      
   keywords text
);

create table Links(
   movieId int, 
   imdbId int,  
   tmdbId int
);

create table Ratings( 
   userId int, 
   movieId int, 
   rating float,
   timestamp int
);

create table Ratings_Small( 
   userId int,
   movieId int, 
   rating float,
   timestamp int
);

create table Movies_Metadata(
   adult boolean,
   belongs_to_collection varchar(190),
   budget int,
   genres varchar(270),
   homepage varchar(250),
   id int, 					
   imdb_id int,				
   original_language varchar(10),
   original_title varchar(110),
   overview text,
   popularity varchar(10),
   poster_path varchar(40),
   production_companies text,
   production_countries text,
   release_date date,
   revenue bigint,
   runtime float,
   spoken_languages text,
   status varchar(20),
   tagline varchar(300),
   title varchar(110),
   video boolean,
   vote_average float,
   vote_count int
);

ALTER TABLE Movies_Metadata ADD PRIMARY KEY (id)
ALTER TABLE CREDITS ADD PRIMARY KEY (id)
ALTER TABLE KEYWORDS ADD PRIMARY KEY (id);
ALTER TABLE Links ADD PRIMARY KEY (movieId);
ALTER TABLE Ratings ADD PRIMARY KEY (userId,movieId);
ALTER TABLE Ratings_Small ADD PRIMARY KEY (userId,movieId);

ALTER TABLE CREDITS ADD FOREIGN  KEY (ID) REFERENCES KEYWORDS(id);
ALTER TABLE RATINGS ADD FOREIGN  KEY (MOVIEID) REFERENCES LINKS (MOVIEID);
ALTER TABLE RATINGS_SMALL ADD FOREIGN  KEY (MOVIEID) REFERENCES LINKS (MOVIEID);
ALTER TABLE CREDITS ADD FOREIGN  KEY (ID) REFERENCES Movies_Metadata(id);
