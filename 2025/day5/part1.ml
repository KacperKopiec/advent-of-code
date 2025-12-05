let filename = "day5/input.in"

let lines = Advent.read_lines filename

let parse = function
  | [l; r] -> (int_of_string l, int_of_string r)
  | _ -> failwith "invalid input"
  
let intervals = 
  let rec aux = function
  | hd :: tl -> if hd = "" then [] else hd :: aux tl
  | _ -> failwith "invalid input"
  in
  aux lines 
  |> List.map (fun s -> String.split_on_char '-' s) 
  |> List.map parse

let products =
  let rec aux = function
  | hd :: tl -> if hd = "" then [] else hd :: aux tl
  | _ -> failwith "invalid input"
  in 
  List.map (fun x -> int_of_string x) (aux (List.rev lines))

let check id lst =
  let rec aux ans = function
  | [] -> ans 
  | (l, r) :: tl -> aux (if l <= id && id <= r then 1 else ans) tl
  in
  aux 0 lst

let () =
  products
  |> List.map (fun x -> check x intervals)
  |> List.fold_left ( + ) 0
  |> Printf.printf "%d\n"