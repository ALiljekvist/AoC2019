pub fn run_code(mut code: Vec<i64>, user_input: Vec<i64>) -> i64 {
    let mut i: usize = 0;
    let mut j: usize = 0;
    while i < code.len() {
        let mut instruction = code[i];
        let opcode: i64 = instruction % 100;
        instruction = instruction / 100;
        if opcode == 99 {
            break;
        }
        else if opcode == 1 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            let addr = code[i+3] as usize; // mode3 always positional - given
            code[addr as usize] = val1 + val2;
            i = i + 4;
        }
        else if opcode == 2 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            let addr = code[i+3] as usize; // mode3 always positional - given
            code[addr as usize] = val1 * val2;
            i = i + 4;
        }
        else if opcode == 3 {
            let addr: usize = code[i+1] as usize;
            let val = user_input[j];
            j = j + 1;
            code[addr] = val;
            i = i + 2;
        }
        else if opcode == 4 {
            let mode = instruction % 10;
            let val = if mode == 1 {code[i+1]} else if mode == 0 {code[code[i+1] as usize]} else {panic!("faulty mode2: {}", mode)};
            return val;
        }
        else if opcode == 5 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            if val1 != 0 {
                i = val2 as usize;
            }
            else {
                i = i + 3;
            }
        }
        else if opcode == 6 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            if val1 == 0 {
                i = val2 as usize;
            }
            else {
                i = i + 3;
            }
        }
        else if opcode == 7 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            let addr = code[i+3] as usize; // mode3 always positional - given
            code[addr] = if val1 < val2 {1} else {0};
            i = i + 4;
        }
        else if opcode == 8 {
            let mode1 = instruction % 10;
            instruction = instruction / 10;
            let mode2 = instruction % 10;
            let val1 = if mode1 == 1 {code[i+1]} else if mode1 == 0 {code[code[i+1] as usize]} else {panic!("faulty mode1: {}", mode1)};
            let val2 = if mode2 == 1 {code[i+2]} else if mode2 == 0 {code[code[i+2] as usize]} else {panic!("faulty mode2: {}", mode2)};
            let addr = code[i+3] as usize; // mode3 always positional - given
            code[addr] = if val1 == val2 {1} else {0};
            i = i + 4;
        }
        else {
            panic!("Faulty opcode {}", opcode);
        }
    }
    return 0;
}
