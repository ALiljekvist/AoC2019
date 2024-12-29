use std::fs;

fn segment_images(nums: &str) -> Vec<Vec<u32>> {
    let mut images: Vec<Vec<u32>> = Vec::new();
    let sequence_length:u32 = 25*6;
    let num_layers: usize = nums.len()/(sequence_length as usize);
    for i in 0..num_layers {
        let image_sequence: Vec<u32> = nums[i*sequence_length as usize..(i+1)*sequence_length as usize]
                                        .split("")
                                        .filter(|x| !x.is_empty())
                                        .map(|x| x.parse().unwrap()).collect();
        images.push(image_sequence)
    }
    return images
}

fn fill_image(images: Vec<Vec<u32>>) -> Vec<u32> {
    let mut image = vec![2; 25*6];
    for layer in images.iter() {
        for (i, color) in layer.iter().enumerate() {
            if image[i] == 2 {
                if color != &2 {
                    image[i] = *color;
                }
            }
        }
    }
    return image
}

fn main() {
    let nums = fs::read_to_string("input.txt").unwrap().replace("\n","");
    let images = segment_images(&nums);
    let mut min_0 = 0;
    let mut result1 = 0;
    for (i, layer) in images.iter().enumerate() {
        let nbr_0 = layer.iter().filter(|x| *x == &0).count();
        if nbr_0 < min_0 || i == 0 {
            let nbr_1 = layer.iter().filter(|x| *x == &1).count();
            let nbr_2 = layer.iter().filter(|x| *x == &2).count();
            result1 = nbr_1 * nbr_2;
            min_0 = nbr_0;
        }
    }
    println!("Result for part 1: {}", result1);
    let final_image = fill_image(images);
    let mut message: String = String::new();
    for (i,num) in final_image.iter().enumerate() {
        if i % 25 == 0 && i != 0 {
            message.push_str("\n")
        }
        message.push_str(if num == &1 {"0"} else {" "});
    }
    println!("{}", message);
}
