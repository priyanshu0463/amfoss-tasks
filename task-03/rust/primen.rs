use std::io;

fn main() {
    println!("Enter the number: ");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let x: u32 = input.trim().parse().expect("Invalid input");

    for i in 2..=x {
        let mut f = 0;

        for j in 2..i {
            if i % j == 0 {
                f = 1;
                break;
            }
        }

        if f == 0 {
            println!("{}: prime", i);
        }
    }
}
