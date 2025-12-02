let filename = "day2/input.in"

let list_to_pair = function
  | [a; b] -> (a, b)
  | _ -> failwith "Expected list with 2 elements"

let parse line = 
  String.split_on_char ',' line 
  |> List.map (String.split_on_char '-') 
  |> List.map (List.map int_of_string)
  |> List.map list_to_pair

let max_list_pairs lst =
  let rec aux ans = function
  | [] -> ans
  | (a, b) :: tl -> aux (max (max a b) ans) tl
  in aux 0 lst

let int_lenght n = 
  let rec aux ans = function
  | 0 -> ans
  | x -> aux (ans + 1) (x / 10)
  in
  aux 0 n 
  
let rec pow a = function
  | 0 -> 1
  | b -> a * pow a (b - 1)
  
let rec check n = function 
  | [] -> false
  | (l, r) :: tl -> if l <= n && n <= r then true else check n tl

let intervals = Advent.read_line filename |> parse
let max_lenght = int_lenght (max_list_pairs intervals)
let rec solve ans = function
  | 0 -> ans
  | n -> 
    let x = n * (pow 10 (int_lenght n) + 1) in 
    solve (ans + if check x intervals then x else 0) (n - 1)

let () =
  solve 0 (pow 10 (max_lenght / 2) - 1)
  |> Printf.printf "%d\n"