CREATE TABLE person (
    driver_id INT PRIMARY KEY,          
    name VARCHAR(50) NOT NULL,         
    address VARCHAR(150)                
);

CREATE TABLE car (
    license_plate VARCHAR(15) PRIMARY KEY,   
    model VARCHAR(50) NOT NULL,              
    year INT CHECK (year >= 1886)            
);	

CREATE TABLE owns (
    driver_id INT,                           
    license_plate VARCHAR(15),               
    PRIMARY KEY (driver_id, license_plate),  
    FOREIGN KEY (driver_id) REFERENCES person(driver_id) ON DELETE CASCADE,
    FOREIGN KEY (license_plate) REFERENCES car(license_plate) ON DELETE CASCADE
);


CREATE TABLE accident (
    report_number INT PRIMARY KEY,      
    date DATE NOT NULL,                 
    location VARCHAR(150) NOT NULL       
);


CREATE TABLE participated (
    report_number INT,                               
    license_plate VARCHAR(15),                       
    driver_id INT,                                   
    damage_amount DECIMAL(10, 2),                    
    PRIMARY KEY (report_number, license_plate, driver_id),  
    FOREIGN KEY (report_number) REFERENCES accident(report_number) ON DELETE CASCADE,
    FOREIGN KEY (license_plate) REFERENCES car(license_plate) ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES person(driver_id) ON DELETE CASCADE
);