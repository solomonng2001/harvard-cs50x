-- Log of SQL Queries + Elaboration

-- SQL QUERY: Obtain Crime scene description to start investigation
SELECT description FROM crime_scene_reports WHERE year = 2020 AND month = 7 AND day = 28 AND UPPER(TRIM(street)) = 'CHAMBERLIN STREET';

/* description
Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. Interviews were conducted today with three witnesses who were present at the time — each of their interview transcripts mentions the courthouse. */

-- SQL QUERY: Obtain interviews on 28 JUL 2020, each of which mentions "courthouse"
SELECT transcript FROM interviews WHERE UPPER(transcript) LIKE "%COURTHOUSE%" AND year = 2020 AND month = 7 AND day = 28;

/* transcript
Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse parking lot and drive away. If you have security footage from the courthouse parking lot, you might want to look for cars that left the parking lot in that time frame.
I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at the courthouse, I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money.
As the thief was leaving the courthouse, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. */

/* SQL QUERY: Search individuals whoose information fulfils all the details in the above interview transcript
- license plate captured on courthouse security logs from 10:15am to 10:25am
- withdrew from ATM on Fifer Street on 28 Jul 2020 before 10:15am
- called from 10.15am to 10.25am for duration less than 1 minute */
SELECT name, people.id FROM courthouse_security_logs
JOIN people ON courthouse_security_logs.license_plate = people.license_plate
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND people.id IN (
SELECT bank_accounts.person_id FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2020 AND month = 7 AND day = 28 AND UPPER(atm_location) LIKE '%FIFER STREET%') AND people.id IN (
SELECT people.id FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60);

/* Suspects
name | id
Russell | 514354
Ernest | 686048 */

-- SQL Query: Check that suspect is flying off on 29 Jul 2020 from Fiftyville (earliest flight)
SELECT name, people.id, destination_airport_id FROM airports
JOIN flights ON airports.id = flights.origin_airport_id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON people.passport_number = passengers.passport_number
WHERE year = 2020 AND month = 7 AND day = 29 AND UPPER(city) = "FIFTYVILLE" AND (people.id = 514354 OR people.id = 686048) AND flights.id = (
SELECT flights.id FROM flights WHERE year = 2020 AND month = 7 AND day = 29 ORDER BY hour, minute DESC LIMIT 1);

/* Suspect
name | id | destination_airport_id
Ernest | 686048 | 4 */

-- SQL Query: Destination city / airport
SELECT city, full_name FROM airports WHERE id = 4;

/* Destination of Suspect
city | full_name
London | Heathrow Airport */

-- SQL Query: Find accomplice that received suspect's call (from 10.15am to 10.25am for duration less than 1 minute)
SELECT name, people.id FROM phone_calls
JOIN people ON phone_calls.receiver = people.phone_number
WHERE phone_calls.id IN (
SELECT phone_calls.id FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE people.id = 686048 AND year = 2020 AND month = 7 AND day = 28 AND duration < 60);

/* Accomplice
name | id
Berthold | 864400 */