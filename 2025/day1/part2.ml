let filename = "day1/input.in"

let parse line = 
  let dir = line.[0] in
  let r = int_of_string (String.sub line 1 (String.length line - 1)) in
  (dir, r)

let rec password cur = function
  | [] -> [cur]
  | ('L', r) :: lst -> cur :: password (-r) lst
  | ('R', r) :: lst -> cur :: password r lst
  | _ -> failwith "Invalid input"

let rec separete_number n = 
  if abs n <= 99 then [n]
  else
    let sign = if n < 0 then -1 else 1 in
    (sign * 99) :: separete_number (n - (sign * 99))

let rec prefix_sum acc = function
  | [] -> [acc]
  | hd :: lst -> acc :: prefix_sum (acc + hd) lst

let pairwise lst =
  let rec aux prv xs =
    match xs with
    | [] -> []
    | hd :: xs' -> (prv, hd) :: aux hd xs'
  in
  match lst with
  | [] -> []
  | hd :: tl -> aux hd tl

let clamp100 n = (n / 100) - if n < 0 then 1 else 0
let count (a, b) =
  match (a, b) with
  | x, _ when x mod 100 = 0 -> 0
  | _, x when x mod 100 = 0 -> 1
  | _ -> if clamp100 a <> clamp100 b then 1 else 0

let () = 
  Advent.read_lines filename
  |> List.map parse
  |> password 50
  |> List.map separete_number
  |> List.flatten
  |> prefix_sum 0
  |> pairwise
  |> List.map count
  |> List.fold_left ( + ) 0
  |> Printf.printf "%d\n"