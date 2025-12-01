let filename = "day1/input.in"

let parse line = 
  let dir = line.[0] in
  let r = int_of_string (String.sub line 1 (String.length line - 1)) in
  (dir, r)

let rec password cur = function
  | [] -> [cur]
  | ('L', r) :: lst -> cur :: password ((cur - r) mod 100) lst
  | ('R', r) :: lst -> cur :: password ((cur + r) mod 100) lst
  | _ -> failwith "Invalid input"

let () = 
  Advent.read_lines filename
  |> List.map parse
  |> password 50
  |> List.fold_left (fun acc x -> if x = 0 then acc + 1 else acc) 0 
  |> Printf.printf "%d\n"