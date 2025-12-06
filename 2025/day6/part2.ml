let filename = "day6/input.in"

let lines = Advent.read_lines filename
let max_len = List.fold_left (fun acc s -> max acc (String.length s)) 0 lines

let add_padding s =
  let len = String.length s in
  if len < max_len then s ^ String.make (max_len - len) ' '
  else s

let parsed_lines = 
  lines
  |> List.map add_padding
  |> List.map (fun s -> List.of_seq (String.to_seq s))
  |> Advent.zip
  |> List.map (List.filter (fun c -> c <> ' '))
  |> List.map (fun chars -> String.of_seq (List.to_seq chars))
  |> List.filter (fun s -> s <> "")
  |> List.rev

let rec solve lines stack acc =
  match lines with
  | [] -> acc
  | x :: xs ->
    let len = String.length x - 1 in
    let op = String.get x len in
    let num = if len > 0 then int_of_string (String.sub x 0 len) else 0 in
    match op with
    | '+' -> solve xs [] (acc + List.fold_left ( + ) num stack)
    | '*' -> solve xs [] (acc + List.fold_left ( * ) num stack)
    | _ -> let d = int_of_char op - int_of_char '0' in solve xs ((num * 10 + d) :: stack) acc

let () =
  solve parsed_lines [] 0
  |> Printf.printf "%d\n"