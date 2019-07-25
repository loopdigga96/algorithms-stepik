use std::io;
use std::vec::Vec;

fn fib(n: u64) -> u64 {
    let mut a: u64 = 0;
    let mut b: u64 = 1;

    for i in 2..n+1 {
        let c = a + b;
        a = b.clone();
        b = c.clone();
    }
    b
}

fn main() {
    let reader = io::stdin();
    let mut buffer: String = String::new();

    reader.read_line(&mut buffer)
        .ok()
        .expect("ERRORMSG");
    let n: u64 = buffer.trim().parse().unwrap();
    println!("{}", fib(n));

}
