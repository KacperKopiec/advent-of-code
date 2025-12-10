let filename = "day10/input.in"

let parse lst = 
  let parse_lights s =
    String.sub s 1 (String.length s - 2)
    |> String.to_seq
    |> List.of_seq
    |> List.mapi (fun i c -> if c = '#' then (1 lsl i) else 0)
    |> List.fold_left ( + ) 0
  in
  let parse_button s =
    String.sub s 1 (String.length s - 2)
    |> String.split_on_char ','
    |> List.map (fun x -> 1 lsl (int_of_string x))
    |> List.fold_left ( + ) 0
  in
  let parse_buttons lst = List.map parse_button lst in
  let first = List.hd lst in
  let last = List.hd (List.rev lst) in
  let mid = List.tl lst |> List.rev |> List.tl in
  (parse_lights first, parse_buttons mid, last)

let lines = Advent.read_lines filename |> List.map(fun s -> parse (String.split_on_char ' ' s))

let solve n lst =
  let inf = List.length lst + 1 in
  let rec aux x acc lst = 
    if x = n then acc
    else match lst with
    | [] -> inf
    | hd :: tl -> min (aux x acc tl) (aux (x lxor hd) (acc + 1) tl)
  in
  aux 0 0 lst

let () =
  List.fold_left (fun acc (n, buttons, _) -> acc + solve n buttons) 0 lines
  |> Printf.printf "%d\n"
