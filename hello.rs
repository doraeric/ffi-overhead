use std::{
    env,
    ffi::{c_int, c_longlong},
};

#[link(name = ":newplus/libnewplus.so")]
extern "C" {
    fn plusone(x: c_int) -> c_int;
    fn current_timestamp() -> c_longlong;
}

fn run(count: c_int) {
    unsafe {
        // start immediately
        let start = current_timestamp();

        let mut x = 0;
        while x < count {
            x = plusone(x);
        }

        let end = current_timestamp();
        let elapsed = end - start;

        println!("{}", elapsed);
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() == 1 {
        println!("First arg (0 - 2000000000) is required.");
        return;
    }
    let count = args[1].parse::<i32>().unwrap();
    if count <= 0 || count > 2000000000 {
        println!("Must be a positive number not exceeding 2 billion.");
        return;
    }
    run(count as c_int);
}
