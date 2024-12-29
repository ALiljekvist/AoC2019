use std::fs;
mod int_comp;
use int_comp::run_code;

fn create_combinations() -> Vec<Vec<i64>> {
    let mut combinations: Vec<Vec<i64>> = Vec::new();
    let mut start: Vec<i64> = Vec::new();
    for i in 0..5 {
        start.push(i as i64);
        for j in 0..5 {
            if !start.contains(&(j as i64)) {
                start.push(j);
                for k in 0..5{
                    if !start.contains(&(k as i64)){
                        start.push(k);
                        for l in 0..5 {
                            if !start.contains(&(l as i64)){
                                start.push(l);
                                for m in 0..5 {
                                    if !start.contains(&(m as i64)) {
                                        start.push(m);
                                        combinations.push(start.clone());
                                        start.pop();
                                    }
                                }
                                start.pop();
                            }
                        }
                        start.pop();
                    }
                }
                start.pop();
            }
        }
        start.pop();
    }
    return combinations;
}

fn main() {
    let int_code: Vec<i64> = fs::read_to_string("input.txt")
                            .unwrap()
                            .replace("\n","")
                            .split(",")
                            .filter(|x| !x.is_empty())
                            .map(|x| x.parse::<i64>().unwrap()).collect();
    let combinations: Vec<Vec<i64>> = create_combinations();
    let mut result: i64 = 0;
    for comb in combinations.iter() {
        let mut res: i64 = 0;
        let mut amplifiers: Vec<Vec<i64>> = Vec::new();
        for num in comb.iter() {
            let input: Vec<i64> = vec![*num, res]; 
            let (res_i, mem) = run_code(int_code.clone(), input);
            res = res_i;
            amplifiers.push(mem);
            if res > result {
                result = res;
            }
        }
    }
    println!("Maximum result: {}",  result);
}
