# Skylog Database Schema

## Checklist
- [ ] **Users**
- [ ] **Aircraft**
- [ ] **Flight Plans**
- [ ] **Airports**
- [ ] **Facilities**
- [ ] **Weather**
- [ ] **Notifications**
- [ ] **Rentals**

## Schemas

### Users
```sql
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    groups UNSIGNED BIG INT,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `groups`:
- `0` - Default Group (User)
- `1` - Aircraft Maintenance
- `2` - Airline
- `4` - Automated (Bot)
- `8` - Admin

### Aircraft
```sql
CREATE TABLE aircraft (
    id SERIAL PRIMARY KEY,
    registration TEXT NOT NULL UNIQUE,
    manufacturer TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacture_date DATE NOT NULL,
    aircraft_type TEXT NOT NULL,
    owner_id TEXT NOT NULL REFERENCES users(id),
    status TEXT NOT NULL,
    hours_flown INT DEFAULT 0,
    last_maintenance TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    next_maintenance TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tail_number TEXT NOT NULL UNIQUE,
    classification TEXT NOT NULL
);
```

#### `status`:
Can be one of:
- Available
- In Use
- Maintenance
- Retired
- Decommissioned

#### `classification`:
Can be one of:
- Commercial
- Private
- Cargo
- Military
- Experimental

### Flight Plans
```sql
CREATE TABLE flight_plans (
    id SERIAL PRIMARY KEY,
    associated_user TEXT NOT NULL REFERENCES users(id),
    route TEXT NOT NULL,
    departure_airport TEXT NOT NULL,
    arrival_airport TEXT NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    sid TEXT,
    star TEXT,
    sia TEXT
);
```

#### `route`:
- A string representing the route of the flight, including waypoints and airways.
- Example: `KLAX DARRK3.SCTRR SCTRR KNGDM.HAWKZ8 KSEA`

#### `departure_airport`:
- The ICAO code of the departure airport.
- Example: `KLAX`

#### `arrival_airport`:
- The ICAO code of the arrival airport.
- Example: `KSEA`

### Airports

Note: this might get replaced with an external database instead of our own.

```sql
CREATE TABLE airports (
    icao TEXT PRIMARY KEYm
    faa TEXT NOT NULL,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL,
    elevation INT NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    runways INT NOT NULL,
    type TEXT NOT NULL,
    status TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `type`:
Can be one of:
- Public
- Private
- Military
- Heliport
- Seaplane Base

#### `status`:
Can be one of:
- Open
- Closed
- Under Construction
- Decommissioned

#### `runways`:
- The number of runways at the airport.

### Runways
```sql
CREATE TABLE runways (
    id SERIAL PRIMARY KEY,
    airport_icao TEXT NOT NULL REFERENCES airports(icao),
    runway_number TEXT NOT NULL,
    length INT NOT NULL,
    width INT NOT NULL,
    surface_type TEXT NOT NULL,
    direction FLOAT NOT NULL,
    elevation INT NOT NULL,
    grade FLOAT NOT NULL,
    lighting TEXT NOT NULL,
    approach_lighting TEXT NOT NULL,
    ils TEXT NOT NULL,
    ils_frequency FLOAT NOT NULL,
    last_inspection TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `surface_type`:
Can be one of:
- Asphalt
- Concrete
- Grass
- Dirt
- Water

#### `lighting`:
Can be one of:
- None
- Low Intensity
- Medium Intensity
- High Intensity

#### `approach_lighting`:
Can be one of:
- None
- ALSF-1
- ALSF-2
- MALSR
- REIL

#### `ils`:
- Represents if the runway has an ILS.
- Can be one of:
- None
- CAT I
- CAT II
- CAT III

#### `ils_frequency`:
- The frequency of the ILS in MHz.
- Example: `108.10`
- If `ils` is `None`, this field should be `0.0`.

### Facilities
```sql
CREATE TABLE facilities (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    location TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    operating_hours TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `type`:
Can be one of:
- Fuel Station
- Maintenance Hangar
- Flight School
- Restaurant
- Parking
- Customs
- Security

#### `operating_hours`:
- The operating hours of the facility.
- Example: `Mon-Fri 08:00-17:00, Sat-Sun 09:00-15:00`
- Can be `24/7` if the facility is open all the time.

#### `contact_info`:
- The contact information of the facility.
- Example: `Name/Company Name <email@domain.com> +1-555-555-5555`
- Can be `None` if not applicable/automated facility (such as a weather or fuel station)

### Weather
```sql
CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    airport_icao TEXT NOT NULL REFERENCES airports(icao),
    temperature FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    wind_direction FLOAT NOT NULL,
    visibility FLOAT NOT NULL,
    cloud_cover FLOAT NOT NULL,
    precipitation FLOAT NOT NULL,
    raw TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `raw`:
- The raw METAR string.
- Example: `METAR KLAX 121753Z 18015G25KT 10SM FEW020 SCT250 25/10 A2992 RMK AO2 SLP134`

### Notifications
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    type TEXT NOT NULL,
    message TEXT NOT NULL,
    read BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### `type`:
Can be one of:
- General
- Maintenance
- Flight Plan
- Weather
- Rental
- Facility
- Security

### Rentals
```sql
CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id),
    aircraft_id INT NOT NULL REFERENCES aircraft(id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    status TEXT NOT NULL,
    pickup_location TEXT NOT NULL,
    dropoff_location TEXT NOT NULL,
    total_cost FLOAT NOT NULL,
    payment_status TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

