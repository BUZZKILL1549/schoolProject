CREATE DATABASE school_app;

USE school_app;

CREATE TABLE announcements(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    PRIMARY KEY (Title)
);

CREATE TABLE assignments(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    PRIMARY KEY (Title)
);

CREATE TABLE class_diary(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    PRIMARY KEY (Title)
);

CREATE TABLE parent_concern(
    Subject             VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    PRIMARY KEY (Subject)
);


