-- PostgreSQL database dump

-- Started on 2011-07-10 18:38:29

-- Set the statement timeout to unlimited
SET statement_timeout = 0;
-- Set the client encoding to UTF-8
SET client_encoding = 'UTF8';
-- Disable standard conforming strings
SET standard_conforming_strings = off;
-- Disable function body checks
SET check_function_bodies = false;
-- Set the minimum level of messages to warnings
SET client_min_messages = warning;
-- Disable warnings on escape string syntax
SET escape_string_warning = off;

-- Set the search path to public and pg_catalog schemas
SET search_path = public, pg_catalog;

-- Set the default tablespace to empty (use the default tablespace)
SET default_tablespace = '';

-- Set the default with OIDs to false
SET default_with_oids = false;

-- Table of Contents entry for the test_xy table
-- TOC entry 2384 (class 1259 OID 73780)
-- Dependencies: 3
-- Name: test_xy; Type: TABLE; Schema: public; Owner: -; Tablespace: 

-- Create the test_xy table with gid, x, and y columns
CREATE TABLE test_xy (
    gid integer NOT NULL,
    x double precision,
    y double precision
);

-- Table of Contents entry for the data of test_xy table
-- TOC entry 2684 (class 0 OID 73780)
-- Dependencies: 2384
-- Data for Name: test_xy; Type: TABLE DATA; Schema: public; Owner: -

INSERT INTO test_xy (gid, x, y) VALUES (1, -1.3274956217162872, 0.55166374781085814);
INSERT INTO test_xy (gid, x, y) VALUES (2, -1.264448336252189, 0.5376532399299474);
INSERT INTO test_xy (gid, x, y) VALUES (3, -1.3029772329246936, 0.48161120840630467);
INSERT INTO test_xy (gid, x, y) VALUES (4, -1.0122591943957968, 0.42907180385288957);
INSERT INTO test_xy (gid, x, y) VALUES (5, -0.95621716287215408, 0.59019264448336251);
INSERT INTO test_xy (gid, x, y) VALUES (6, -0.22767075306479856, 0.32399299474605958);
INSERT INTO test_xy (gid, x, y) VALUES (7, -0.19964973730297708, 0.34500875656742558);
INSERT INTO test_xy (gid, x, y) VALUES (8, -0.2206654991243433, 0.37302977232924706);
INSERT INTO test_xy (gid, x, y) VALUES (9, -0.098073555166374726, 0.19789842381786338);
INSERT INTO test_xy (gid, x, y) VALUES (10, -0.11558669001751309, 0.27845884413309974);
INSERT INTO test_xy (gid, x, y) VALUES (11, -0.18213660245183894, 0.28196147110332759);
INSERT INTO test_xy (gid, x, y) VALUES (12, -0.57793345008756569, -0.51313485113835378);
INSERT INTO test_xy (gid, x, y) VALUES (13, -0.59194395796847621, -0.48161120840630467);
INSERT INTO test_xy (gid, x, y) VALUES (14, -0.62697022767075294, -0.52364273204903677);
INSERT INTO test_xy (gid, x, y) VALUES (15, -0.47635726795096311, -0.50262697022767078);
INSERT INTO test_xy (gid, x, y) VALUES (16, 0.098073555166374948, -0.11383537653239928);
INSERT INTO test_xy (gid, x, y) VALUES (17, 0.43432574430823134, 0.16987740805604212);
INSERT INTO test_xy (gid, x, y) VALUES (18, 0.41330998248686512, 0.15236427320490376);
INSERT INTO test_xy (gid, x, y) VALUES (19, 0.35376532399299476, 0.18038528896672501);
INSERT INTO test_xy (gid, x, y) VALUES (20, 0.48686514886164645, 0.092819614711033172);
INSERT INTO test_xy (gid, x, y) VALUES (21, 0.45884413309982497, 0.14535901926444827);
INSERT INTO test_xy (gid, x, y) VALUES (22, 1.7267950963222418, 0.8528896672504378);
INSERT INTO test_xy (gid, x, y) VALUES (23, 1.5096322241681261, -0.092819614711033283);
INSERT INTO test_xy (gid, x, y) VALUES (24, 1.5096322241681261, -0.050788091068301178);
INSERT INTO test_xy (gid, x, y) VALUES (25, 1.6672504378283715, 0.84588441330998254);
INSERT INTO test_xy (gid, x, y) VALUES (26, 1.7057793345008756, 0.7583187390542907);
INSERT INTO test_xy (gid, x, y) VALUES (27, 1.555166374781086, 0.54465849387040288);
INSERT INTO test_xy (gid, x, y) VALUES (28, 1.5936952714535901, 0.73730297723292471);
INSERT INTO test_xy (gid, x, y) VALUES (29, 1.6427320490367778, 0.61821366024518398);
INSERT INTO test_xy (gid, x, y) VALUES (30, 1.7408056042031523, 0.59719789842381799);
INSERT INTO test_xy (gid, x, y) VALUES (31, 1.555166374781086, 0.66024518388791598);


-- Table of Contents entry for the primary key constraint of test_xy table
-- TOC entry 2683 (class 2606 OID 73784)
-- Dependencies: 2384 2384
-- Name: test_xy_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 

-- Add a primary key constraint to the test_xy table on the gid column
ALTER TABLE ONLY test_xy
    ADD CONSTRAINT test_xy_pkey PRIMARY KEY (gid);

-- Completed on 2011-07-10 18:38:29

-- PostgreSQL database dump complete

