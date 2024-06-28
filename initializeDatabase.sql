CREATE DATABASE school_app;

USE school_app;

CREATE TABLE users(
    ID                  INT         NOT NULL,
    Uname               VARCHAR(50) NOT NULL,
    Pwd                 VARCHAR(50) NOT NULL,

    CONSTRAINT PK_ID    PRIMARY KEY (ID)
);

CREATE TABLE announcements(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    CONSTRAINT PK_Title PRIMARY KEY (Title)
);

CREATE TABLE assignments(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    CONSTRAINT PK_Title PRIMARY KEY (Title)
);

CREATE TABLE class_diary(
    Title               VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    CONSTRAINT PK_Title PRIMARY KEY (Title)
);

CREATE TABLE parent_concern(
    Subject             VARCHAR(50) NOT NULL,
    Description         TEXT        NOT NULL,

    CONSTRAINT PK_Title PRIMARY KEY (Subject)
);


