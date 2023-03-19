fn main() {
    let stop = 1000;
    let mut final_num = 0;
    for i in 0..stop {
        if i%3==0 || i%5==0 {
            final_num+=i;
        }
    }
    println!("{}", final_num);
}
