//this program creates m mod 3, m mod 4, and m mod 8 to be added to the triangular number mod m dataframe

use std::time::{Duration, Instant};
use std::error::Error;
use csv::Writer;

fn main() -> Result<(), Box<dyn Error>> {
    let start = Instant::now();
    let mut wtr = Writer::from_path("mod348.csv")?;

    wtr.write_record(&["mod3", "mod4", "mod8"])?;

    for m in 3..1_000_000 {
        let t3 = n%3;
        let t4 = n%4;
        let t8 = n%8;

        wtr.write_record(&[t3.to_string(), t4.to_string(), t8.to_string()])?;
    }

    wtr.flush()?;

    let duration = start.elapsed();
    println!("Time elapsed is: {:?}", duration);

    Ok(())
}
