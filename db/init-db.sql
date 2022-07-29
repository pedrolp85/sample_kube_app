USE name;
CREATE TABLE names (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(10) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO names (name) VALUES
    ('Pedro'),
    ('David')
    ;
