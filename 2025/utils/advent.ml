let read_lines filename = 
  In_channel.with_open_text filename In_channel.input_all
  |> String.trim
  |> String.split_on_char '\n'

let read_line filename = 
  In_channel.with_open_text filename In_channel.input_all
  |> String.trim

let int_lenght n = 
  let rec aux acc = function
  | 0 -> acc
  | n -> aux (acc + 1) (n / 10)
  in 
  aux 0 n

let rec pow a b =
  match b with
  | 0 -> 1
  | x -> let y = pow a (x / 2) in y * y * if x mod 2 = 1 then a else 1 

let directions = [(-1, 0); (0, 1); (1, 0); (0, -1)]
let diagonals = [(-1, -1); (-1, 1); (1, 1); (1, -1)]
let all_directions = directions @ diagonals

let neighbours grid y x dirs =
  let rows = Array.length grid in
  let cols = Array.length grid.(0) in
  dirs
  |> List.to_seq
  |> Seq.filter_map (fun (dy, dx) ->
    let ny = y + dy in
    let nx = x + dx in
    if 0 <= ny && ny < rows && 0 <= nx && nx < cols then Some (ny, nx) else None  
  )