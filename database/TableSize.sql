CREATE TABLE size (
    idSize serial PRIMARY KEY,
    description text,
    height float not null,
    diameter float not null,
    tare float not null
);
