CREATE SCHEMA IF NOT EXISTS NFCE_SCHEMA;
CREATE TABLE IF NOT EXISTS NFCE_SCHEMA.NFCE_LINKS (
    ID SERIAL NOT NULL,
    LINK TEXT NOT NULL,
    PRIMARY KEY (ID)
);
ALTER TABLE NFCE_SCHEMA.NFCE_LINKS OWNER TO postgres;
GRANT ALL ON TABLE NFCE_SCHEMA.NFCE_LINKS TO postgres;

INSERT INTO 
    NFCE_SCHEMA.NFCE_LINKS (LINK)
VALUES
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220601472861000720650050001718001134142000|2|1|1|3EF4376163EFAE184E32B003B6CE77D216173EFD'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220501472861000720650030001950281624502521|2|1|1|911825C250B4178AC77C4122E96A9E625DD9CF30'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220602178214000188650050007606041141344060|2|1|1|341B8213E0B6B2915440EF22500407BC7C6A4C67'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220602178214000188650020003698511201959270|2|1|1|001698017B663CF6FEF624329E6AD4D027A3F94A'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220602178214000188650030000649921202000183|2|1|1|B3317D7539B4E9F44304E08A30837562395CD47C'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220601472861000720650090002118521625054529|2|1|1|82034DC91C20DA9657A53DA6FDA11BFBFF1001CC'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220602178214000188650020003704411241909058|2|1|1|97DE26A490CE83F369338D890E448EC45FC58521'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220601472861000720650050001734001734188695|2|1|1|8CEA6827B22787654D190F53E67502CAACFA1257'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220701472861000720650090002129211515083440|2|1|1|5B4FBA527A29FC7EA20C21DACE90F7C7E78B4D6E'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220772251036000310650010011767811266881735|2|1|1|F2050805E28F2A5CA5C25CB5F24A1ECFE4CF0CE9'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220702178214000188650050007673281131933005|2|1|1|F1343573C0464E24BFF465DCE2DA0E255A42B7CE'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220702178214000188650030000705251201926028|2|1|1|D316618B0635900432EFD73E4BDB5DE4BF05239F'),
    ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220701472861000720650090002163881735154643|2|1|1|D0CA23BEB40F47CF9AA1DCA2FA349CE010C47689')
RETURNING *;
