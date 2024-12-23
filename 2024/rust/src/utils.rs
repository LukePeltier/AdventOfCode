use std::{
    fs::File,
    io::{self, Read},
    path::Path,
};

pub fn get_input(day: u8) -> io::Result<String> {
    let manifest_dir =
        std::env::var("CARGO_MANIFEST_DIR").expect("Failed to find manifest directory");
    let path = manifest_dir + &format!("/../inputs/day{:02}.input", day);
    // Try to open local file first
    match File::open(&path) {
        Ok(mut file) => {
            let mut contents = String::new();
            file.read_to_string(&mut contents)?;
            Ok(contents)
        }
        Err(_) => {
            // If local file doesn't exist, attempt to download
            download_input(day, &path)
        }
    }
}

#[allow(dead_code)]
pub fn get_example_input(day: u8) -> io::Result<String> {
    let manifest_dir =
        std::env::var("CARGO_MANIFEST_DIR").expect("Failed to find manifest directory");
    let path = manifest_dir + &format!("/../inputs/day{:02}.test", day);
    // Try to open local file first
    match File::open(&path) {
        Ok(mut file) => {
            let mut contents = String::new();
            file.read_to_string(&mut contents)?;
            Ok(contents)
        }
        Err(_) => {
            // If local file doesn't exist, attempt to download
            panic!("No test file found for day {}", day);
        }
    }
}

fn download_input(day: u8, path: &str) -> Result<String, io::Error> {
    // Ensure the directory exists
    if let Some(parent) = Path::new(path).parent() {
        std::fs::create_dir_all(parent)?;
    }

    let url = format!("https://adventofcode.com/2024/day/{}/input", day);

    let session = std::env::var("ADVENT_SESSION").map_err(|_| {
        io::Error::new(
            io::ErrorKind::NotFound,
            "ADVENT_SESSION environment variable not set",
        )
    })?;
    let session = format!("session={}", session);

    // Propagate network and file errors
    let mut response = ureq::get(&url)
        .set("Cookie", &session)
        .set(
            "User-Agent",
            "github.com/LukePeltier/AdventOfCode/tree/main/2024/rust/src/utils.rs",
        )
        .call()
        .map_err(|e| io::Error::new(io::ErrorKind::Other, e.to_string()))?
        .into_reader();

    // Create file and copy contents
    let mut file = File::create(path)?;
    std::io::copy(&mut response, &mut file)?;

    // Read the newly downloaded file
    let mut contents = String::new();
    File::open(path)?.read_to_string(&mut contents)?;

    Ok(contents)
}
