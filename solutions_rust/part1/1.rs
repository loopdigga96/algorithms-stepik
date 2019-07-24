use std::io;

fn main() {
    let reader = io::stdin();
    let mut buffer: String = String::new();

    reader.read_line(&mut buffer)
        .ok()
        .expect("ERRORMSG");
    let inputs: Vec<&str> = buffer.split(' ').collect();

    let a: u32 = inputs[0].trim().parse().unwrap();
    let b: u32 = inputs[1].trim().parse().unwrap();

    println!("{}", a + b);
}
