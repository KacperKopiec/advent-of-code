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

let events =
  let rec aux = function
  | [] -> []
  | (l, r) :: tl -> (l, 0) :: (r + 1, 1) :: aux tl
  in
  aux intervals
  |> List.sort (fun (a, b) (c, d) -> if a <> c then a - c else b - d)

let merge lst =
  let rec aux start depth = function
  | (x, 0) :: tl -> aux (if depth = 0 then x else start) (depth + 1) tl
  | (x, 1) :: tl -> if depth = 1 then (x - start) :: aux 0 0 tl else aux start (depth - 1) tl
  | _ -> []
  in
  aux 0 0 lst


let () =
  events
  |> merge
  |> List.fold_left ( + ) 0
  |> Printf.printf "%d\n"