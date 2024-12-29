use std::fs;
use std::collections::HashMap;

fn decode_map(raw_orbit_map: Vec<Vec<String>>) -> HashMap<String, String> {
    let mut orbit_map: HashMap<String, String> = HashMap::new();
    for planet_pair in raw_orbit_map.into_iter() {
        let orbits = planet_pair[0].clone();
        let planet = planet_pair[1].clone();
        orbit_map.insert(planet, orbits);
    }
    return orbit_map;
}

fn count_orbits(orbit_map: HashMap<String, String>) -> u32 {
    let mut tot_orbits: u32 = 0;
    let mut save_counts: HashMap<String, u32> = HashMap::new();

    for planet in orbit_map.keys() {
        if save_counts.contains_key(planet) {

        }
        else {
            let mut line: Vec<&String> = Vec::new();
            line.push(&planet);
            let mut next = orbit_map.get(planet).unwrap();
            while orbit_map.contains_key(next) && !save_counts.contains_key(next) {
                line.push(next);
                next = orbit_map.get(next).unwrap();

            }
            let base: u32;
            if save_counts.contains_key(next) {
                base = *save_counts.get(next).unwrap() + line.len() as u32;
            }
            else {
                base = line.len() as u32;
            }
            for (i, planet) in line.into_iter().enumerate() {
                let planet_str = planet.clone().to_string();
                save_counts.insert(planet_str, base - i as u32);
            }
        }
        tot_orbits = tot_orbits + save_counts.get(planet).unwrap();
    }
    return tot_orbits;
}

fn find_sant(orbit_map: HashMap<String,String>) -> u32 {
    // Find path for my orbits
    let me: String = String::from("YOU");
    let mut my_orbits: Vec<&String> = Vec::new();
    let mut next = orbit_map.get(&me).unwrap();
    while orbit_map.contains_key(next) {
        my_orbits.push(next);
        next = orbit_map.get(next).unwrap();
    }

    // Find path for santas orbits
    let santa: String = String::from("SAN");
    let mut santas_orbits: Vec<&String> = Vec::new();
    let mut next = orbit_map.get(&santa).unwrap();
    while orbit_map.contains_key(next) {
        santas_orbits.push(next);
        next = orbit_map.get(next).unwrap();
    }

    for (jumps_me, planet_me) in my_orbits.iter().enumerate() {
        for (jumps_santa, planet_santa) in santas_orbits.iter().enumerate() {
            if planet_me == planet_santa {
                return jumps_me as u32 + jumps_santa as u32
            }
        }
    }

    return 0;
}

fn main() {
    let raw_orbit_map: Vec<Vec<String>> = fs::read_to_string("input.txt")
                                        .unwrap()
                                        .split("\n")
                                        .filter(|x| !x.is_empty())
                                        .map(|x| x.split(")")
                                            .map(|y| y.to_string())
                                            .collect()
                                        )
                                        .   collect();
    
    let orbit_map: HashMap<String, String> = decode_map(raw_orbit_map);

    let total_orbits = count_orbits(orbit_map.clone());
    println!("Total number of orbits are: {}", total_orbits);

    let jumps_needed = find_sant(orbit_map);
    println!("Number of jumps needed to get to santa: {}", jumps_needed);
}
